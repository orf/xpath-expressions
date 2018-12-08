from xpath import func, Functions, Function, identifier_to_function
import pytest


@pytest.mark.parametrize('name,expected', (
        ('count', 'count'),
        ('is_doc', 'is-doc'),
        ('true_', 'true')
))
def test_getattr(name, expected):
    result = getattr(func, name)
    assert isinstance(result, Function)
    assert result.string == expected


def test_namespace():
    namespace_functions = Functions('abc:')
    assert namespace_functions.count.string == 'abc:count'
