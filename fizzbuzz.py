nombre = input("¿Cuál es su nombre? ")

while True:
    numero = int(input(nombre + ", elija un múmero del 1 al 100 y le diremos si es múltiplo de 3, de 5 o de ambos: "))
    if numero > 100:
        print("Por favor, escriba un número menor de 100")
    else:
        if numero % 3 == 0 and numero % 5 == 0:
            print("Este número es múltiplo de 3 y también de 5")
        elif numero % 3 == 0:
            print("Este número es múltiplo de 3")
        elif numero % 5 == 0:
            print("Este número es múltiplo de 5")
        else:
            print("Este número no es múltiplo de 3 ni de 5")

        respuesta = input("¿Quiere seguir probando (s/n?) ").lower()
        if respuesta == "s":
            print("Sigamos pues " + nombre)
        else:
            print("Hasta la próxima " + nombre)
            break
