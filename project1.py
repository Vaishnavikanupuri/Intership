import math 
import time

def length(unit1,unit2,num1):
    if unit1 == "cm" and unit2 == "m":
        ans = float(num1)/100       
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1)/10
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1)*100
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1)*10
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1)/1000
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1)*1000  
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1)*1000
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1)/1000
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1)/1000000
    else:
        ans = "Invalid unit"
    return ans

def weight(unit1,unit2,num1):
    if unit1=="kg" and unit2=="g":
        ans=float(num1)*1000  # kg to g should multiply by 1000
    elif unit1=="g" and unit2=="kg":
        ans=float(num1)/1000  # g to kg should divide by 1000
    elif unit1=="mg" and unit2=="kg":
        ans=float(num1)/1000000
    elif unit1=="kg" and unit2=="mg":
        ans=float(num1)*1000000
    elif unit1=="g" and unit2=="mg":
        ans=float(num1)*1000
    elif unit1=="mg" and unit2=="g":
        ans=float(num1)/1000  # mg to g should divide by 1000
    elif unit1=="lbs" and unit2=="kg":
        ans=float(num1)/2.205
    elif unit1=="kg" and unit2=="lbs":
        ans=float(num1)*2.205
    else:
        ans = "Invalid unit"
    return ans
        
def temperature(unit1,unit2,num1):
    if unit1=="c" and unit2=="f":
        ans=float(num1)*(9/5) + 32
    elif unit1=="f" and unit2=="c":
        ans=(float(num1)-32) * 5/9
    else:
        ans = "Invalid unit"
    return ans    

def time(unit1, unit2, num1):
    if unit1 == "sec" and unit2 == "min":
        ans = float(num1) / 60
    elif unit1 == "min" and unit2 == "sec":
        ans = float(num1) * 60
    elif unit1 == "hr" and unit2 == "min":
        ans = float(num1) * 60
    elif unit1 == "min" and unit2 == "hr":
        ans = float(num1) / 60
    else:
        ans = "Invalid unit"
    return ans

def volume(unit1, unit2, num1):
    if unit1 == "ltr" and unit2 == "ml":
        ans = float(num1) * 1000
    elif unit1 == "ml" and unit2 == "ltr":
        ans = float(num1) / 1000  
    elif unit1 == "gallons" and unit2 == "ltr":
        ans = float(num1) * 3.785
    elif unit1 == "ltr" and unit2 == "gallons":
        ans = float(num1) / 3.785
    else:
        ans = "Invalid unit"
    return ans

category = input("Which unit would you like to convert (l for length, w for weight, t for temperature, ti for time, v for volume): ").lower()

if category == "l":  # length
    unit1 = input("Which unit would you like to convert from: ").lower()
    unit2 = input("Which unit would you like to convert to: ").lower()
    num1 = float(input("Enter a value: "))  # Convert input to float here
    output = length(unit1, unit2, num1)
elif category == "w":  # weight
    unit1 = input("Which unit would you like to convert from: ").lower()
    unit2 = input("Which unit would you like to convert to: ").lower()
    num1 = float(input("Enter a value: "))
    output = weight(unit1, unit2, num1)
elif category == "t":  # temperature
    unit1 = input("Which unit would you like to convert from: ").lower()
    unit2 = input("Which unit would you like to convert to: ").lower()
    num1 = float(input("Enter a value: "))
    output = temperature(unit1, unit2, num1)
elif category == "ti":  # time
    unit1 = input("Which unit would you like to convert from: ").lower()
    unit2 = input("Which unit would you like to convert to: ").lower()
    num1 = float(input("Enter a value: "))
    output = time(unit1, unit2, num1)
elif category == "v":  # volume
    unit1 = input("Which unit would you like to convert from: ").lower()
    unit2 = input("Which unit would you like to convert to: ").lower()
    num1 = float(input("Enter a value: "))
    output = volume(unit1, unit2, num1)
else:
    output = "Invalid category"

print(f"{num1} {unit1} is equal to {output} {unit2}")
