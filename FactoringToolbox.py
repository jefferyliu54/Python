#####################################################################
#                                                                  #
#         Title: Team Coding Assignment - Factoring Project        #
#         Programmers: Crystal Kong & Jeffery Liu                  #
#         Last Modified: 11/27/2017                                #
#         Description: Factoring Toolbox                           #
#                                                                  #
####################################################################

from math import *

#Function obtains values for a, b, and c from quadratic expression
def getABCvalues( quadratic ):
    
    #Finds x^2 in expression to determine value of a
    s = quadratic
    xSquaredIndex = s.find("x^2")

    #Obtains value of a 
    if xSquaredIndex == 0:
        a = 1
    else:
        a = int(s[0:xSquaredIndex])

    #Finds x to determine value of b 
    s2 = s[xSquaredIndex+3:]
    xIndex = s2.find("x")

    #Obtains value of b & c when b has no value 
    if xIndex == -1:
        b = 0
        s3 = s[xSquaredIndex+3:]
        c = int(s3)

    #Obtains value of b when it has a value 
    else:
        if s2[0:xIndex] == "+":
            b = 1
        else: 
            b = int(s2[0:xIndex])
            
        #Obtains value of c 
        s3 = s2[xIndex+1:]
        if len(s3) == 0:
            c = 0
        else:
            c = int(s3)

    #Puts values of a,b,c into an array
    abcValues = [a, b, c]

    return abcValues

#Function finds common factor of the quadratic expression
def getCommonFactor( a, b, c ):

    #Turns a,b,c positive to find largest # of potential common factors  
    if a < 0:
        a1 = abs(a)
    else:
        a1 = a 
    if b < 0:
        b1 = abs(b)
    else:
        b1 = b 
    if c < 0:
        c1 = abs(c)
    else:
        c1 = c
        
    Max = max(a1,b1,c1)

    #Prepares array for possible common factors 
    commonFactors = [0]

    #Tests all positive integers up until max value
    for i in range(1, Max+1):
        
        #Checks if integer divides evenly into a, b, and c
        remA = a1 % i
        remB = b1 % i
        remC = c1 % i

        #Stores all possible common factors
        if remA == 0 and remB == 0 and remC == 0:
            commonFactors.append(i)

            #Finds GCF by removing smaller common factors 
            j = commonFactors[0]
            k = commonFactors[1]
            
            minFactor = min(j,k)
            commonFactors.remove(minFactor)

    #Sets value for + or - common factor
    if a > 0:
        cf = commonFactors[0]
    else:
        cf = commonFactors[0] * -1
    
    return cf

#Function divides common factor out of a, b, and c
def removeCommonFactor( a, b, c, commonFactor ):
    
    #Update a, b, and c with common factor removed 
    a = int(a/commonFactor)
    b = int(b/commonFactor)
    c = int(c/commonFactor)
    
    abcValues = [a, b, c]
    
    return abcValues

