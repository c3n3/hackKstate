# @see https://pimylifeup.com/i-lcd-16x2/

import Adafruit_CharLCD as LCD

class output():
    def __init__(self):
        self.lcd_rs        = 25
        self.lcd_en        = 24
        self.lcd_d4        = 23
        self.lcd_d5        = 17
        self.lcd_d6        = 18
        self.lcd_d7        = 22
        self.lcd_backlight = 4
        self.lcd_columns = 16
        self.lcd_rows = 2
        self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

    def showAnswer(self, string):
        self.lcd.set_cursor(16 - len(string), 1)
        self.lcd.message = string

    def showMessage(self, string):
        self.lcd.message = string

    # def addChar(self):
    #     self.lcd.message()

    def moveLeft(self):
        self.lcd.move_left()

    def moveRight(self):
        self.lcd.move_right()

    def set_cursor(self, x, y):
        self.lcd.set_cursor(x, y)

    def clear(self):
        self.lcd.clear()

    def resetCursor(self):
        self.lcd.home()
