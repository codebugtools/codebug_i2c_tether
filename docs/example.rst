########
Examples
########

Basic usage
===========

::

    >>> import codebug_i2c_tether
    >>> cb = codebug_i2c_tether.CodeBug()
    >>> cb.open()
    >>> cb.set_pixel(0, 0, 1)

You don't have to call ``open`` when using Python's ``with`` syntax::

    >>> import codebug_i2c_tether
    >>> with codebug_i2c_tether.CodeBug() as codebug:
    ...     codebug.set_pixel(2, 2, 1)
    ...     codebug.set_row(0, 0x1f)
    ...     codebug.set_col(4, 0x1f)

You can view all methods by running::

    >>> import codebug_i2c_tether
    >>> cb = codebug_i2c_tether.CodeBug()
    >>> help(cb)
