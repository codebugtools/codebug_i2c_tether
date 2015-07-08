# Converted from /usr/include/linux/i2c.h and /usr/include/linux/i2c-dev.h
import ctypes

#-----------------------------------------------------------------------
# /usr/include/linux/i2c.h


class i2c_msg(ctypes.Structure):
    """struct i2c_msg - an I2C transaction segment beginning with START

    @addr: Slave address, either seven or ten bits.  When this is a ten
        bit address, I2C_M_TEN must be set in @flags and the adapter
        must support I2C_FUNC_10BIT_ADDR.
    @flags: I2C_M_RD is handled by all adapters.  No other flags may be
        provided unless the adapter exported the relevant I2C_FUNC_*
        flags through i2c_check_functionality().
    @len: Number of data bytes in @buf being read from or written to the
        I2C slave address.  For read transactions where I2C_M_RECV_LEN
        is set, the caller guarantees that this buffer can hold up to
        32 bytes in addition to the initial length byte sent by the
        slave (plus, if used, the SMBus PEC); and this value will be
        incremented by the number of block data bytes received.
    @buf: The buffer into which data is read, or from which it's written.
        An i2c_msg is the low level representation of one segment of an I2C
        transaction.  It is visible to drivers in the @i2c_transfer()
        procedure, to userspace from i2c-dev, and to I2C adapter drivers
        through the @i2c_adapter.@master_xfer() method.
        Except when I2C "protocol mangling" is used, all I2C adapters
        implement the standard rules for I2C transactions.  Each transaction
        begins with a START.  That is followed by the slave address, and a
        bit encoding read versus write.  Then follow all the data bytes,
        possibly including a byte with SMBus PEC.  The transfer terminates
        with a NAK, or when all those bytes have been transferred and ACKed.
        If this is the last message in a group, it is followed by a STOP.
        Otherwise it is followed by the next @i2c_msg transaction segment,
        beginning with a (repeated) START. Alternatively, when the adapter
        supports I2C_FUNC_PROTOCOL_MANGLING then passing certain @flags may
        have changed those standard protocol behaviors. Those flags are only
        for use with broken/nonconforming slaves, and with adapters which
        are known to support the specific mangling options they need (one
        or more of IGNORE_NAK, NO_RD_ACK, NOSTART, and REV_DIR_ADDR).
    """
    _fields_ = [('addr', ctypes.c_uint16),
                ('flags', ctypes.c_ushort),
                ('len', ctypes.c_short),
                ('buf', ctypes.POINTER(ctypes.c_char))]

    __slots__ = [name for name, type in _fields_]


# i2c_msg flags
I2C_M_TEN = 0x0010  # this is a ten bit chip address
I2C_M_RD = 0x0001  # read data, from slave to master
I2C_M_NOSTART = 0x4000  # if I2C_FUNC_PROTOCOL_MANGLING
I2C_M_REV_DIR_ADDR = 0x2000  # if I2C_FUNC_PROTOCOL_MANGLING
I2C_M_IGNORE_NAK = 0x1000  # if I2C_FUNC_PROTOCOL_MANGLING
I2C_M_NO_RD_ACK = 0x0800  # if I2C_FUNC_PROTOCOL_MANGLING
I2C_M_RECV_LEN = 0x0400  # length will be first received byte


# To determine what functionality is present
I2C_FUNC_I2C = 0x00000001
I2C_FUNC_10BIT_ADDR = 0x00000002
I2C_FUNC_PROTOCOL_MANGLING = 0x00000004  # I2C_M_NOSTART etc.
I2C_FUNC_SMBUS_PEC = 0x00000008
I2C_FUNC_SMBUS_BLOCK_PROC_CALL = 0x00008000  # SMBus 2.0
I2C_FUNC_SMBUS_QUICK = 0x00010000
I2C_FUNC_SMBUS_READ_BYTE = 0x00020000
I2C_FUNC_SMBUS_WRITE_BYTE = 0x00040000
I2C_FUNC_SMBUS_READ_BYTE_DATA = 0x00080000
I2C_FUNC_SMBUS_WRITE_BYTE_DATA = 0x00100000
I2C_FUNC_SMBUS_READ_WORD_DATA = 0x00200000
I2C_FUNC_SMBUS_WRITE_WORD_DATA = 0x00400000
I2C_FUNC_SMBUS_PROC_CALL = 0x00800000
I2C_FUNC_SMBUS_READ_BLOCK_DATA = 0x01000000
I2C_FUNC_SMBUS_WRITE_BLOCK_DATA = 0x02000000
I2C_FUNC_SMBUS_READ_I2C_BLOCK = 0x04000000  # I2C-like block xfer
I2C_FUNC_SMBUS_WRITE_I2C_BLOCK = 0x08000000  # w/ 1-byte reg. addr.

I2C_FUNC_SMBUS_BYTE = (I2C_FUNC_SMBUS_READ_BYTE |
                       I2C_FUNC_SMBUS_WRITE_BYTE)
