from math import * 

print("Welcome to the Quadrilateral Classifier!")
print()

again = "Y"

while again == "Y" or "y":

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    print()

    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print()

    x3 = int(input("Enter x3: "))
    y3 = int(input("Enter y3: "))
    print()

    x4 = int(input("Enter x4: ")) 
    y4 = int(input("Enter y4: "))
    print()

    ##CALCULATING SLOPES:
    if x1 == x2:
        slopeAB = "undefined"

    else:
        slopeAB = (y2-y1)/(x2-x1)

    if x2 == x3:
        slopeBC = "undefined"

    else:
        slopeBC = (y3-y2)/(x3-x2)

    if x3 == x4:
        slopeCD = "undefined"

    else:
        slopeCD = (y4-y3)/(x4-x3)

    if x4 == x1:
        slopeDA = "undefined"

    else:
        slopeDA = (y1-y4)/(x1-x4)

    ##CALCULATING LENGTHS
    #Side Lengths
    lengthAB = sqrt((x2-x1)**2 + (y2-y1)**2)
    lengthBC = sqrt((x3-x2)**2 + (y3-y2)**2)
    lengthCD = sqrt((x4-x3)**2 + (y4-y3)**2)
    lengthDA = sqrt((x1-x4)**2 + (y1-y4)**2)

    #Diagonal Lengths
    lengthAC = sqrt((x3-x1)**2 + (y3-y1)**2)
    lengthBD = sqrt((x4-x2)**2 + (y4-y2)**2)

    ##QUADRILATERAL CLASSIFICATION
    if slopeAB == slopeCD:
        
        if slopeBC == slopeDA:
            
            if lengthAC == lengthBD:
                
                if lengthAB == lengthBC == lengthCD == lengthDA:
                    print("You have a square.")

                else:
                    print("You have a rectangle.")

            else:
                if lengthAB == lengthBC == lengthCD == lengthDA:
                    print("You have a rhombus.")
                else:
                    print("You have a parallelogram.")

        else:
            print("You have a trapezoid.")

    else:
        if slopeBC == slopeDA:
            print("You have a trapezoid.")
        else:
            if lengthAB == lengthBC and lengthCD == lengthDA:
                print("You have a kite.")
            else:
                print("You have a boring quadrilateral.")

    print()
    again = input("Would you like to classify another quadrilateral? (Y/N): ")
    print()



