def ver_argumentos(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)

def multiplicacion(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

def datos_personales(**datos):
    for key, value in datos.items():
        print("{} => {}".format(key, value))

resultado = multiplicacion(1, 2, 3, 4, 5)
ver_argumentos(1, 2, 3, nombre = "Brian", apellido = "Gomez")
print("Resultado:", resultado) 
datos_personales(nombre = "Brian", apellido = "Gomez", edad = 22, ocupacion = "programador")