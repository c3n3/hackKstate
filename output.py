# @see https://pimylifeup.com/i-lcd-16x2/

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

class output():
    def __init__(self):
        self.lcd_rs        = digitalio.DigitalInOut(board.D26)
        self.lcd_en        = digitalio.DigitalInOut(board.D19)
        self.lcd_d7        = digitalio.DigitalInOut(board.D27)
        self.lcd_d6        = digitalio.DigitalInOut(board.D22)
        self.lcd_d5        = digitalio.DigitalInOut(board.D24)
        self.lcd_d4        = digitalio.DigitalInOut(board.D25)
        self.lcd_columns = 16
        self.lcd_rows = 2
        self.lcd = characterlcd.Character_LCD_Mono(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7, self.lcd_columns, self.lcd_rows)
        #self.lcd.message = "Hello"
    def showAnswer(self, string):
        self.lcd.cursor_position(16 - len(string), 1)
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
        self.lcd.cursor_position(x,y)

    def clear(self):
        self.lcd.clear()

    def resetCursor(self):
        self.lcd.home()

    def add(self,string):
        self.lcd.message += string
