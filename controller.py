from utility import utility
from newKeyboard import buttons
from output import output
from time import sleep


class controller():

    def __init__(self):

        self.executable = ""
        self.display = ""
        self.tempdisplay = ""

        self.menu = 'Main'      #Main,2nd,Alpha,Math
        self.func = 'None'      #None,defInt,defDer,Sum,decToFrac


        self.selectedline = 0   #To scroll through different functions
        self.index = 0 #index of selection
        self.window = [0,15]

        #create objects for useful functions
        self.util = utility()                                   #For calculations and parsing
        self.buttons = buttons()                                #To read from buttons
        self.buttons.setHandler(self.processButtonPress)
        self.output = output()                                  #To print to screen


    #Activates whenever a button is pressed with key as parameter
    def processButtonPress(self, keyPressed):

        #Switch between different screens or keypress configurations
        if (keyPressed == "2nd"):
            if (self.menu == '2nd'):
                self.menu = 'Main'
                self.buttons.setKeys(self.buttons.mainkeys)
            else:
                self.menu == '2nd'
                self.buttons.setKeys(self.buttons.secondkeys)

        elif (keyPressed == "Alpha"):
            if (self.menu == 'Alpha'):
                self.menu = 'Main'
                self.buttons.setKeys(self.buttons.mainkeys)
            else:
                self.menu = 'Alpha'
                self.buttons.setKeys(self.buttons.alphakeys)

        elif (keyPressed == "Math"):
            if (self.menu == 'Math'):
                self.menu = 'Main'
            else:
                self.menu = 'Math'


        #Move the cursor and index with the left and right arrows
        elif (keyPressed == "RIGHT" and self.index < len(self.display)):
            self.output.moveRight()
            self.index += 1
        elif (keyPressed == "LEFT" and self.index > 0):
            self.output.moveLeft()
            self.index -= 1

        #Scroll between different options in math functions
        elif (keyPressed == "UP"):
            self.selectedline = (self.selectedline + 1) % 4
        elif (keyPressed == "DOWN"):
            self.selectedline = (self.selectedline - 1) % 4


        #Activate if enter is pressed
        elif (keyPressed == "ENTER"):
            #If not in a specific function, solve the written expression and display it
            if (self.func == 'None'):
                self.display = str(self.util.executeStringFunction(self.executable))
                self.executable = ""
            #If in a specific function, confirm you finished entering parameters and execute
            else:
                entered = True

        #delete current selection
        elif (keyPressed == "DELETE"):
            if (self.func == 'None'):
                self.executable = self.executable[:self.index] + self.executable[self.index+1:]
                self.display = self.display[:self.index] + self.display[self.index+1:]
            else:
                self.display = self.display[:self.index] + self.display[self.index+1:]

        #If no special key was pressed, add the key into the expression string starting at the selection
        elif (self.menu == 'Main' or self.menu == '2nd'):
            if (self.func == 'None'):
                self.executable = self.executable[:self.index] + keyPressed + self.executable[self.index:]
                self.display = self.display[:self.index] + keyPressed + self.display[self.index:]
                self.index += 1
            else:
                #If we are operating in a function, use the dynamic variable 'x'
                if (keyPressed == "X"):
                    keyPressed = 'x'
                self.display = self.display[:self.index] + keyPressed + self.display[self.index:]
                self.index += 1

        #If the selection is off the screen, move the screens view until it aint
        while ((self.index < self.window[0]) or (self.index > self.window[1])):
            if (self.index < self.window[0]):
                self.window[0] -= 1
                self.window[1] -= 1

            elif (self.index > self.window[1]):
                self.window[0] += 1
                self.window[1] += 1

        #If we are in the math menu, and have not selected a function, display the menu
        if (self.menu == 'Math' and self.func == 'None'):
            #store current display to not lose information
            self.tempdisplay = self.display
            self.selectedline = 0

            #allow scrolling to get to selected item
            if (self.selectedline == 0):
                self.display = "1: defIntegral"
            elif (self.selectedline == 1):
                self.display = "2: defDerivative"
            elif (self.selectedline == 2):
                self.display = "3: Summation"
            elif (self.selectedline == 3):
                self.display = "4: decToFrac"

            #display the selection and request parameters
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

            #set index to the end of the string ready to edit
            self.index = len(self.display)
            entered = False

        #for each function, parse out the function and the enclosing brackets into different parameters
        if (self.func == 'defInt'):
            if (entered):
                self.display.replace("defInt(",'')
                self.display.replace(')','')
                f = self.display.split(',')
                f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]

                #Calculate value of the function and reset the ability to call a function and display value
                value = str(self.util.defIntegrate(self.util.convertStringToFunction(f[0]),float(f[1]),float(f[2])))
                self.executable += value
                self.display = self.tempdisplay + value
                self.index = len(self.display)
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
                self.index = len(self.display)
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
                self.index = len(self.display)
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
                self.index = len(self.display)
                self.func = 0
                self.selectedline = 0

        #set blinking cursor location in relation to the window
        #cursor = self.index-self.window[0]
        #self.output.set_cursor(cursor,0)

        #self.output.showMessage(self.display)
        print(self.display)


controller = controller()
while(True):
    sleep(.1)
