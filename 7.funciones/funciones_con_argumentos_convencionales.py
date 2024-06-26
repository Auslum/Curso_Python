def saludo(nombre = "Rosalia"):
    print("Hola " + nombre)

def resta(numero_1 = 100, numero_2 = 100):
    return numero_1 - numero_2

saludo("Luciana")
saludo(nombre = "Gabriel")
saludo()
print("Resultado:", resta(5, 3))
print("Resultado:", resta(numero_1 = 10, numero_2 = 7))
print("Resultado:", resta())
print("Resultado:", resta(numero_2 = 30))


