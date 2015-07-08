import time
import codebug_i2c_tether


if __name__ == '__main__':
    with codebug_i2c_tether.CodeBug() as codebug:
        codebug.set_row(4, 0x15)
        codebug.set_row(3, 0x0a)
        codebug.set_row(2, 0x15)
        codebug.set_row(1, 0x0a)
        codebug.set_row(0, 0x15)
        time.sleep(1)
        codebug.set_row(4, 0x0a)
        codebug.set_row(3, 0x15)
        codebug.set_row(2, 0x0a)
        codebug.set_row(1, 0x15)
        codebug.set_row(0, 0x0a)
        time.sleep(1)
        codebug.clear()
