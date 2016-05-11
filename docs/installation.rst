############
Installation
############

Setting up CodeBug
==================
In order to use CodeBug with codebug_i2c_tether you need to program CodeBug
with ``codebug_i2c_tether.cbg`` (|firmwaredownload|).

To do this, hold down button A and plug in CodeBug via USB --- it should
appear as a USB drive --- then copy the ``codebug_i2c_tether.cbg`` file onto it.
CodeBug is now ready to be used via serial USB. Press button B to exit
programming mode.

.. note:: When CodeBug is connected to a computer via USB is should now
          appear as a serial device. To reprogram CodeBug: hold down
          button A and (re)plug it into a USB port.

Unplug CodeBug, remove the battery (if one is inserted) and then plug
CodeBug's extension header into the I2C GPIO pins on the Raspberry Pi.
These are the left-most inner row GPIO pins on the Raspberry Pi with
CodeBug facing in.

Here is a diagram of this configuration::

    +-------------------------------------------------------+
    | oooooooooooooooooooooooooooooooooooooooo <- GPIO pins |
    | XXXXXXoooooooooooooooooooooooooooooooooo              |
    |    ^                                                  |
    |    |                                                  |
    | CodeBug                                               |
    |                                                       |
    |                                                       |
    |                             RPi                       |
    |                                                       |
    |                                                       |
    |                                                       |
    +-------------------------------------------------------+

And here is a picture of the same thing:

.. image:: codebug_i2c_tether_rpi_pins.jpg
   :alt: Image showing the back of CodeBug plugged into the correct GPIO pins on a Raspberry Pi 2.
   :align: center


Install codebug_i2c_tether on a Raspberry Pi
============================================
First, make sure you have enabled I2C by running::

    sudo raspi-config

and then navigating to::

    Advanced Options > Would you like the I2C interface to be enabled? > Yes
    Would you like the I2C kernel module to be loaded by default? > Yes

Then reboot.

Install Python
--------------
Python should already be installed but for good measure::

    sudo apt-get install python3

To install pip, securely download `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_.

Then run the following::

    sudo python3 get-pip.py


Install codebug_i2c_tether
--------------------------
To install codebug_i2c_tether, open up a terminal and type::

    pip3 install codebug_i2c_tether

To test it has worked, plug in CodeBug and open a Python shell by typing::

    python3

Your command prompt should have changed to::

    >>> _

Now type::

    >>> import codebug_i2c_tether
    >>> with codebug_i2c_tether.CodeBug() as codebug:
    ...     codebug.set_pixel(2, 2, 1)
    ...

The middle pixel on your CodeBug should light up.

See :ref:`examples-label` for more ways to use codebug_i2c_tether.
