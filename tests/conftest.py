import pytest
from xpath import Expression


@pytest.fixture
def expr():
    return Expression('.')


@pytest.fixture
def value_expr():
    return Expression('1')
