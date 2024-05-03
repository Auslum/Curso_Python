edad = int(input("Ingresa tu edad: "))
edad_par = "es par" if edad % 2 == 0 else "no es par"
print("Eres mayor de edad") if edad >= 18 else print("No eres mayor de edad")
print("Tu edad es un numero que " + edad_par)