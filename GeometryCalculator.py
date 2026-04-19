import math
import os

def clear():
    os.system('cls')

def key():
    input("Press any key to continue...")

def ask():

    asking = input("Area or Perimeter?: ").lower()
    return asking

def wrong():
    print("Error. You entered a non-existent characteristic")
    input("Press any key...")

def circle(answer):

    if answer == "area":

        radius = float(input("radius: "))
        cArea = math.pi * radius ** 2
        result = print(f"Area of the Circle is {round(cArea, 2)}")
        key()
        

    elif answer == "perimeter":

        radius = float(input("radius: "))
        cPer = 2 * math.pi * radius
        result = print(f"Perimeter of the Circle is {round(cPer, 2)}")
        key()
    
    else:
        wrong()
    
def square(answer):
        
    if answer == "area":

        side = float(input("side: "))
        sArea = side ** 2
        result = print(f"Area of the Square is {round(sArea, 2)}")
        key()

    elif answer == "perimeter":

        side = float(input("side: "))
        sPer = side * 4
        result = print(f"Perimeter of the Circle is {round(sPer, 2)}")
        key()
    else:
        wrong()

def triangle(answer):
        
    if answer == "area":

        base = float(input("Base of a Triangle: "))
        height = float(input("Triangle height: "))
        tArea = (base * height) / 2
        result = print(f"Area of the Triangle is: {tArea}")
        key()

    elif answer == "perimeter":

        side1 = float(input("First side: "))
        side2 = float(input("Second side: "))
        side3 = float(input("Third side: "))
        tPer = side1 + side2 + side3
        result = print(f"Perimeter of the triangle is {tPer}")
        key()

    else:

        wrong()
        
def rectangle(answer):

    if answer == "area":

        side1 = float(input("First side: "))
        side2 = float(input("Second side: "))
        rArea = side1 * side2
        result = print(f"Area of the Rectangle is {rArea}")
        key()
        
    elif answer == "perimeter":

        side1 = float(input("First side: "))
        side2 = float(input("Second side: "))
        rPer = 2 * (side1 + side2)
        result = print(f"Perimeter of the Rectangle is {rPer}")
        key()
    else:
        wrong()
        
def rhombus(answer):
             
    if answer == "area":

        side = float(input("side: "))
        height = float(input("Rhombus height: "))
        rhArea = side * height
        result = print(f"Area of the Rhombus: {rhArea}")
        key()

    elif answer == "perimeter":

        side = float(input("side: "))
        rhPer = side * 4
        result = print(f"Perimeter of the Rhombus is {rhPer}")
        key()
    else:
        wrong()

def trapezium(answer):
    if answer == "area":

        base1 = float(input("First base of a Trapezium: "))
        base2 = float(input("Second base of a Trapezium: "))
        height = float(input("Trapezium height: "))
        trArea = ((base1 + base2) / 2) * height
        result = print(f"Area of the Trapezium is {trArea}")
        key()
        
    elif answer == "perimeter":

        side1 = float(input("First side: "))
        side2 = float(input("Second side: "))
        side3 = float(input("Third side: "))
        side4 = float(input("Fourth side: "))
        trPer = side1 + side2 + side3 + side4
        result = print(f"Perimeter of the Trapezium is {trPer}")
        key()
    else:
        wrong()

while True:
    clear()
    figure = input("(Circle, Square, Triangle, Rectangle, Rhombus, Trapezium)\n" \
    "Select a geometric figure: ").lower()

    answer = ask()

    match figure:

        case "circle":

            circle(answer)

        case "square":

            square(answer)

        case "triangle":
         
            triangle(answer)

        case "rectangle":

            rectangle(answer)

        case "rhombus":
          
            rhombus(answer)
        
        case "trapezium":
        
            trapezium(answer)
