from math import *
from fractions import Fraction      #lets me cleanly display fractions

u = complex(0,1)

"""     These are all the imported functions from math module

'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign',
'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial',
'floor', 'fmod', 'frexp', 'fsum', 'func', 'gamma', 'gcd', 'hypot', 'inf', 'isclose',
'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
 'modf', 'nan', 'operator', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh',
 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'util', 'utility'
 """

 #
 # contains useful mathematical and formatting functions
class utility():

    def __init__(self):
        self.n = 1000       #number of chunks used in integration and derivatives, the bigger n, the more precise
        self.radians = True #False for degrees



    #general wrapper to enclose messy functions like factorial into parenthesis
    def wrapper(self, string, target, direction):


        while (string.find(target) != -1):      #while a target still exists
            i = string.find(target)             #set initial i and j
            j = i + direction


            #wrap around a float
            if (string[j].isdigit()):

                while(string[j].isdigit() or string[j] == '.'):
                    if (j+direction < len(string) and j+direction >= -1):
                        j += direction
                    else:
                        break

            #wrap around a string
            elif (string[j].isalpha()):

                while(string[j].isalpha()):
                    if (j+direction < len(string) and j+direction >= -1):
                        j += direction
                    else:
                        break

            #wrap around the outermost set of parenthesis
            elif (string[j] == ")" and direction == -1):
                count = 0

                while (True):
                    if (string[j] == ")"):
                        count += 1
                    elif (string[j] == "("):
                        count -= 1

                    j += direction

                    if (count == 0):
                        break


            #insert indicator characters and remove target
            string = string[:j-direction] + "?" + string[j-direction:]
            string = string.replace(target, "@",1)


        return string


    #converts a string mathematical expression into a useful formula
    def convertStringToFunction(self,strfunction):

        assignment = False
        #remove all whitespace
        strfunction = strfunction.replace(' ','')

        #check if its an assignment instead of an expression
        if (strfunction != ""):
            if (strfunction[1] == "="):
                assignment = True
                var = strfunction[0].upper()
                strfunction = strfunction[2:]   #remove the assignment for parsing

        #replace pretty things with functional things
        strfunction = strfunction.replace('^',"**")
        strfunction = strfunction.replace('ln',"log")
        strfunction = strfunction.replace('i',"u")

        #add * sign between variables and numbers and paranthesis if necessary
        i = 0
        while(i<len(strfunction)):
            #add * between distributions
            if (strfunction[i].isalpha()):
                if (i!=0):
                    if (strfunction[i-1].isdigit() or strfunction[i-1] == ')'):
                        strfunction = strfunction[:i] + '*' + strfunction[i:]
                if (i!=len(strfunction)-1):
                    if (strfunction[i+1].isdigit() or strfunction[i+1] == '('):
                        strfunction = strfunction[:i+1] + '*' + strfunction[i+1:]

            elif (strfunction[i] == '('):
                if (i!=0):
                    if (strfunction[i-1].isdigit()):
                        strfunction = strfunction[:i] + '*' + strfunction[i:]
            elif (strfunction[i] == ')'):
                if (i!=len(strfunction)-1):
                    if (strfunction[i+1].isdigit()):
                        strfunction = strfunction[:i+1] + '*' + strfunction[i+1:]
            i += 1

        #use wrapper to replace factorial expression
        strfunction = self.wrapper(strfunction,"!",-1)
        strfunction = strfunction.replace('?',"factorial(")
        strfunction = strfunction.replace('@',")")

        #if in degrees mode, change degrees into radians for input and degrees into radians for output
        if (not self.radians):
            strfunction = strfunction.replace("cos(","cos((pi/180)*")
            strfunction = strfunction.replace("sin(","sin((pi/180)*")
            strfunction = strfunction.replace("tan(","tan((pi/180)*")
            strfunction = strfunction.replace("acos(","(180/pi)*acos(")
            strfunction = strfunction.replace("asin(","(180/pi)*asin(")
            strfunction = strfunction.replace("atan(","(180/pi)*atan(")

        if (not assignment):
            #create executable string
            strlambda = "func = lambda x: " + strfunction + "+0*x"

            #print(strlambda)
            #execute string and make func accessible again
            exec(strlambda, globals())

            return func

        #if its an assignment, say so
        else:
            strassign = var + " = " + strfunction
            exec(strassign, globals())

            return (None)


    #definate integral of function with bounds [a,b]
    def defIntegrate(self, function, a, b):

        #use simpson's method to numerically approximate the integral
        h = (b-a)/self.n
        area = function(a) + function(b)

        for i in range(1,self.n):
            x = a + i*h

            if (i % 2 == 0):
                area += 2 * function(x)
            else:
                area += 4 * function(x)

        area *= h/3
        return area

    #definate derivative of function at a
    def defDerivative(self, function, a):

        #use definition of derivative to numerically approximate derivative
        h = 1 / self.n

        slope = (function(a+h)-function(a))/h

        return slope

    #summation of function from a to b
    def summation(self,function,a,b):

        sum = 0
        for i in range(a,b+1):
            sum += function(i)

        return sum

    #convert some decimal to nice fraction
    def decToFraction(self,x):
        return str(Fraction(x).limit_denominator())

    #set Mode, True:Radians Mode :: False:Degrees Mode
    def setRadiansMode(self, isOn):
        self.radians = isOn

    def executeStringFunction(self,strfunction):
        fun = self.convertStringToFunction(strfunction)
        if (fun != None):
            return fun(0)
        else:
            return strfunction

util = utility()
util.setRadiansMode(True)
func = util.convertStringToFunction("")

#print(util.executeStringFunction("A=2"))

#util.convertStringToFunction("a=15")
#print(A)

# print(X)
#
# print(func(9))
# print(util.defIntegrate(func,0,1))
# print(util.defDerivative(func,1))
#
# print(util.decToFraction(pi))
#
# print(util.summation(func,0,3))
