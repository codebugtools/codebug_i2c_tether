import codebug_i2c_tether.char_map
import codebug_i2c_tether.codebug_i2c


DEFAULT_I2C_BUS = 1
DEFAULT_I2C_ADDRESS = 0x18

NUM_CHANNELS = 8
OUTPUT_CHANNEL_INDEX = 5
INPUT_CHANNEL_INDEX = 6
IO_DIRECTION_CHANNEL = 7



IO_DIGITAL_OUTPUT = 0
IO_DIGITAL_INPUT = 1
IO_ANALOGUE_INPUT = 2
IO_PWM_OUTPUT = 3

# CHANNEL_INDEX_ROW_0 = 0
# CHANNEL_INDEX_ROW_1 = 1
# CHANNEL_INDEX_ROW_2 = 2
# CHANNEL_INDEX_ROW_3 = 3
# CHANNEL_INDEX_ROW_4 = 4
(CHANNEL_INDEX_OUTPUT,
 CHANNEL_INDEX_LEG_INPUT,
 CHANNEL_INDEX_BUTTON_INPUT,
 CHANNEL_INDEX_ANALOGUE_CONF,
 CHANNEL_INDEX_ANALOGUE_INPUT,
 CHANNEL_INDEX_IO_DIRECTION_LEGS,
 CHANNEL_INDEX_PULLUPS,
 CHANNEL_INDEX_PWM_CONF_0,
 CHANNEL_INDEX_PWM_CONF_1,
 CHANNEL_INDEX_PWM_CONF_2,
 CHANNEL_INDEX_SERVO_PULSE_LENGTH,
 CHANNEL_INDEX_SERVO_CONF) = range(5, 17)





