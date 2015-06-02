########
Examples
########

Basic usage
===========

::

    >>> import codebug_i2c_tether
    >>> with codebug_i2c_tether.CodeBug() as codebug:
    ...     codebug.set_pixel(0, 0, 1)
    ...     codebug.set_row(0, 0x1f)
    ...     codebug.set_col(4, 0x1f)
