from utility import utility
from newKeyboard import buttons
from output import output
from time import sleep
from lcdInterface import lcdInterface

class controller():

    def __init__(self):

        self.executable = ""
        self.display = ""
        self.tempdisplay = ""
        self.print = ""

        self.menu = 'Main'      #Main,2nd,Alpha,Math
        self.func = 'None'      #None,defInt,defDer,Sum,decToFrac,Graph


        #self.selectedline = 0   #To scroll through different functions
        self.index = 0 #index of selection
        self.window = [0,22]

        #create objects for useful functions
        self.util = utility()                                   #For calculations and parsing
        self.buttons = buttons()                                #To read from buttons
        self.buttons.setHandler(self.processButtonPress)
        self.lcd = lcdInterface()                                  #To print to screen


    #Activates whenever a button is pressed with key as parameter
    def processButtonPress(self, keyPressed):
        try:
            entered = False
            #Switch between different screens or keypress configurations
            if (self.menu == 'Alpha'):
                keyPressed = str(self.buttons.mapKey('alpha', keyPressed))
            elif (self.menu == "2nd"):
                keyPressed = str(self.buttons.mapKey('2nd', keyPressed))
                print(keyPressed)
                
            if (keyPressed == "2nd"):
                if (self.menu == '2nd'):
                    self.menu = 'Main'
                else:
                    self.menu = '2nd'

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

            #Move the cursor and index with the left and right arrows
            elif (keyPressed == "RIGHT"):
                if(self.index < len(self.display)):
                    print("R")
                    self.index += 1
            elif (keyPressed == "LEFT"):
                if(self.index < len(self.display)):
                    print("L")
                    self.index -= 1

            #Scroll between different options in math functions
            elif (keyPressed == "UP"):
                pass
            elif (keyPressed == "DOWN"):
                pass

            #Activate if enter is pressed
            elif (keyPressed == "ENTER"):
                #If not in a specific function, solve the written expression and display it
                if (self.func == 'None'):
                    self.print = self.display
                    self.lcd.setFirstLine(self.print)
                    self.lcd.execute(str(self.util.executeStringFunction(self.executable)))
                    self.display = ""
                    self.executable = ""
                    if (self.display == '0'):
                        self.display = ""
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
            elif (self.menu == 'Main' or self.menu == '2nd' or self.menu == 'Alpha'):
                if (keyPressed != "None"):
                    if (self.func == 'None'):
                        self.executable = self.executable[:self.index] + keyPressed + self.executable[self.index:]
                        self.display = self.display[:self.index] + keyPressed + self.display[self.index:]
                        self.index += len(keyPressed)
                    else:
                        #If we are operating in a function, use the dynamic variable 'x'
                        if (keyPressed == "X"):
                            keyPressed = 'x'
                        self.display = self.display[:self.index] + keyPressed + self.display[self.index:]
                        self.index += len(keyPressed)

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
                """
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
                """
                self.lcd.clear()
                self.lcd.text("1: defIntegral\n2: defDerivative\n3: summation\n4: decToFrac\n5: graphFunc")

                #display the selection and request parameters
                if (keyPressed == "1"):
                    self.menu = 'Main'
                    self.func = 'defInt'
                    self.lcd.clear()
                    self.lcd.text("defInt(f,a,b)")
                    self.display = "defInt("
                elif (keyPressed == "2"):
                    self.menu = 'Main'
                    self.func = 'defDer'
                    self.lcd.clear()
                    self.lcd.text("defDer(f,a)")
                    self.display = "defDer("
                elif (keyPressed == "3"):
                    self.menu = 'Main'
                    self.func = 'Sum'
                    self.lcd.clear()
                    self.lcd.text("Sum(f,a,b)")
                    self.display = "Sum("
                elif (keyPressed == "4"):
                    self.menu = 'Main'
                    self.func = 'decToFrac'
                    self.lcd.clear()
                    self.lcd.text("decToFrac(a)")
                    self.display = "decToFrac("
                elif (keyPressed == "5"):
                    self.menu = 'Main'
                    self.func = 'graph'
                    self.lcd.clear()
                    self.lcd.text("graph(f)")
                    self.display = "graph("

                #set index to the end of the string ready to edit
                self.index = len(self.display)
                entered = False

            #for each function, parse out the function and the enclosing brackets into different parameters
            if (self.func == 'defInt'):
                if (entered):
                    self.display = self.display.replace("defInt(",'')
                    f = self.display.split(',')
                    f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]

                    #Calculate value of the function and reset the ability to call a function and display value
                    value = str(self.util.defIntegrate(self.util.convertStringToFunction(f[0]),float(f[1]),float(f[2])))
                    self.executable += value
                    self.display = self.tempdisplay + value
                    self.index = len(self.display)
                    self.func = ""
                    self.selectedline = 0

            elif (self.func == 'defDer'):
                if (entered):
                    self.display = self.display.replace("defDer(",'')
                    f = self.display.split(',')
                    f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]
                    value = str(self.util.defDerivative(self.util.convertStringToFunction(f[0]),float(f[1])))
                    self.executable += value
                    self.display = self.tempdisplay + value
                    self.index = len(self.display)
                    self.func = "None"
                    self.selectedline = 0

            elif (self.func == 'Sum'):
                if (entered):
                    self.display = self.display.replace("Sum(",'')
                    f = self.display.split(',')
                    f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]
                    value = str(self.util.summation(self.util.convertStringToFunction(f[0]),float(f[1]),float(f[2])))
                    self.executable += value
                    self.display = self.tempdisplay + value
                    self.index = len(self.display)
                    self.func = "None"
                    self.selectedline = 0

            elif (self.func == 'decToFrac'):
                if (entered):
                    self.display = self.display.replace("decToFrac(",'')
                    f = self.display.split(',')
                    f[len(f)-1] = f[len(f)-1][:(len(f[len(f)-1])-1)]
                    value = self.util.decToFraction(self.util.executeStringFunction(f[0]))
                    self.executable += value
                    self.display = self.tempdisplay + value
                    self.index = len(self.display)
                    self.func = "None"
                    self.selectedline = 0

            elif (self.func == 'graph'):
                if (entered):
                    self.display = self.display.replace("graph(",'')
                    self.display = self.display[:len(self.display)-1]

                    self.lcd.graph1D(self.util.convertStringToFunction(self.display))
                    self.display = ""
                    self.index = len(self.display)
                    self.func = ""
                    self.selectedline = 0
            
            if not(self.menu == 'Math' or self.func == ""):
                self.print = self.display[:self.index] + "|" + self.display[self.index:]
                self.lcd.setFirstLine(self.print)
                
            if (self.func == ""):
                self.func = "None"
            #set blinking cursor location in relation to the window
            #cursor = self.index-self.window[0]
            #self.output.set_cursor(cursor,0)

            #self.output.showMessage(self.display)
            #self.print = self.display[:self.index] + "|" self.display[self.index:]
            #self.lcd.SetFirstLine(self.display[self.window[0],self.window[1]])
            #print(self.display)
        except Exception:
            self.lcd.setFirstLine("Error")
            self.display = ""
            self.executable = ""

    def updateDisplay(self):
        if (i==0):
            self.print = self.display[:self.index] + "|" + self.display[self.index:]
        elif (i==1):
            self.print = self.display[:self.index] + "," + self.display[self.index:]

        self.lcd.setFirstLine(self.print)#[int(self.window[0]),int(self.window[1])])
        print(self.display)


controller = controller()
#i=0
while(True):
    sleep(.1)
    #controller.updateDisplay()
    #i = (i + 1) % 2
