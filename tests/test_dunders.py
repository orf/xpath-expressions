from xpath import Expression, arg_to_representation
import operator
import pytest


all_operators = [
    (operator.eq, '='),
    (operator.ne, '!='),
    (operator.lt, '<'),
    (operator.gt, '>'),
    (operator.le, '<='),
    (operator.ge, '>='),
    (operator.add, '+'),
    (operator.sub, '-'),
    (operator.mul, '*'),
    (operator.truediv, '/'),
    (operator.and_, ' and '),
    (operator.or_, ' or ')
]


@pytest.mark.parametrize('op,joiner', all_operators)
def test_operator(value_expr, op, joiner):
    result = op(value_expr, 1)
    assert isinstance(result, Expression)
    assert result.string == value_expr.string + joiner + '1'


@pytest.mark.parametrize('op,joiner', all_operators)
def test_operator_expression(value_expr, op, joiner):
    other = Expression('test')
    result = op(value_expr, other)
    assert isinstance(result, Expression)
    if joiner == '/':
        assert result.string == value_expr.string + joiner + other.string
    else:
        assert result.string == value_expr.string + joiner + arg_to_representation(other)