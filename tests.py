import time
import unittest
import codebug_i2c_tether


I2C_BUS = 1
I2C_ADDRESS = 0x18


class TestCodeBugI2CTether(unittest.TestCase):

    def test_set_pixel(self):
        with codebug_i2c_tether.CodeBug() as codebug:
            codebug.clear()
            for y in range(5):
                for x in range(5):
                    codebug.set_pixel(x, y, 1)
                self.assertEqual(codebug.get_row(y), 0x1f)
            for y in range(5):
                for x in range(0, 5, 2):
                    codebug.set_pixel(x, y, 1)
                for x in range(1, 5, 2):
                    codebug.set_pixel(x, y, 0)
                self.assertEqual(codebug.get_row(y), 0x15)
            for y in range(5):
                for x in range(0, 5, 2):
                    codebug.set_pixel(x, y, 0)
                for x in range(1, 5, 2):
                    codebug.set_pixel(x, y, 1)
                self.assertEqual(codebug.get_row(y), 0x0A)

    def test_get_pixel(self):
        with codebug_i2c_tether.CodeBug() as codebug:
            codebug.clear()
            for y in range(5):
                for x in range(5):
                    codebug.set_pixel(x, y, 1)
            for y in range(5):
                for x in range(5):
                    self.assertEqual(codebug.get_pixel(x, y), 1)

    def test_get_set_row(self):
        with codebug_i2c_tether.CodeBug() as codebug:
            codebug.clear()
            for i in range(5):
                for y in range(5):
                    codebug.set_row(y, 0x1f)
                for y in range(5):
                    codebug.set_row(y, 0x15)
                for y in range(5):
                    codebug.set_row(y, 0x0A)
            for y in range(5):
                self.assertEqual(codebug.get_row(y), 0x0a)

    def test_get_set_col(self):
        with codebug_i2c_tether.CodeBug() as codebug:
            codebug.clear()
            for x in range(5):
                codebug.set_col(x, 0x1f)
            for x in range(5):
                self.assertEqual(codebug.get_col(x), 0x1f)
            for x in range(5):
                codebug.set_col(x, 0x15)
            for x in range(5):
                self.assertEqual(codebug.get_col(x), 0x15)
            for x in range(5):
                codebug.set_col(x, 0)
            for x in range(5):
                self.assertEqual(codebug.get_col(x), 0)

    def test_write_text(self):
        with codebug_i2c_tether.CodeBug() as codebug:
            message = 'Hello, CodeBug!'
            for i in range(len(message) * 6):
                time.sleep(0.05)
                codebug.write_text(-i, 0, message)


if __name__ == "__main__":
    unittest.main()
