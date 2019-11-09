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
KEYPAD = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
]

ROW_PINS = [17,27,22] # BCM numbering
COL_PINS = [33,35,37] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def printKey(key):
        print(key)

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

while (True):
    time.sleep(0.1)
