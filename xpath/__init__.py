from functools import singledispatch, lru_cache
from typing import Union, List, Iterable


class Expression:
    __slots__ = ('string',)

    def __init__(self, string=""):
        self.string = string

    def __repr__(self):
        return "<Expression: %s>" % self.string

    @property
    def text(self) -> 'IterableExpression':
        return IterableExpression(self.string + "/text()")

    @property
    def any_node(self) -> 'Expression':
        return Expression(self.string + "/node()")

    def add_path(self, path) -> 'Expression':
        return Expression(self.string + path)

    @property
    def count(self) -> 'Expression':
        return func.count(self)

    @property
    def name(self) -> 'Expression':
        return func.name(self)

    def value(self) -> str:
        return self.string

    @property
    def attributes(self) -> 'AttributesExpression':
        return AttributesExpression("%s/@*" % self.string)

    @property
    def comments(self) -> 'CommentsExpression':
        return CommentsExpression(self.string + "/comment()")

    @property
    def children(self) -> 'IterableExpression':
        return IterableExpression("%s/*" % self.string)

    def expr(self, symbol, value) -> 'Expression':
        return Expression("%s%s%s" % (self.value(), symbol, arg_to_representation(value)))

    def __getitem__(self, item) -> Union[List['Expression'], 'Expression']:
        if isinstance(item, slice):
            return [
                self[idx]
                for idx in range(item.start or 1, item.stop, item.step or 1)
            ]

        return Expression("%s[%s]" % (self.value(), item))

    def __eq__(self, other) -> 'Expression':
        return self.expr("=", other)

    def __ne__(self, other) -> 'Expression':
        return self.expr("!=", other)

    def __lt__(self, other) -> 'Expression':
        return self.expr("<", other)

    def __gt__(self, other) -> 'Expression':
        return self.expr(">", other)

    def __le__(self, other) -> 'Expression':
        return self.expr("<=", other)

    def __ge__(self, other) -> 'Expression':
        return self.expr(">=", other)

    def __add__(self, other) -> 'Expression':
        return self.expr("+", other)

    def __sub__(self, other) -> 'Expression':
        return self.expr("-", other)

    def __mul__(self, other) -> 'Expression':
        return self.expr("*", other)

    def __truediv__(self, other) -> 'Expression':
        return Expression('{string}/{other}'.format(string=self.string, other=other))

    def __and__(self, other) -> 'Expression':
        return self.expr(" and ", other)

    def __or__(self, other) -> 'Expression':
        return self.expr(" or ", other)

    def __str__(self):
        return "%s" % self.value()


class Node(Expression):
    pass


class IterableExpression(Expression):
    def __call__(self, count) -> Iterable['Expression']:
        for i in range(1, count + 1):
            yield self[i]


class CommentsExpression(IterableExpression):
    pass


class AttributesExpression(IterableExpression):
    pass


class Attribute(Expression):
    def __repr__(self):
        return "<Attribute: %s>" % self.string

    def value(self) -> str:
        return "@%s" % self.string


class Function(Expression):
    def get_string(self, args) -> str:
        str_args = ",".join((arg_to_representation(a) for a in args))
        return "%s(%s)" % (self.string, str_args)

    def __str__(self):
        return self.get_string(tuple)

    def __call__(self, *args) -> 'Expression':
        return Expression(self.get_string(args))

    def __repr__(self):
        return "<Function: %s>" % self.string


class Literal(Expression):
    pass


@singledispatch
def arg_to_representation(other):
    return str(other)


@arg_to_representation.register(str)
def _(other):
    if "'" not in str(other):
        return "'%s'" % other

    if '"' not in str(other):
        return '"%s"' % other

    safe_concat = ",".join(arg_to_representation(c) for c in str(other))
    safe_concat = safe_concat.replace('","', '')
    safe_concat = safe_concat.replace("','", '')
    return "concat(" + safe_concat + ")"


@arg_to_representation.register(Expression)
def _(other):
    return "(%s)" % other


@arg_to_representation.register(Literal)
def _(other):
    return str(other)


@lru_cache(maxsize=50)
def identifier_to_function(namespace, identifier):
    new_identifier = namespace + identifier.rstrip('_').replace('_', '-')
    return Function(new_identifier)


class Functions:
    def __init__(self, namespace=""):
        self.namespace = namespace

    def __getattr__(self, item) -> 'Function':
        return identifier_to_function(self.namespace, item)


A = Attribute
E = Expression
L = Literal
F = Function
N = Node

ROOT_NODE = E('/*[1]')

func = Functions()
