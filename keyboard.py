import RPi.GPIO as GPIO
import time

row = [17,27,22]
col = [2,3,4]


class keyboard():
    def __init__(self):
        self.row = [17,27,22]
        self.col = [2,3,4]
    def rowOut(self):
        for id in row:
            GPIO.setup(id, GPIO.OUT)
            GPIO.output(id, True)
        for id in col:
            GPIO.setup(id, GPIO.IN)
    def colOut(self):
        for id in col:
            GPIO.setup(id, GPIO.OUT)
            GPIO.output(id, True)
        for id in row:
            GPIO.setup(id, GPIO.IN)
    def readRow(self):
        rowin = []
        for index, id in enumerate(self.row):
            if (GPIO.input(id))
                rowin.append(index)
        if len(rowin) > 1:
            return "fuck off"
        else return rowin[0]
    def readCol(self):
        colin = []
        for index, id in enumerate(self.col):
            if (GPIO.input(id))
                rowin.append(index)
        if len(colin) > 1:
            return "fuck off"
        else return colin[0]
    def readButton(self):
        self.rowOut()
        c = self.readCol()
        self.colOut()
        r = self.readRow()
        return [r,c]

print(keyboard().readButton())