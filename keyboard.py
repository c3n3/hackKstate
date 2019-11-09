import RPi.GPIO as GPIO
import time


class keyboard():
    def __init__(self):
        self.row = [17,27,22]
        self.col = [33,35,37]
    def rowOut(self):
        for id in self.row:
            GPIO.setup(id, GPIO.OUT)
            GPIO.output(id, True)
        for id in self.col:
            GPIO.setup(id, GPIO.IN)
    def colOut(self):
        for id in self.col:
            GPIO.setup(id, GPIO.OUT)
            GPIO.output(id, True)
        for id in self.row:
            GPIO.setup(id, GPIO.IN)
    def readRow(self):
        rowin = []
        for index, id in enumerate(self.row):
            print(GPIO.input(id))
            time.sleep(1)
            if GPIO.input(id):
                rowin.append(index)
        if len(rowin) > 1:
            return "fuck off"
        if len(rowin) < 1:
            return "cunt"
        else:
            return rowin[0]
    def readCol(self):
        colin = []
        for index, id in enumerate(self.col):
            print(GPIO.input(id))
            time.sleep(1)
            if GPIO.input(id):
                colin.append(index)
        if len(colin) > 1:
            return "fuck off"
        if len(colin) < 1:
            return "cunt"
        else: 
            return colin[0]
    def readButton(self):
        GPIO.setmode(GPIO.BCM)
        self.rowOut()
        c = self.readCol()
        self.colOut()
        r = self.readRow()
        return [r,c]

print(keyboard().readButton())