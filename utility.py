from math import *
from fractions import Fraction

"""
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign',
'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial',
'floor', 'fmod', 'frexp', 'fsum', 'func', 'gamma', 'gcd', 'hypot', 'inf', 'isclose',
'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
 'modf', 'nan', 'operator', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh',
 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'util', 'utility'
 """
class utility():

    def __init__(self):
        self.n = 1000
        self.radians = True #False for degrees



    def wrapper(self, string, target, direction):


        while (string.find(target) != -1):
            i = string.find(target)
            j = i + direction


            if (string[j].isdigit()):

                while(string[j].isdigit() or string[j] == '.'):
                    if (j+direction < len(string) and j+direction >= -1):
                        j += direction
                    else:
                        break

            elif (string[j].isalpha()):

                while(string[j].isalpha()):
                    if (j+direction < len(string) and j+direction >= -1):
                        j += direction
                    else:
                        break

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



            string = string[:j-direction] + "?" + string[j-direction:]
            string = string.replace(target, "@",1)


        return string



    def convertStringToFunction(self,strfunction):

        strfunction = strfunction.replace('^',"**")
        strfunction = strfunction.replace('ln',"log")

        strfunction = self.wrapper(strfunction,"!",-1)
        strfunction = strfunction.replace('?',"factorial(")
        strfunction = strfunction.replace('@',")")

        if (not self.radians):
            strfunction = strfunction.replace("cos(","cos((pi/180)*")
            strfunction = strfunction.replace("sin(","sin((pi/180)*")
            strfunction = strfunction.replace("tan(","tan((pi/180)*")

        strfunction = strfunction.replace(' ','')

        i = 0
        while(i<len(strfunction)):
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


        strlambda = "func = lambda x: " + strfunction


        exec(strlambda, globals())

        print(strlambda)
        return func


    def defIntegrate(self, function, a, b):

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


    def defDerivative(self, function, a):

        h = 1 / self.n

        slope = (function(a+h)-function(a))/h

        return slope

    def summation(self,function,a,b):

        sum = 0
        for i in range(a,b+1):
            sum += function(i)

        return sum

    def decToFraction(self,x):
        return str(Fraction(x).limit_denominator())

    def setRadiansMode(self, isOn):
        self.radians = isOn

util = utility()
util.setRadiansMode(True)
func = util.convertStringToFunction("2 (x3( 3)3)")

# print(func(1))
# print(util.defIntegrate(func,0,1))
# print(util.defDerivative(func,1))
#
# print(util.decToFraction(.02))
#
# print(util.summation(func,0,3))
