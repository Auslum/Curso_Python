#a(b) -> c
def a(b):
    def c():
        print("Antes de la ejecucion")
        b()
        print("Despues de la ejecucion\n")
    return c

def resultado(function):
    def wrapper(*args, **kwargs):
        resultado = function(*args, **kwargs)
        return "Resultado: "+str(resultado)
    return wrapper

@a
def hola_mundo():
    print("Hola Mundo")

@resultado
def division(numero_1, numero_2):
    return numero_1 / numero_2

hola_mundo()
print(division(10, 2))