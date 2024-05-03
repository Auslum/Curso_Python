#range(start, stop, step)
numeros_pares = []

for element in range(1, 101):
    if element % 2 != 0:
        continue
    if element == 50:
        break
    else:
        pass
    numeros_pares.append(element)

for i in numeros_pares:
    print(i)
