#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

import math

number = int(input("enter number: "))

for i in range (0, number + 1 ):
    answer = math.pow( 2, i)
    print (f" {answer}")