import codebug_i2c_tether.char_map
import codebug_i2c_tether.codebug_i2c


DEFAULT_I2C_BUS = 1
DEFAULT_I2C_ADDRESS = 0x18

NUM_CHANNELS = 8
OUTPUT_CHANNEL_INDEX = 5
INPUT_CHANNEL_INDEX = 6
IO_DIRECTION_CHANNEL = 7


class CodeBug(codebug_i2c_tether.codebug_i2c.CodeBugI2CMaster):

    def __init__(self, bus=DEFAULT_I2C_BUS, address=DEFAULT_I2C_ADDRESS):
        super().__init__(bus, address)

    def _int_input_index(self, input_index):
        """Returns an integer input index."""
        # 'A' is 4, 'B' is 5
        if isinstance(input_index, str):
            input_index = 4 if 'a' in input_index.lower() else 5
        return input_index

    def get_input(self, input_index):
        """Returns the state of an input. You can use 'A' and 'B' to
        access buttons A and B.

            >>> with CodeBug() as codebug:
            ...     codebug.get_input('A')  # switch A is unpressed
            ...
            0
            >>> codebug.get_input(0)  # assuming pad 0 is connected to GND
            1

        """
        input_index = self._int_input_index(input_index)
        return (self.get(INPUT_CHANNEL_INDEX)[0] >> input_index) & 0x1

    # def set_pullup(self, input_index, state):
    #     """Sets the state of the input pullups. Turn off to enable touch
    #     sensitive pads (bridge GND and input with fingers).

    #         >>> codebug = CodeBug()
    #         >>> codebug.set_pullup(0, 1)  # input pad 0 <10K OHMS
    #         >>> codebug.set_pullup(2, 0)  # input pad 2 <22M OHMS touch sensitive

    #     """
    #     state = 1 if state else 0
    #     input_index = self._int_input_index(input_index)
    #     self.set(PULLUP_CHANNEL_INDEX, state << input_index, or_mask=True)

    def set_output(self, output_index, state):
        """Sets the output at index to state. `1` or `True` is ON, `0` or
        `False` is OFF.
        """
        output_state = self.get(OUTPUT_CHANNEL_INDEX)[0]
        if state:
            output_state |= 1 << output_index
        else:
            output_state &= 0xff ^ (1 << output_index)
        self.set(OUTPUT_CHANNEL_INDEX, output_state)

    def set_leg_io(self, leg_index, direction):
        """Sets the I/O direction of the leg at index. 1 is Input, 0 is Output.
        """
        # io_config_state = leg_index in upper nibble and state in lower nibble
        io_config_state = ((leg_index << 4) & 0xf0) | (direction & 0x0f)
        self.set(IO_DIRECTION_CHANNEL, io_config_state)

    def clear(self):
        """Clears the LED's on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.clear()
            ...

        """
        self.set_bulk(0, (0,)*5)

    def set_row(self, row, val):
        """Sets a row of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.set_row(0, 0b10101)
            ...

        """
        self.set(row, val)

    def get_row(self, row):
        """Returns a row of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.get_row(0)
            ...
            21

        """
        return self.get(row)[0]

    def set_col(self, col, val):
        """Sets an entire column of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.set_col(0, 0b10101)
            ...

        """
        # TODO add and_mask into set packet
        rows = []
        row_bytes = self.get_bulk(0, 5)
        for row in range(5):
            row_state = row_bytes[row]
            state = (val >> (4 - row)) & 0x1  # state of column: 1 or 0
            if state:
                row_state |= 1 << (4 - col)
            else:
                row_state &= 0xff ^ (1 << (4 - col))
            rows.append(row_state)
        self.set_bulk(0, rows)

    def get_col(self, col):
        """Returns an entire column of LEDs on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.get_col(0)
            ...
            21

        """
        row_bytes = self.get_bulk(0, 5)
        c = 0
        for row_index in range(5):
            col_state = 0x1 & row_bytes[row_index] >> (4 - col)
            c |= col_state << (4 - row_index)
        return c

    def set_pixel(self, x, y, state):
        """Sets a pixel on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.set_pixel(0, 0, 1)
            ...

        """
        row_state = self.get_row(y)
        if state:
            row_state |= 1 << (4 - x)
        else:
            row_state &= 0xff ^ (1 << (4 - x))
        self.set_row(y, row_state)

    def get_pixel(self, x, y):
        """Returns the state of an LED on CodeBug.

            >>> with CodeBug() as codebug:
            ...     codebug.get_pixel(0, 0)
            ...
            1

        """
        return (self.get_row(y) >> (4 - x)) & 0x1

    def write_text(self, x, y, message, direction="right"):
        """Writes some text on CodeBug at LED (x, y).

            >>> with CodeBug() as codebug:
            ...     codebug.write_text(0, 0, 'Hello, CodeBug!')
            ...

        """
        s = codebug_i2c_tether.char_map.StringSprite(message, direction)
        self.clear()
        for row_i, row in enumerate(s.pixel_state):
            if (row_i - y) >= 0 and (row_i - y) <= 4:
                code_bug_pixel_row = 0
                for col_i, state in enumerate(row):
                    if col_i + x >= 0 and col_i + x <= 4:
                        code_bug_pixel_row |= state << 4 - (col_i + x)
                self.set(4-row_i+y, code_bug_pixel_row)
