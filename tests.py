import time
import unittest
import codebug_i2c_tether


I2C_BUS = 1
I2C_ADDRESS = 0x18


class TestCodeBugI2CTether(unittest.TestCase):

    # def test_set_pixel(self):
    #     with codebug_i2c_tether.CodeBug() as codebug:
    #         for y in range(5):
    #             for x in range(5):
    #                 print(x, y)
    #                 codebug.set_pixel(x, y, 1)
    #                 time.sleep(1)
    #                 codebug.set_pixel(x, y, 0)

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
            # for y in range(5):
            #     self.assertEqual(codebug.get_row(y), 0x1f)

    # def test_get_set_col(self):
    #     with codebug_i2c_tether.CodeBug() as codebug:
    #         codebug.clear()
    #         for x in range(5):
    #             codebug.set_col(x, 0x1f)
    #         for x in range(5):
    #             self.assertEqual(codebug.get_col(x), 0x1f)


if __name__ == "__main__":
    unittest.main()
