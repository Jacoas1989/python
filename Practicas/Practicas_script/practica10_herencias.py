'''Enunciado
* Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.

* Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su
clase y sus atributos.

* Modifica la función catalogar() para que:
        1.Reciba un argumento optativo ruedas:
            haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento.
        2.También debe mostrar un mensaje
            "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas.
        3.Ponla a prueba con 0, 2 y 4 ruedas como valor.

Recordatorio:
Puedes utilizar el atributo especial de clase name para recuperar el nombre de la clase de un objeto:
type(objeto).name'''

class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)


# definimos las subclases:
class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


    def __str__(self):
        return Vehiculo.__str__(self)+" {} velocidad y {} cilindrada".format(self.velocidad,self.cilindrada)

class Bici(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo


    def __str__(self):
        return Vehiculo.__str__(self)+" y tipo {}".format(self.tipo)


class Camioneta(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.carga = carga


    def __str__(self):
        return Vehiculo.__str__(self)+"{} velocidad  {} cilindrada y carga de {}".format(self.velocidad,self.cilindrada,self.carga)

class Moto(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self)+", {} velocidad y {} cilindrada".format(self.velocidad,self.cilindrada)

# Soluciones:

print("objeto de cada clase:")
coche = Coche("azul", 4, 120, 60)
print(coche)

moto = Moto("negra", 2, 160, 50)
print(moto)

camioneta = Camioneta("blanca", 4, 90, 40, 500)
print(camioneta)

bici = Bici("rosa", 2, "urbana")
print(bici)

print("\nlista de cada objeto:")
vehiculos = [coche, moto, camioneta, bici]
print(vehiculos)

print("""
      \nRealiza una función llamada catalogar() que reciba la lista de vehiculos y los 
recorra mostrando el nombre de su clase y sus atributos:
""")


def catalogar(vehiculos,ruedas=None):
    # Primera pasada, mostrar recuento
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))
    # Segnda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)


catalogar(vehiculos)


