def Faren_to_Cel(Fahrenheit):
    return ((Fahrenheit - 32) * (5 / 9))

Fahrenheit = float(input("Enter Fahrenheit to convert: "))
Centigrade  = Faren_to_Cel(Fahrenheit)
print(Centigrade)