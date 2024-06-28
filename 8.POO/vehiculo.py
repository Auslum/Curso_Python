class Vehiculo:
    def __init__(self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = str(precio)+"$"
        self.arrancar = False

if __name__ == "__main__":
    auto = Vehiculo("Tesla", "Model S", "Rojo", "90,000")
    moto = Vehiculo("BMW", "CE04", "Negro", "13,000")
    camion = Vehiculo("Volvo", "FH16", "Gris", "40,000")
    #auto.modelo = "Cybertruck"
    #del auto.precio
    moto.arrancar = True
    for vehiculo in (auto, moto, camion):
        print(f"Vehiculo: {vehiculo.marca} {vehiculo.modelo}\nColor: {vehiculo.color}\nPrecio: {vehiculo.precio}")
        print("Arrancar:", vehiculo.arrancar, "\n")