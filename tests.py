import time
import struct
import unittest
import codebug_i2c_tether
from codebug_tether.sprites import (Sprite, StringSprite)


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

    def test_draw_sprite(self):
        with codebug_i2c_tether.CodeBug() as codebug:
            codebug.clear()

            def fill_sprite(s):
                for x in range(s.width):
                    for y in range(s.height):
                        s.set_pixel(x, y, 1)

            sprite = Sprite(4, 4)
            fill_sprite(sprite)

            codebug.draw_sprite(0, 0, sprite)
            self.assertEqual(codebug.get_row(4), 0x00)
            self.assertEqual(codebug.get_row(3), 0x1E)
            self.assertEqual(codebug.get_row(2), 0x1E)
            self.assertEqual(codebug.get_row(1), 0x1E)
            self.assertEqual(codebug.get_row(0), 0x1E)

            codebug.draw_sprite(1, 1, sprite)
            self.assertEqual(codebug.get_row(4), 0x0F)
            self.assertEqual(codebug.get_row(3), 0x0F)
            self.assertEqual(codebug.get_row(2), 0x0F)
            self.assertEqual(codebug.get_row(1), 0x0F)
            self.assertEqual(codebug.get_row(0), 0x00)

            sprite = Sprite(2, 3)
            fill_sprite(sprite)
            codebug.draw_sprite(0, 0, sprite)
            self.assertEqual(codebug.get_row(4), 0x00)
            self.assertEqual(codebug.get_row(3), 0x00)
            self.assertEqual(codebug.get_row(2), 0x18)
            self.assertEqual(codebug.get_row(1), 0x18)
            self.assertEqual(codebug.get_row(0), 0x18)

            sprite = Sprite(3, 3)
            fill_sprite(sprite)
            sprite.set_pixel(1, 2, 0) # key the sprite

            codebug.draw_sprite(0, 0, sprite)
            self.assertEqual(codebug.get_row(4), 0x00)
            self.assertEqual(codebug.get_row(3), 0x00)
            self.assertEqual(codebug.get_row(2), 0x14)
            self.assertEqual(codebug.get_row(1), 0x1C)
            self.assertEqual(codebug.get_row(0), 0x1C)

            codebug.draw_sprite(2, 2, sprite)
            self.assertEqual(codebug.get_row(4), 0x05)
            self.assertEqual(codebug.get_row(3), 0x07)
            self.assertEqual(codebug.get_row(2), 0x07)
            self.assertEqual(codebug.get_row(1), 0x00)
            self.assertEqual(codebug.get_row(0), 0x00)

            hello_str = StringSprite('Hello!')
            codebug.draw_sprite(0, 0, hello_str)
            self.assertEqual(codebug.get_row(4), 0x12)
            self.assertEqual(codebug.get_row(3), 0x12)
            self.assertEqual(codebug.get_row(2), 0x1E)
            self.assertEqual(codebug.get_row(1), 0x12)
            self.assertEqual(codebug.get_row(0), 0x12)
            codebug.draw_sprite(-7, 0, hello_str)
            self.assertEqual(codebug.get_row(4), 0x03)
            self.assertEqual(codebug.get_row(3), 0x11)
            self.assertEqual(codebug.get_row(2), 0x19)
            self.assertEqual(codebug.get_row(1), 0x01)
            self.assertEqual(codebug.get_row(0), 0x1B)


if __name__ == "__main__":
    unittest.main()
