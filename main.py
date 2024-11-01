#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. 
#Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6
n1 = int(input(" enter number: "))
n2 = int(input(" enter number: "))

if n1 > n2:
    n1, n2 = n3, n4
Addition = 0

for i in range (n1 + 1, n2):
    Addition += i
print (f"{Addition}")
