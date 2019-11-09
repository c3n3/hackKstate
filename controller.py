from utility import utility
from newKeyboard import buttons
from output import output


class controller():

    def __init__(self):

        self.executable = ""
        self.display = ""
        self.tempdisplay = ""
        self.menu = 'Main'      #Main,2nd,Alpha,Math
        self.func = 'None'      #None,defInt,defDer,Sum,decToFrac
        self.selectedline = 0
        self.cursor = 0 #index of cursor
        self.window = [0,15]

        self.util = utility()
        self.buttons = buttons()
        self.buttons.setHandler(self.processButtonPress())
        self.output = output()


    def processButtonPress(self, keyPressed):


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
        elif (keyPressed == "RIGHT" and self.cursor < len(self.display)):
            self.output.moveRight()
            self.cursor += 1
        elif (keyPressed == "LEFT" and self.cursor > 0):
            self.output.moveLeft()
            self.cursor -= 1

        elif (keyPressed == "UP"):
            self.selectedline = (self.selectedline + 1) % 4
        elif (keyPressed == "DOWN"):
            self.selectedline = (self.selectedline - 1) % 4


        elif (keyPressed == "ENTER"):
            if (self.func == 'None'):
                self.display = self.util.executeStringFunction(self.executable)
                self.executable = 0
            else:
                entered = True

        elif (keyPressed == "DELETE"):
            if (self.func == 'None'):
                self.executable = self.executable[:self.cursor] + self.executable[self.cursor+1:]
                self.display = self.display[:self.cursor] + self.display[self.cursor+1:]
            else:
                input = input[:self.cursor] + input[self.cursor+1:]

        elif (self.menu == 'Main' or self.menu == '2nd'):
            if (self.func = 'None'):
                self.executable = self.executable[:self.cursor] + keyPressed + self.executable[self.cursor:]
                self.display = self.display[:self.cursor] + keyPressed + self.display[self.cursor:]
            else:
                if (keyPressed == "X"):
                    keyPressed = 'x'
                #input = input[:self.cursor] + keyPressed + input[self.cursor:]
                self.display = self.display[:self.cursor] + keyPressed + self.display[self.cursor:]


        if (self.cursor < self.window[0]):
            self.window[0] -= 1
            self.window[1] -= 1

        elif (self.cursor > self.window[1]):
            self.window[0] += 1
            self.window[1] += 1


        if (self.menu == 'Math' and self.func == 'None'):
            self.tempdisplay = self.display
            self.selectedline = 0

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
                self.display = "defInt("
            elif (keyPressed == "2"):
                self.menu = 'Main'
                self.func = 'defDer'
                self.display = "defDer("
            elif (keyPressed == "3"):
                self.menu = 'Main'
                self.func = 'Sum'
                self.display = "Sum("
            elif (keyPressed == "4"):
                self.menu = 'Main'
                self.func = 'decToFrac'
                self.display = "decToFrac("

            self.cursor = len(self.display)
            #output.set_cursor(self.cursor,0)

            # input = ""
            # entered = 0
            # argument = 0
            # f = ["","",""]
            entered = False

        if (self.func == 'defInt'):
            if (entered):
                self.display.replace("defInt(",'')
                self.display.replace(')','')
                f = self.display.split(',')
                f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]
                value = str(self.util.defIntegrate(self.util.convertStringToFunction(f[0]),float(f[1]),float(f[2])))
                self.executable += value
                self.display = self.tempdisplay + value
                self.cursor = len(self.display)
                self.func = 0
                self.selectedline = 0

        elif (self.func == 'defDer'):
            if (entered):
                self.display.replace("defDer(",'')
                self.display.replace(')','')
                f = self.display.split(',')
                f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]
                value = str(self.util.defDerivative(self.util.convertStringToFunction(f[0]),float(f[1])))
                self.executable += value
                self.display = self.tempdisplay + value
                self.cursor = len(self.display)
                self.func = 0
                self.selectedline = 0

        elif (self.func == 'Sum'):
            if (entered):
                self.display.replace("Sum(",'')
                self.display.replace(')','')
                f = self.display.split(',')
                f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]
                value = str(self.util.summation(self.util.convertStringToFunction(f[0]),float(f[1]),float(f[2])))
                self.executable += value
                self.display = self.tempdisplay + value
                self.cursor = len(self.display)
                self.func = 0
                self.selectedline = 0

        elif (self.func == 'decToFrac'):
            if (entered):
                self.display.replace("decToFrac(",'')
                self.display.replace(')','')
                f = self.display.split(',')
                f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]
                value = self.util.decToFraction(self.util.executeStringFunction(f[0]))
                self.executable += value
                self.display = self.tempdisplay + value
                self.cursor = len(self.display)
                self.func = 0
                self.selectedline = 0

        output.set_cursor(self.cursor,0)

        """
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
            """




controller = controller()
while(True):
    sleep(.1)
