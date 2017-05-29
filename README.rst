xpath-expressions
=================

.. image:: https://travis-ci.org/orf/xpath-expressions.svg?branch=master
    :target: https://travis-ci.org/orf/xpath-expressions

This is a Python library to aide in the manipulations of xpath expressions, allowing
you to manipulate them as Python objects with Python expressions. For example:


.. code:: python

  from xpath import Expression as E, Attribute as A

  root_node = E('/root')
  all_children = root_node.children         # /root/*
  root_node_name = root_node.name           # name(/root)
  an_attribute = root_node.attributes[1]    # /root/@*[1]

  attrs = A('abc') == 'def'                # @abc='def'
  filtered = root_node.children[attrs]      # /root/*[@abc='def']

  # You can also use xpath functions:
  from xpath.functions import string_length
  length = string_length(root_node.name)    # string-length(name(/root/))
  is_length_5 = length == 5                 # string-length(name(/root/)) == 5


There is a lot more you can do, check out the main Expression class.
