#Funcion de tipo void
def saludo():
    print("Hola Mundo")

#Funcion de tipo flotante
def suma():
    numero_1 = float(input("Numero 1: "))
    numero_2 = float(input("Numero 2: "))
    return numero_1 + numero_2;

resultado = suma()
saludo()
saludo()
saludo()
print("Resultado: ", resultado)