#Function to factor the quadratic expression 
def determineFactoredQuadratic( quadratic ):

    #Calls function that gets a, b, and c values
    abc = getABCvalues(quadratic)

    #Sets a, b, and c values 
    a = abc[0]
    b = abc[1]
    c = abc[2]

    #Calls common factor function
    cf = getCommonFactor(a, b, c)

    #Removes cf if there is one and factored a,b,c values
    if cf > 1 or cf <= -1:
        newABC = removeCommonFactor(a,b,c, cf) 
        a = newABC[0]
        b = newABC[1]
        c = newABC[2]

    #Prepares arrays for factors of a and c & Boolean flag 
    aFactors = []
    cFactors = []
    cantBeFactored = True

    #Common factors for binomial (when there is no c)
    if c == 0:
        
        #Removes 1's and changes signs for final answer 
        if cf == 1:
            cf = ""
        if cf == -1:
            cf = "-"
            
        if a == 1:
            a = ""
            
        if b > 0:
            b = "+" + str(abs(b))
        else:
            b = "-" + str(abs(b))
            
        #Writes final factored form
        factoredQuadratic = str(cf) + "x(" + str(a) + "x" + str(b) + ")"

        return factoredQuadratic

    #Factors expression when c has a value 
    else:
        #Finds + and - factors of a when it is positive
        if a > 0:
            for x in range(-a, a+1):
                #Skips division by zero 
                if x == 0:
                    continue
                #Calculates all possible factors of a 
                else: 
                    multiple = a / x
                    if multiple == int(multiple):
                        aFactors.append(x)
                        aFactors.append(int(multiple))

        #Finds + and - factors of a when it is negative       
        else:
            for x in range(a, -a+1):
                if x == 0:
                    continue
                else: 
                    multiple = a / x
                    if multiple == int(multiple):
                        aFactors.append(x)
                        aFactors.append(int(multiple))

        #Finds + and + factors of c when it is positive
        if c > 0:
            for x in range(-c, c+1):
                if x == 0:
                    continue
                else:
                    multiple = c / x
                    if multiple == int(multiple):
                        cFactors.append(x)
                        cFactors.append(int(multiple))

        #Finds + and - factors of c when it is negative
        else:
            for x in range(c, -c+1):
                if x == 0:
                    continue
                else: 
                    multiple = c / x
                    if multiple == int(multiple):
                        cFactors.append(x)
                        cFactors.append(int(multiple))

        #Cycles through each pair of factors for a and c
        for i in range(0, int(len(aFactors)/2)):
            for j in range(0, int(len(cFactors)/2)):

                #Cross multiplies factor pairs of a and c
                crossMultiply = aFactors[2*i]*cFactors[2*j+1] + aFactors[2*i+1]*cFactors[2*j]
                
                #Sets values when correct factors are obtained 
                if crossMultiply == b:
                    x1 = aFactors[2*i]
                    y1 = cFactors[2*j]
                    x2 = aFactors[2*i+1]
                    y2 = cFactors[2*j+1]

                    #Checks that positive factors for a are used in final answer
                    if x1 > 0 and x2 > 0:
                        
                        #Removes 1's and changes signs 
                        if cf == 1:
                            cf = ""
                        if cf == -1:
                            cf = "-"
                            
                        if x1 == 1:
                            x1 = ""
                        if x2 == 1:
                            x2 = ""
                            
                        if y1 > 0:
                            y1 = "+" + str(abs(y1))
                        else:
                            y1 = "-" + str(abs(y1))
                            
                        if y2 > 0:
                            y2 = "+" + str(abs(y2))
                        else:
                            y2 = "-" + str(abs(y2))

                        #Writes final factored form
                        factoredQuadratic = str(cf) + "(" + str(x1) + "x" + str(y1) + ")(" + str(x2) + "x" + str(y2) + ")"

                        #Writes factored form when expression is a perfect square
                        if x1 == x2 and y1 == y2:
                            factoredQuadratic = str(cf) + "(" + str(x1) + "x" + str(y1) + ")^2"

                        #Changes Boolean flag since the expression can be factored
                        cantBeFactored = False

                        return factoredQuadratic

    #When expression can only be common factored 
    if cantBeFactored and cf > 1 or cantBeFactored and cf <= -1:
        
        #Removes 1's and changes signs 
        if cf == 1:
            cf = ""
        if cf == -1:
            cf = "-"
            
        if a == 1:
            a = "x^2"
            
        if b > 0:
            b = "+" + str(abs(b)) + "x"
        elif b == 0:
            b = ""
        else:
            b = "-" + str(abs(b)) + "x"
            
        if c > 0:
            c = "+" + str(abs(c))
        else:
            c = "-" + str(abs(c))

        #Writes final factored answer
        factoredQuadratic = str(cf) + "(" + str(a) + str(b) + str(c) + ")"
        
        return factoredQuadratic

    #Returns if expression cannot be factored in any way 
    else:
        return "can't be factored"
