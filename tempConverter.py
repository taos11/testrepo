##Tempature Converter
# Celsius
def cToK(n1):
    return n1 + 273.15
def cToF(n2):
    return n2 * 9 / 5 + 32 
def cToR(n3):
    return n3 + 273.15 * 9 / 5
# Fahrenheit
def fToC(n4):
    return n4 - 32 * 5 / 9
def fToK(n5):
    return n5  + 459.67 * 5 / 9
def ftoR(n6):
    return n6  + 459.67
# Kelvin
def kToF(n7):
    return n7 * 9 / 5 - 459.67
def kToC(n8):
    return n8 - 273.15
def kToR(n9):
    return n9 * 9 / 5
# Rankin
def rToF(n10):
    return n10 - 459.67
def rToC(n11):
    return n11 - 491.67 * 5 / 9
def rToK(n12):
    return n12 * 5 / 9
tempConverter = True
while tempConverter:
    try:
        varOne = input("Please enter the first variable's first letter in capital: ")
        varTwo = input("Please enter the second variable's first letter in capital ")
        if varOne not in "FRKC" or varTwo not in "FRKC":
            print("Please enter a valid unit")
        if varOne == "C" and varTwo == "K":
            xx = int(input("Please enter the Celsius: "))
            ff = cToK(xx)
            print(f"{xx} Celsius is {ff} Kelvin")
        if varOne == "C" and varTwo == "F":
            xx = int(input("Please enter the Celsius: "))
            ff = cToF(xx)
            print(f"{xx} Celsius is {ff} Fahrenheit")
        if varOne == "C" and varTwo == "R":
            xx = int(input("Please enter the Celsius: "))
            ff = cToR(xx)
            print(f"{xx} Celsius is {ff} Rankin")
        if varOne == "F" and varTwo == "C":
            xx = int(input("Please enter the Fahrenheit: "))
            ff = fToC(xx)
            print(f"{xx} Fahrenheit is {ff} Celsius")
        if varOne == "F" and varTwo == "K":
            xx = int(input("Please enter the Fahrenheit: "))
            ff = fToK(xx)
            print(f"{xx} Fahrenheit is {ff} Kelvin")
        if varOne == "F" and varTwo == "R":
            xx = int(input("Please enter the Fahrenheit: "))
            ff = fToR(xx)
            print(f"{xx} Fahrenheit is {ff} Rankin")
        if varOne == "K" and varTwo == "F":
            xx = int(input("Please enter the Kelvin: "))
            ff = kToF(xx)
            print(f"{xx} Kelvin is {ff} Fahrenheit")
        if varOne == "K" and varTwo == "F":
            xx = int(input("Please enter the Kelvin: "))
            ff = kToF(xx)
            print(f"{xx} Kelvin is {ff} Celsius")
        if varOne == "K" and varTwo == "R":
            xx = int(input("Please enter the Kelvin: "))
            ff = kToR(xx)
            print(f"{xx} Kelvin is {ff} Rankin")
        if varOne == "R" and varTwo == "F":
            xx = int(input("Please enter the Rankin: "))
            ff = rToF(xx)
            print(f"{xx} Rankin is {ff} Fahrenheit")
        if varOne == "R" and varTwo == "C":
            xx = int(input("Please enter the Rankin: "))
            ff = rToC(xx)
            print(f"{xx} Rankin is {ff} Celsius")
        if varOne == "R" and varTwo == "K":
            xx = int(input("Please enter the Rankin: "))
            ff = rToK(xx)
            print(f"{xx} Rankin is {ff} Kelvin")
    except:
        print("Please enter a Number. ")
    

        
         

