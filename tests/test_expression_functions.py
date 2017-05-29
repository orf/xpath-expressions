from xpath import IterableExpression, Expression, Function, AttributesExpression, CommentsExpression


def test_text_returns_iterable(expr):
    assert isinstance(expr.text, IterableExpression)


def test_text_is_iterable(expr):
    assert len(list(expr.text(5))) == 5


def test_any_node(expr):
    assert isinstance(expr.any_node, Expression)


def test_add_path(expr):
    new_expr = expr.add_path('/test')
    assert new_expr is not expr
    assert new_expr.string == expr.string + '/test'


def test_value_returns_string(expr):
    assert expr.value() == expr.string


def test_attributes_returns_attributes_expression(expr):
    assert isinstance(expr.attributes, AttributesExpression)


def test_comments_returns_comments_expression(expr):
    assert isinstance(expr.comments, CommentsExpression)


def test_children_returns_iterable_expression(expr):
    assert isinstance(expr.children, IterableExpression)


def test_expr_works():
    assert Expression('test').expr('==', 1) == 'test==1'

