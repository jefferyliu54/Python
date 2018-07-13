####################################################################
#                                                                  #
#         Title: Team Coding Assignment - Factoring Project        #
#         Programmers: Crystal Kong & Jeffery Liu                  #
#         Last Modified: 11/27/2017                                #
#         Description: Tester                                      #
#                                                                  #
####################################################################

from FactoringToolbox import *

#Array of Test Cases
testCases = ["x^2+18x+32", "x^2+17x+32", "x^2-16x+63", "x^2+5x-24", "x^2-5x-24", "x^2-9", "x^2-10", "x^2+9",    #a = 1 and no common factoring is possible
             "2x^2+11x+5", "12x^2-7x-10", "87x^2-29x+143", "9x^2-100", "9x^2+1",                                #a > 1 and no common factoring is possible
             "3x^2+12x+6", "2x^2+10x+8", "5x^2-500", "x^2+7x", "-10x^2+5x"]                                     #common factoring is possible

#Loop to go through the array and factor each test case 
for t in testCases:
    print(t, "=", determineFactoredQuadratic(t)) 
