xpath-expressions
=================

.. image:: https://travis-ci.org/orf/xpath-expressions.svg?branch=master
    :target: https://travis-ci.org/orf/xpath-expressions

This is a Python library to aide in the manipulations of xpath expressions, allowing
you to manipulate them as Python objects with Python expressions. For example:


.. code-block:: html
    from xpath import Expression as E, Literal as L

    root_node = E('/root')
    all_children = root_node.children         # /root/*
    root_node_name = root_node.name           # name(/root)
    an_attribute = root_node.attributes[1]    # /root/@*[1]

    attrs = L('@abc') == 'def'                # @abc='def'
    filtered = root_node.children[attrs]      # /root/*[@abc='def']


There is a lot more you can do, check out the main Expression class.