class CodeBug(codebug_i2c_tether.codebug_i2c.CodeBugI2CMaster):

    def __init__(self, bus=DEFAULT_I2C_BUS, address=DEFAULT_I2C_ADDRESS):
        super().__init__(bus, address)

    # def _int_input_index(self, input_index):
    #     """Returns an integer input index."""
    #     # 'A' is 4, 'B' is 5
    #     if isinstance(input_index, str):
    #         input_index = 4 if 'a' in input_index.lower() else 5
    #     return input_index

    # def get_input(self, input_index):
    #     """Returns the state of an input. You can use 'A' and 'B' to
    #     access buttons A and B.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.get_input('A')  # switch A is unpressed
    #         ...
    #         0
    #         >>> codebug.get_input(0)  # assuming pad 0 is connected to GND
    #         1

    #     """
    #     input_index = self._int_input_index(input_index)
    #     return (self.get(INPUT_CHANNEL_INDEX)[0] >> input_index) & 0x1

    # # def set_pullup(self, input_index, state):
    # #     """Sets the state of the input pullups. Turn off to enable touch
    # #     sensitive pads (bridge GND and input with fingers).

    # #         >>> codebug = CodeBug()
    # #         >>> codebug.set_pullup(0, 1)  # input pad 0 <10K OHMS
    # #         >>> codebug.set_pullup(2, 0)  # input pad 2 <22M OHMS touch sensitive

    # #     """
    # #     state = 1 if state else 0
    # #     input_index = self._int_input_index(input_index)
    # #     self.set(PULLUP_CHANNEL_INDEX, state << input_index, or_mask=True)

    # def set_output(self, output_index, state):
    #     """Sets the output at index to state. `1` or `True` is ON, `0` or
    #     `False` is OFF.
    #     """
    #     output_state = self.get(OUTPUT_CHANNEL_INDEX)[0]
    #     if state:
    #         output_state |= 1 << output_index
    #     else:
    #         output_state &= 0xff ^ (1 << output_index)
    #     self.set(OUTPUT_CHANNEL_INDEX, output_state)

    # def set_leg_io(self, leg_index, direction):
    #     """Sets the I/O direction of the leg at index. 1 is Input, 0 is Output.
    #     """
    #     # io_config_state = leg_index in upper nibble and state in lower nibble
    #     io_config_state = ((leg_index << 4) & 0xf0) | (direction & 0x0f)
    #     self.set(IO_DIRECTION_CHANNEL, io_config_state)

    # def clear(self):
    #     """Clears the LED's on CodeBug.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.clear()
    #         ...

    #     """
    #     self.set_bulk(0, (0,)*5)

    # def set_row(self, row, val):
    #     """Sets a row of LEDs on CodeBug.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.set_row(0, 0b10101)
    #         ...

    #     """
    #     self.set(row, val)

    # def get_row(self, row):
    #     """Returns a row of LEDs on CodeBug.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.get_row(0)
    #         ...
    #         21

    #     """
    #     return self.get(row)[0]

    # def set_col(self, col, val):
    #     """Sets an entire column of LEDs on CodeBug.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.set_col(0, 0b10101)
    #         ...

    #     """
    #     # TODO add and_mask into set packet
    #     rows = []
    #     row_bytes = self.get_bulk(0, 5)
    #     for row in range(5):
    #         row_state = row_bytes[row]
    #         state = (val >> (4 - row)) & 0x1  # state of column: 1 or 0
    #         if state:
    #             row_state |= 1 << (4 - col)
    #         else:
    #             row_state &= 0xff ^ (1 << (4 - col))
    #         rows.append(row_state)
    #     self.set_bulk(0, rows)

    # def get_col(self, col):
    #     """Returns an entire column of LEDs on CodeBug.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.get_col(0)
    #         ...
    #         21

    #     """
    #     row_bytes = self.get_bulk(0, 5)
    #     c = 0
    #     for row_index in range(5):
    #         col_state = 0x1 & row_bytes[row_index] >> (4 - col)
    #         c |= col_state << (4 - row_index)
    #     return c

    # def set_pixel(self, x, y, state):
    #     """Sets a pixel on CodeBug.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.set_pixel(0, 0, 1)
    #         ...

    #     """
    #     row_state = self.get_row(y)
    #     if state:
    #         row_state |= 1 << (4 - x)
    #     else:
    #         row_state &= 0xff ^ (1 << (4 - x))
    #     self.set_row(y, row_state)

    # def get_pixel(self, x, y):
    #     """Returns the state of an LED on CodeBug.

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.get_pixel(0, 0)
    #         ...
    #         1

    #     """
    #     return (self.get_row(y) >> (4 - x)) & 0x1

    # def write_text(self, x, y, message, direction="right"):
    #     """Writes some text on CodeBug at LED (x, y).

    #         >>> with CodeBug() as codebug:
    #         ...     codebug.write_text(0, 0, 'Hello, CodeBug!')
    #         ...

    #     """
    #     s = codebug_i2c_tether.char_map.StringSprite(message, direction)
    #     self.clear()
    #     for row_i, row in enumerate(s.pixel_state):
    #         if (row_i - y) >= 0 and (row_i - y) <= 4:
    #             code_bug_pixel_row = 0
    #             for col_i, state in enumerate(row):
    #                 if col_i + x >= 0 and col_i + x <= 4:
    #                     code_bug_pixel_row |= state << 4 - (col_i + x)
    #             self.set(4-row_i+y, code_bug_pixel_row)



# class CodeBug(SerialChannelDevice):
#     """Manipulates CodeBug over a USB serial connection."""

