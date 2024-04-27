'''
is
is not
'''

numero_1 = 11
numero_2 = 11
numero_3 = 33
set_1 = {1, 2, 3}
set_2 = {1, 2, 3}
set_3 = set_1

set_3.add(4)
set_3.add(5)

print("numero_1:", numero_1, id(numero_1))
print("numero_2:", numero_2, id(numero_2))
print("numero_3:", numero_3, id(numero_3))
print("set_1:", set_1, id(set_2))
print("set_2:", set_2, id(set_2))
print("set_3:", set_3, id(set_3))

print(numero_1 is numero_2)
print(numero_1 is numero_3)
print(numero_1 is not numero_3)

print(set_1 is set_2)
print(set_1 is not set_3)