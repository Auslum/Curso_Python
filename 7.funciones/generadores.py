from time import sleep

def range_generator(start=0, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0
    while start < stop:
        sleep(1)
        yield start
        start += step

resultado = range_generator(1, 11)
for i in resultado:
    print(i)
print("\n")
for i in range_generator(16):
    print(i)