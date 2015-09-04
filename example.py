import time
import codebug_i2c_tether


if __name__ == '__main__':
    with codebug_i2c_tether.CodeBug() as codebug:
        codebug.set_row(4, 0b11100)
        codebug.set_row(3, 0b11000)
        codebug.set_row(2, 0b10100)
        codebug.set_row(1, 0b00010)
        codebug.set_row(0, 0b00001)
