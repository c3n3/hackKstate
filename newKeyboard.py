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
import output

class buttons():
    def __init__(self):
        self.keys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','UP'],
                ['^','sin(','cos(','tan(','/'],
                ['LOG(','7','8','9','*'],
                ['LN(','4','5','6','-'],
                ['=','1','2','3','+'],
                ['DELETE','.','0',' ','ENTER'],
        ]
        self.ROW_PINS = [4,17,10,22,5,9,13] # BCM numbering
        self.COL_PINS = [18,11,24,16,12] # BCM numbering

        self.factory = rpi_gpio.KeypadFactory()

        self.keypad = self.factory.create_keypad(keypad=self.keys, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)

        self.mainkeys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','UP'],
                ['^','sin(','cos(','tan(','/'],
                ['LOG(', '7',  '8', '9',  '*'],
                ['LN(', '4' ,' 5',  '6' , '-'],
                ['=',  '1',  '2',  '3',   '+'],
                ['DELETE','.','0',' ','ENTER']]
        self.secondkeys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','UP'],
                ['pi','asin(','acos(','atan(','/'],
                ['10^(', '7',  '8', '9',  '*'],
                ['e^(', '4' ,' 5',  '6' , '-'],
                ['=',  '1',  '2',  '3',   '+'],
                ['DELETE','.','0',' ','ENTER']]
        self.alphakeys = [
                ['2nd','X','Math','LEFT','UP'],
                ['Alpha','(' ,')','DOWN','UP'],
                ['A',  'B',  'C',  'D'  , '/'],
                ['E',  'F',  'G',  'H'  , '*'],
                ['I',  'J',  'K',  'L'  , '-'],
                ['=',  'M',  'N',  'O'  , '+'],
                ['DELETE','P','Q',' ','ENTER']]
    def setHandler(self, function):
        self.keypad.registerKeyPressHandler(function)

    def setKeys(self, newKeys):
        self.keys = newKeys
        self.keypad = self.factory.create_keypad(keypad=self.keys, row_pins=self.ROW_PINS, col_pins=self.COL_PINS)

Lcd = output()
things = buttons()
def out(thing):
    Lcd.showMessage(thing)

things.setHandler(out)

while True:
    time.sleep(.1)