#     def __init__(self, serial_port=DEFAULT_SERIAL_PORT):
#         super(CodeBug, self).__init__(serial.Serial(serial_port, timeout=2))

    def get_input(self, input_index):
        """Returns the state of an input. You can use 'A' and 'B' to
        access buttons A and B.

            >>> codebug = CodeBug()
            >>> codebug.get_input('A')  # switch A is pressed
            1
            >>> codebug.get_input(0)  # assuming leg 0 is connected to GND
            0
            >>> codebug.get_input(4)  # extension I/O pin 4 is connected to GND
            0

        """
        if isinstance(input_index, str):
            channel_index = CHANNEL_INDEX_BUTTON_INPUT
            input_index = 0 if 'a' in input_index.lower() else 1
        else:
            channel_index = CHANNEL_INDEX_LEG_INPUT
        return self.get_bit(channel_index, input_index)

    def read_analogue(self, leg_index):
        """Reads the analogue value of the leg at leg_index. The leg must
        first be configured as an analogue input. For example:

            >>> codebug = CodeBug()
            >>> codebug.set_leg_io(0, IO_ANALOG_INPUT)
            >>> codebug.read_analogue(0)
            128

        """
        # set which leg to read (and do the read)
        self.set(CHANNEL_INDEX_ANALOGUE_CONF, leg_index)
        # return the value
        analogue_value = self.get(CHANNEL_INDEX_ANALOGUE_INPUT)
        return struct.unpack('B', analogue_value)[0]

    def set_pullup(self, input_index, state):
        """Sets the state of the input pullups. Turn off to enable touch
        sensitive pads (bridge GND and input with fingers).

            >>> codebug = CodeBug()
            >>> codebug.set_pullup(0, 1)  # input pad 0 <10K OHMS
            >>> codebug.set_pullup(2, 0)  # input pad 2 <22M OHMS touch sensitive

        """
        self.set_bit(CHANNEL_INDEX_PULLUPS, input_index, state)

    def set_output(self, output_index, state):
        """Sets the output index to state."""
        self.set_bit(CHANNEL_INDEX_OUTPUT, output_index, state)

    def get_output(self, output_index):
        """Returns the state of the output at index."""
        return self.get_bit(CHANNEL_INDEX_OUTPUT, output_index)

    def set_leg_io(self, leg_index, direction):
        """Sets the I/O direction of the leg at index. For example:

            >>> codebug = CodeBug()
            >>> codebug.set_leg_io(0, IO_DIGITAL_OUTPUT)
            >>> codebug.set_leg_io(0, IO_PWM_OUTPUT)
            >>> codebug.set_leg_io(1, IO_DIGITAL_INPUT)
            >>> codebug.set_leg_io(2, IO_ANALOG_INPUT)

        """
        if leg_index < 4:
            clear_mask = 0xff ^ (0b11 << leg_index * 2)
            direction_mask = (0b11 & direction) << leg_index * 2
            self.and_mask(CHANNEL_INDEX_IO_DIRECTION_LEGS, clear_mask)
            self.or_mask(CHANNEL_INDEX_IO_DIRECTION_LEGS, direction_mask)
        else:
            ext_index = leg_index - 4
            clear_mask = 0b11 << ext_index * 2
            direction_mask = (0b11 & direction) << ext_index * 2
            self.and_mask(CHANNEL_INDEX_IO_DIRECTION_EXT, clear_mask)
            self.or_mask(CHANNEL_INDEX_IO_DIRECTION_EXT, direction_mask)

    def pwm_on(self, t2_prescale, full_period, on_period):
        """Turns on the PWM generator with the given settings.

        :param t2_prescale: One of T2_PS_1_1, T2_PS_1_4, T2_PS_1_16
                            Scales down the 12MHz instruction clock by
                            1, 4 or 16.
        :param full_period: 8-bit value - which is scaled up to 10-bits
                            (<< 2) - to which timer 2 will count up to
                            before resetting PWM output to 1.
        :param on_period: 10-bit value to which timer 2 will count up to
                          before setting PWM output to 0. Use this with
                          full_period to control duty cycle. For
                          example:

                              # 12MHz / 16 with 50% duty cycle
                              codebug.pwm_on(T2_PS_1_16, 0xff, 0x200)

        """
        # full period
        self.set(CHANNEL_INDEX_PWM_CONF_0, full_period)
        self.set(CHANNEL_INDEX_PWM_CONF_1, on_period & 0xff)
        go_busy = 1
        top_two_bit_on_period = (on_period >> 8) & 0b11
        conf = go_busy << 4 | t2_prescale << 2 | top_two_bit_on_period
        self.set(CHANNEL_INDEX_PWM_CONF_2, conf)

    def pwm_freq(self, frequency):
        """Turns on the PWM generator with the given frequency. For example:

            >>> codebug = CodeBug()
            >>> codebug.set_leg_io(0, IO_PWM_OUTPUT)
            >>> codebug.pwm_freq(1046)
            >>> time.sleep(2)
            >>> codebug.pwm_off()

        """
        # calculate pwm settings
        # 12MHz / 16 = 750k ticks per second
        full_period = int(750000 / frequency) - 1
        # for 50% duty cycle: shift up by 2 then /(2 i.e. 50% duty cycle)
        # on_period = (full_period << 2) / 2;
        # this is quicker
        on_period = full_period << 1
        self.pwm_on(T2_PS_1_16, full_period, on_period)

    def pwm_off(self):
        """Turns off the PWM generator."""
        go_busy_off_mask = 0xff ^ (1 << 4)
        self.and_mask(CHANNEL_INDEX_PWM_CONF_2, go_busy_off_mask)

    def servo_set(self, servo_index, pulse_length):
        """Set the servo at servo_index to pulse_length. Make sure that
        the leg is configured as IO_DIGITAL_OUTPUT (0).
        """
        pulse_length_msb = 0xff & (pulse_length >> 8)
        pulse_length_lsb = 0xff & pulse_length
        conf_msb = ((servo_index & 0xf) << 4) | 0x01
        conf_lsb = ((servo_index & 0xf) << 4) | 0x00
        self.set_bulk(CHANNEL_INDEX_SERVO_PULSE_LENGTH,
                      bytes([pulse_length_msb, conf_msb]))
        self.set_bulk(CHANNEL_INDEX_SERVO_PULSE_LENGTH,
                      bytes([pulse_length_lsb, conf_lsb]))

    def clear(self):
        """Clears the pixels on CodeBug.

            >>> codebug = CodeBug()
            >>> codebug.clear()

        """
        self.set_bulk(0, bytes([0]*5))

    def fill(self):
        """Sets all pixels on.

            >>> codebug = CodeBug()
            >>> codebug.fill()

        """
        self.set_bulk(0, bytes([0x1f]*5))

    def set_row(self, row, val):
        """Sets a row of PIXELs on CodeBug.

            >>> codebug = CodeBug()
            >>> codebug.set_row(0, 0b10101)

        """
        self.set(row, val)

    def get_row(self, row):
        """Returns a row of pixels on CodeBug.

            >>> codebug = CodeBug()
            >>> codebug.get_row(0)
            21

        """
        row = self.get(min(row, 5))  # only row channels
        return struct.unpack('B', row)[0]

    def set_col(self, col, val):
        """Sets an entire column of PIXELs on CodeBug.

            >>> codebug = CodeBug()
            >>> codebug.set_col(0, 0b10101)

        """
        rows = struct.unpack('B'*5, self.get_bulk(0, 5))
        # clear col
        rows = [rows[i] & (0xff ^ (1 << (4-col))) for i in range(5)]
        # set cols
        val_bits = [(val >> i) & 1 for i in reversed(range(5))]
        rows = [rows[i] | (bit << (4-col)) for i, bit in enumerate(val_bits)]
        self.set_bulk(0, bytes(rows))

    def get_col(self, col):
        """Returns an entire column of PIXELs on CodeBug.

            >>> codebug = CodeBug()
            >>> codebug.get_col(0)
            21

        """
        rows = struct.unpack('B'*5, self.get_bulk(0, 5))
        c = 0
        for row in rows:
            c <<= 1
            col_bit = 1 & (row >> (4 - col))
            c |= col_bit
        return c

    def set_pixel(self, x, y, state):
        """Sets an PIXEL on CodeBug.

            >>> codebug = CodeBug()
            >>> codebug.set_pixel(0, 0, 1)

        """
        channel = min(y, 5)  # only row channels
        bit_index = 4 - x
        self.set_bit(channel, bit_index, state)

    def get_pixel(self, x, y):
        """Returns the state of an PIXEL on CodeBug.

            >>> codebug = CodeBug()
            >>> codebug.get_pixel(0, 0)
            1

        """
        channel = min(y, 5)
        bit_index = 4 - x
        return self.get_bit(channel, bit_index)

    def draw_sprite(self, x, y, sprite, clear_first=True):
        """Draws a sprite at (x, y) on CodeBug's 5x5 display."""
        cb_display_sprite = sprite.get_sprite(-x, -y, 5, 5)
        cb_rows = [cb_display_sprite.get_row(y)
                   for y in range(cb_display_sprite.height)]
        if clear_first:
            self.set_bulk(0, bytes(cb_rows))
        else:
            for i, row in enumerate(cb_rows):
                self.or_mask(i, bytes(row))