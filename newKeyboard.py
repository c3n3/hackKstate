#
# import RPi.GPIO as GPIO
# import keypad
#
#
#
# class testKeyBoard():
#
#
#     def __init__(self):
#         cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D6, board.D5)]
#         rows = [digitalio.DigitalInOut(x) for x in (board.D13, board.D12, board.D11, board.D10)]
#         keys = ((1, 2, 3),
#         (4, 5, 6),
#         (7, 8, 9),
#         ('*', 0, '#'))
#         self.ROWS = 3
#         self.COLS = 3
#         self.keys = [
#             '1', '2', '3',
#             '4', '5', '6',
#             '7', '8', '9',
#         ]
#         self.rowPins = [17, 27, 22]
#         self.colPins = [33, 35, 37]
#         self.keypad = Keypad.Keypad(self.keys, rowPins, colPins, ROWS, COLS)
#         self.keypad.setDebounceTime(50)
#
#     def read():
#         key = self.keypad.getKey()
#         if (key != keypad.NULL):
#             print(key)
#
# k = testKeyBoard()
# while (True):
#     k.read()


from pad4pi import rpi_gpio
import time
from lcdInterface import lcdInterface

class buttons():
    def __init__(self):
        self.keys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','RIGHT'],
                ['^','sin(','cos(','tan(','/'],
                ['log(','7','8','9','*'],
                ['ln(','4','5','6','-'],
                ['=','1','2','3','+'],
                ['DELETE','.','0',',','ENTER'],
        ]
        self.ROW_PINS = [4,17,26,5,6,21,13] # BCM numbering
        self.COL_PINS = [18,20,23,16,12] # BCM numbering

        self.factory = rpi_gpio.KeypadFactory()

        self.keypad = self.factory.create_keypad(keypad=self.keys, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)

        self.mainkeys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','RIGHT'],
                ['^','sin(','cos(','tan(','/'],
                ['log(', '7',  '8', '9',  '*'],
                ['ln(', '4' ,' 5',  '6' , '-'],
                ['=',  '1',  '2',  '3',   '+'],
                ['DELETE','.','0',',','ENTER']]
        self.secondkeys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','RIGHT'],
                ['pi','asin(','acos(','atan(','/'],
                ['10^(', '7',  '8', '9',  '*'],
                ['e^(', '4' ,' 5',  '6' , '-'],
                ['=',  '1',  '2',  '3',   '+'],
                ['DELETE','.','0',' ','ENTER']]
        self.alphakeys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','RIGHT'],
                ['A',  'B',  'C',  'D'  , '/'],
                ['E',  'F',  'G',  'H'  , '*'],
                ['I',  'J',  'Z',  'L'  , '-'],
                ['=',  'M',  'N',  'O'  , '+'],
                ['DELETE','P','Q',' ','ENTER']]
    def setHandler(self, function):
        self.keypad.registerKeyPressHandler(function)

    #def setKeys(self, newKeys):
     #   self.keypad =  newKeys
    def mapKey(self, state, key):
        temp = self.alphakeys if state == "alpha" else self.secondkeys
        for i, keys in enumerate(self.mainkeys):
            for index, k in enumerate(keys):
                if (key == k):
                    return temp[i][index]
"""
Lcd = lcdInterface()
things = buttons()
Lcd.setFirstLine("Hello this is cool")
def out(thing):
    print(thing)
    Lcd.setFirstLine(thing)
    Lcd.toString()

things.setHandler(out)

while True:
    time.sleep(.1)"""
