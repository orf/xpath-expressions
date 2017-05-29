import pytest
from xpath import Expression
from lxml import etree


@pytest.fixture
def expr():
    return Expression('.')


@pytest.fixture
def value_expr():
    return Expression('1')


@pytest.fixture
def xml_root():
    return Expression('/root')


@pytest.fixture(scope='session')
def xml_doc():
    return etree.fromstring("""
    <root abc='123'>
        <!-- A comment -->
        <node1 id='1'>Node1</node1>
        <node2 id='2'>Node2</node2>
    </root>
    """)
