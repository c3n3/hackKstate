
import RPi.GPIO as GPIO
import Keypad



class testKeyBoard():


    def __init__(self):
        self.ROWS = 3
        self.COLS = 3
        self.keys = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
        ]
        self.rowPins = [17, 27, 22]
        self.colPins = [33, 35, 37]
        self.keypad = Keypad.Keypad(self.keys, rowPins, colPins, ROWS, COLS)
        self.keypad.setDebounceTime(50)

    def read():
        key = self.keypad.getKey()
        if (key != keypad.NULL):
            print(key)

k = testKeyBoard():
while (True):
    k.read()
