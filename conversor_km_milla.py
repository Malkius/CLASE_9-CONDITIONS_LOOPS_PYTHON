milla = 0.6214

nombre = input("Saludos, ¿cuál es tu nombre? ")
print(nombre + " vamos a hacer conversiones de kilómetros a millas")

while True:
    pregunta = int(input("Cuántos kilómetros quieres convertir a millas: "))
    print("La conversión es: ", (pregunta * milla), " millas")
    respuesta = input("¿" + nombre + ", quieres realizar otra operación (s/n)? ")
    if respuesta == "s":
        print("De acuerdo, allá vamos de nuevo")
    else:
        print("Hasta pronto " + nombre)
        break
