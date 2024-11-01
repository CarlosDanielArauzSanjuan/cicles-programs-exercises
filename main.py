#Escriba un programa que entregue todos los divisores del número entero ingresado:

def get_dividers (number):
    dividers =[]
    for i in range (1, number + 1):
        if number % i == 0:
            dividers.append(i)
    return dividers

number = int(input("enter number: "))

dividers = get_dividers(number)
print("divider of", number, "are:", " ".join(map(str, dividers)))
