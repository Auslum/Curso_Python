'''
128 64 32 16 8 4 2 1
               1 0 1 -> 5
               1 1 1 -> 7

               1 0 1 -> 5
               1 1 1 -> 7
               0 1 0 -> 2
                 1 0 1 -> 2
                   1 0 1 -> 1
              1 1 1 ->  14
            1 1 1 -> 28
                 1 1 1 -> 3
                1 1 -> 6
'''
a = 0b101
b = 0b111

#NOT bit a bit
print(~ a)
print(bin(~ a))

#AND bit a bit
print(a & b)
print(bin(a & b))

#OR bit a bit
print(a | b)
print(bin(a | b))

#XOR bit a bit
print(a ^ b)
print(bin(a ^ b))

#Desplazamiento a la derecha
print(a >> 1)
print(bin(a >> 1))
print(a >> 2)
print(bin(a >> 2))

#Desplazamiento a la izquierda
print(b << 1)
print(bin(b << 1))
print(b << 2)
print(bin(b << 2))

#Operadores de asignacion a nivel de Bit
a &= b
a |= b
b ^= a
a >>= 1
a <<= 1

print("a: ", a, bin(a))
print("b: ", b, bin(b))