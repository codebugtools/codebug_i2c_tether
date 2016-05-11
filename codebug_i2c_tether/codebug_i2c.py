import struct
from .i2c import I2CMaster, writing_bytes, writing, reading


STATUS_OKAY = 0
STATUS_BUSY = 1

ROUTINE_QUERY =  0
ROUTINE_GET =  1
ROUTINE_GET_BULK =  2
ROUTINE_SET =  3
ROUTINE_SET_BULK =  4


class CodeBugI2CMaster(I2CMaster):
    """Interface to CodeBug I2C slave."""

    def __init__(self, bus, device_address):
        super().__init__(bus)
        self.device_address = device_address

    def get(self, address):
        """Runs a CodeBug I2C GET command. Returns the data as a byte object.
        To get the integer value, access the first element like so:

            with CodeBugI2CMaster(0, 0) as codebug_i2c_master:
                integer_value = codebug_i2c_master.get(0)[0]

        """
        return self.transaction(writing_bytes(self.device_address,
                                              ROUTINE_GET,
                                              address),
                                reading(self.device_address, 1))[0]

    def get_bulk(self, start_address, length):
        """Runs a CodeBug I2C GET_BULK command. Returns the data as a byte
        object. To get the integer values, access the elements like so:

            with CodeBugI2CMaster(0, 0) as codebug_i2c_master:
                byte_values = codebug_i2c_master.get_bulk(2)
                integer_value0 = byte_values[0]
                integer_value1 = byte_values[1]

        """
        return self.transaction(writing_bytes(self.device_address,
                                              ROUTINE_GET_BULK,
                                              start_address,
                                              length),
                                reading(self.device_address, length))[0]

    def set(self, address, value):
        """Runs a CodeBug I2C SET command and sets address to value."""
        self.transaction(writing_bytes(self.device_address,
                                       ROUTINE_SET,
                                       address,
                                       value))

    def set_bulk(self, start_address, values):
        """Runs a CodeBug I2C SET_BULK command and sets addresses starting
        from start_address to the values given.
        """
        packet = (self.device_address,
                  ROUTINE_SET_BULK,
                  start_address,
                  len(values))
        packet += tuple(values)
        self.transaction(writing_bytes(*packet))

    def and_mask(self, address, mask):
        """Logical AND the address with mask."""
        value = struct.unpack('B', self.get(address))[0]
        self.set(address, value & mask)

    def or_mask(self, address, mask):
        """Logical OR the address with mask."""
        value = struct.unpack('B', self.get(address))[0]
        self.set(address, value | mask)

    def set_bit(self, address, bit_index, state):
        """Sets a bit at address to state."""
        if state:
            self.or_mask(address, 1 << bit_index)
        else:
            self.and_mask(address, 0xff ^ (1 << bit_index))

    def get_bit(self, address, bit_index):
        """Returns a bit from an address."""
        value = struct.unpack('B', self.get(address))[0]
        return (value >> bit_index) & 0x1
