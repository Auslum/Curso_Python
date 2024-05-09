#List Comprehension
abecedario = "abcdefghijklmnñopqrstuvwxyz"
letras = [letra for letra in abecedario]
print(letras)

#Tuple Comprehension
numeros = *(i for i in range(1, len(letras) + 1)),
print(numeros)

#Dictionary Comprehension
diccionario = {key: value for key, value in zip(letras, numeros)}
print(diccionario)
print(diccionario.get("m"))

#Set Comprehension
numeros_pares = {i for i in numeros if i % 2 == 0}
print(numeros_pares)