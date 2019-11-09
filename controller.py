from utility import utility


class controller():

    def __init__(self):

        self.executable = ""
        self.display = ""
        self.menu = 'Main'      #Main,2nd,Alpha,Math

        self.util = utility



    def processButtonPress(self):

        while(True):
            #waitforkeyfunction
            #keyPressed = key
            break


        if (keyPressed == "2nd"):
            if (self.menu == '2nd'):
                self.menu = 'Main'
            #switcharrayto2nd
            pass

        elif (keyPressed == "Alpha"):

            #switcharraytoAlpha
            pass
        elif (keyPressed == "Math"):
            #switch
            pass

        elif (keyPressed == "RIGHT"):
            pass
        elif (keyPressed == "LEFT"):
            pass
        elif (keyPressed == "UP"):
            pass
        elif (keyPressed == "DOWN"):
            pass

        elif (keyPressed == "ENTER"):
            self.display = self.util.executeStringFunction(self.executable)

        else:
            self.executable += keyPressed