I2C_FUNC_SMBUS_BYTE_DATA = (I2C_FUNC_SMBUS_READ_BYTE_DATA |
                            I2C_FUNC_SMBUS_WRITE_BYTE_DATA)
I2C_FUNC_SMBUS_WORD_DATA = (I2C_FUNC_SMBUS_READ_WORD_DATA |
                            I2C_FUNC_SMBUS_WRITE_WORD_DATA)
I2C_FUNC_SMBUS_BLOCK_DATA = (I2C_FUNC_SMBUS_READ_BLOCK_DATA |
                             I2C_FUNC_SMBUS_WRITE_BLOCK_DATA)
I2C_FUNC_SMBUS_I2C_BLOCK = (I2C_FUNC_SMBUS_READ_I2C_BLOCK |
                            I2C_FUNC_SMBUS_WRITE_I2C_BLOCK)

I2C_FUNC_SMBUS_EMUL = (I2C_FUNC_SMBUS_QUICK |
                       I2C_FUNC_SMBUS_BYTE |
                       I2C_FUNC_SMBUS_BYTE_DATA |
                       I2C_FUNC_SMBUS_WORD_DATA |
                       I2C_FUNC_SMBUS_PROC_CALL |
                       I2C_FUNC_SMBUS_WRITE_BLOCK_DATA |
                       I2C_FUNC_SMBUS_I2C_BLOCK |
                       I2C_FUNC_SMBUS_PEC)

# Data for SMBus Messages
I2C_SMBUS_BLOCK_MAX = 32  # As specified in SMBus standard


class i2c_smbus_data(ctypes.Union):
    """block[0] is used for length and one more for user-space compatibility"""
    _fields_ = [('byte', ctypes.c_uint8),
                ('word', ctypes.c_uint16),
                ('block', ctypes.c_uint8 * (I2C_SMBUS_BLOCK_MAX + 2))]

    __slots__ = [name for name, type in _fields_]


# i2c_smbus_xfer read or write markers
I2C_SMBUS_READ = 1
I2C_SMBUS_WRITE = 0

# SMBus transaction types (size parameter in the above functions)
# Note: these no longer correspond to the (arbitrary) PIIX4 internal codes!
I2C_SMBUS_QUICK = 0
I2C_SMBUS_BYTE = 1
I2C_SMBUS_BYTE_DATA = 2
I2C_SMBUS_WORD_DATA = 3
I2C_SMBUS_PROC_CALL = 4
I2C_SMBUS_BLOCK_DATA = 5
I2C_SMBUS_I2C_BLOCK_BROKEN = 6
I2C_SMBUS_BLOCK_PROC_CALL = 7  # SMBus 2.0
I2C_SMBUS_I2C_BLOCK_DATA = 8

#-----------------------------------------------------------------------
# /usr/include/linux/i2c.h

# /dev/i2c-X ioctl commands.  The ioctl's parameter is always an
# unsigned long, except for:
#  - I2C_FUNCS, takes pointer to an unsigned long
#  - I2C_RDWR, takes pointer to struct i2c_rdwr_ioctl_data
#  - I2C_SMBUS, takes pointer to struct i2c_smbus_ioctl_data

# number of times a device address should be polled when not acknowledging
I2C_RETRIES = 0x0701
I2C_TIMEOUT = 0x0702  # set timeout in units of 10 ms

# NOTE: Slave address is 7 or 10 bits, but 10-bit addresses are NOT supported!
#       (due to code brokenness)
I2C_SLAVE = 0x0703  # Use this slave address
# Use this slave address, even if it is already in use by a driver!
I2C_SLAVE_FORCE = 0x0706
I2C_TENBIT = 0x0704  # 0 for 7 bit addrs, != 0 for 10 bit

I2C_FUNCS = 0x0705  # Get the adapter functionality mask

I2C_RDWR = 0x0707  # Combined R/W transfer (one STOP only)

I2C_PEC = 0x0708  # != 0 to use PEC with SMBus
I2C_SMBUS = 0x0720  # SMBus transfer


# This is the structure as used in the I2C_SMBUS ioctl call
class i2c_smbus_ioctl_data(ctypes.Structure):
    _fields_ = [
        ('read_write', ctypes.c_uint8),
        ('command', ctypes.c_uint8),
        ('size', ctypes.c_uint32),
        ('i2c_smbus_data', ctypes.POINTER(i2c_smbus_data))]

    __slots__ = [name for name, type in _fields_]


# This is the structure as used in the I2C_RDWR ioctl call
class i2c_rdwr_ioctl_data(ctypes.Structure):
    """<linux/i2c-dev.h> struct i2c_rdwr_ioctl_data"""
    _fields_ = [
        ('msgs', ctypes.POINTER(i2c_msg)),
        ('nmsgs', ctypes.c_int)]

    __slots__ = [name for name, type in _fields_]


I2C_RDRW_IOCTL_MAX_MSGS = 42
