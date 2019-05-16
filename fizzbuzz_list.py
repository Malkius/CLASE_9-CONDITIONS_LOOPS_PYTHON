nombre = input("¿Cuál es su nombre? ")
print(nombre + " vamos a escribir un número del 1 al 100 y comprobar si es divisible por 3, 5 ó ambos.")
tope = int(input("Si su número es divisible entre 3 será fizz, entre 5 será buzz y de ambos será fizzbuzz: "))

for num in range(1, tope + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
while True:
    respuesta = input(nombre + ", otra vez? (s/n) ").lower()
    if respuesta == "s":
        print("De acuerdo, sigamos")
    else:
        print("Hasta la vista")
        break
