from utility import utility
from newKeyboard import buttons


class controller():

    def __init__(self):

        self.executable = ""
        self.display = ""
        self.tempdisplay = ""
        self.menu = 'Main'      #Main,2nd,Alpha,Math
        self.func = 'None'      #None,defInt,defDer,Sum,decToFrac
        self.selectedline = 0
        self.cursor = 0 #index of window

        self.util = utility
        self.buttons = buttons()
        self.buttons.setHandler(self.processButtonPress())


    def processButtonPress(self):


        if (keyPressed == "2nd"):
            if (self.menu == '2nd'):
                self.menu = 'Main'
            else:
                self.menu == '2nd'

        elif (keyPressed == "Alpha"):
            if (self.menu == 'Alpha'):
                self.menu = 'Main'
            else:
                self.menu = 'Alpha'

        elif (keyPressed == "Math"):
            if (self.menu == 'Math'):
                self.menu = 'Main'
            else:
                self.menu = 'Math'


        #add cursor junk
        elif (keyPressed == "RIGHT"):
            pass
        elif (keyPressed == "LEFT"):
            pass

        elif (keyPressed == "UP"):
            self.selectedline = (self.selectedline + 1) % 4
        elif (keyPressed == "DOWN"):
            self.selectedline = (self.selectedline - 1) % 4


        elif (keyPressed == "ENTER"):
            if (self.func == 'None'):
                self.display = self.util.executeStringFunction(self.executable)
            else:
                entered += 1


        elif (self.menu == 'Main' or self.menu == '2nd'):
            if (self.func = 'None'):
                self.executable += keyPressed
                self.display += keyPressed
            else:
                input += keyPressed

        if (self.menu == 'Math' and self.func == 'None'):
            self.tempdisplay = self.display

            if (self.selectedline == 0):
                self.display = "1: defIntegral"
            elif (self.selectedline == 1):
                self.display = "2: defDerivative"
            elif (self.selectedline == 2):
                self.display = "3: Summation"
            elif (self.selectedline == 3):
                self.display = "4: decToFrac"


            if (keyPressed == "1"):
                self.menu = 'Main'
                self.func = 'defInt'
            elif (keyPressed == "2"):
                self.menu = 'Main'
                self.func = 'defDer'
            elif (keyPressed == "3"):
                self.menu = 'Main'
                self.func = 'Sum'
            elif (keyPressed == "4"):
                self.menu = 'Main'
                self.func = 'decToFrac'

            input = ""
            entered = 0
            argument = 0
            f = ["","",""]

        if (self.func == 'defInt'):
            if (arguments == 0):
                self.display = "Function: " + input
            elif (arguments == 1):
                self.display = "Lower Bound: " + input
            elif (arguments == 2):
                self.display = "Upper Bound: " + input

            if (entered > arguments and entered < 4):
                f[arguments] = input
                input = ""
                arguments += 1
            elif (entered > 3):
                value = str(self.util.defIntegrate(self.util.convertStringToFunction(f[0][1:]),float(f[1]),float(f[2])))
                self.executable += value
                self.display = self.tempdisplay + value
                self.func = 0
                self.selectedline = 0

        elif (self.func == 'defDer'):
            if (arguments == 0):
                self.display = "Function: " + input
            elif (arguments == 1):
                self.display = "Evaluate at: " + input

            if (entered > arguments and entered < 3):
                f[arguments] = input
                input = ""
                arguments += 1
            elif (entered > 2):
                value = str(self.util.defDerivative(self.util.convertStringToFunction(f[0][1:]),float(f[1])))
                self.executable += value
                self.display = self.tempdisplay + value
                self.func = 0
                self.selectedline = 0

        elif (self.func == 'Sum'):
            if (arguments == 0):
                self.display = "Function: " + input
            elif (arguments == 1):
                self.display = "Lower Bound: " + input
            elif (arguments == 2):
                self.display = "Upper Bound: " + input

            if (entered > arguments and entered < 4):
                f[arguments] = input
                input = ""
                arguments += 1
            elif (entered > 3):
                value = str(self.util.summation(self.util.convertStringToFunction(f[0][1:]),float(f[1]),float(f[2])))
                self.executable += value
                self.display = self.tempdisplay + value
                self.func = 0
                self.selectedline = 0

        elif (self.func == 'decToFrac'):
            if (arguments == 0):
                self.display = "Decimal: " + input

            if (entered > arguments and entered < 2):
                f[arguments] = input
                input = ""
                arguments += 1
            elif (entered > 3):
                value = self.util.decToFraction(self.util.executeStringFunction(f[0][1:]))
                self.display = value
                self.func = 0
                self.selectedline = 0





controller = controller()
while(True):
    sleep(.1)
