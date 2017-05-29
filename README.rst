xpath-expressions
=================

|ci| |pypi|

.. |ci| image:: https://travis-ci.org/orf/xpath-expressions.svg?branch=master
    :target: https://travis-ci.org/orf/xpath-expressions

.. |pypi| image:: https://badge.fury.io/py/xpath-expressions.svg
    :target: https://badge.fury.io/py/xpath-expressions


.. code:: shell

  pip install xpath-expressions

This is a small, lightweight Python 3.5+ library to aide in the manipulations of
xpath expressions, allowing you to manipulate them as Python objects with
Python expressions. For example:


.. code:: python

  from xpath import Expression as E, Attribute as A

  root_node = E('/root')
  all_children = root_node.children         # /root/*
  root_node_name = root_node.name           # name(/root)
  an_attribute = root_node.attributes[1]    # /root/@*[1]

  attrs = A('abc') == 'def'                 # @abc='def'
  filtered = root_node.children[attrs]      # /root/*[@abc='def']

  # The library handles quoting for you:
  attr2 = A('abc') == "def'"
  filtered2 = root_node.children[attrs]     # /root/*[@abc="def'"]

  # You can also use xpath functions:
  from xpath.functions import string_length
  length = string_length(root_node.name)    # string-length(name(/root/))
  is_length_5 = length == 5                 # string-length(name(/root/)) == 5

There is a lot more you can do, check out the main Expression class.

Not all functions are defined in the ``xpath.functions` module. To add your own,
simply define: ``myfunc = Function('my-func')``. Please make a merge request if
you want some more added to the library!

Why
---
Manipulating xpath expressions as strings is error-prone and annoying. This
library makes it really simple.

It was split out from XCat_ into a separate module.

.. _XCat: https://github.com/orf/xcat/