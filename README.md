# XPath-expressions

![](https://travis-ci.com/orf/xpath-expressions.svg?branch=master)
![](https://badge.fury.io/py/xpath-expressions.svg)


This is a small, lightweight Python 3.5+ library to aide in the manipulations of
xpath expressions. It allows you to manipulate them as Python objects with
Python expressions and operators.

### Install

`pip install xpath-expressions`


### Quickstart

```python
from xpath import Expression, Attribute

root_node = Expression('/root')
print(root_node.children)                 # /root/*
print(root_node.name)                     # name(/root)
print(root_node.attributes[1])            # /root/@*[1]
print(root_node / 'abc' / 'def')          # /root/abc/def

# Filtering expressions:
print(root_node.text == 'abc')            # /root/text()='abc'

expr = Attribute('abc') == 'def'
print(expr)                               # @abc='def'
print(root_node.children[expr])           # /root/*[@abc='def']

# The library handles quoting for you:
expr = Attribute('abc') == "def'"
filtered2 = root_node.children[expr]      # /root/*[@abc="def'"]

# You can use xpath functions:
from xpath import func
# Pass arguments like usual
expr = func.string_length(root_node.name)
print(expr)                               # string-length(name(/root/))

# And treat those as normal expressions
print(expr == 5)                          # string-length(name(/root/)) == 5

# The library normalizes python reserved names:
print(func.or_())                         # or()

# Use custom namespaces
from xpath import Functions
ns_functions = Functions('my-ns:')
print(ns_functions.something())           # my-ns:something()
```
