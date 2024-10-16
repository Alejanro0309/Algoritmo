class Transporte:
    def __init__(self,color,marca,modelo,años) -> None:
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.años=años
class Carro(Transporte):
    def __init__(self, color, marca, modelo, años,puertas) -> None:
        super().__init__(color, marca, modelo, años)
        self.puertas=puertas
    def show_attr(self):
        return "Color: {}, Marca: {}, Modelo: {}, Año: {}, Puertas: {}".format(self.color,self.marca,self.modelo,self.años,self.puertas)
class Avion(Transporte):
    def __init__(self, color, marca, modelo, años,alas,aerolinea) -> None:
        super().__init__(color, marca, modelo, años)
        self.alas=alas
        self.aerolinea=aerolinea
    def show_attr(self):
        return "Color: {}, Marca: {}, Modelo: {}, Año: {}, Alas: {}, Aerolinea: {}".format(self.color,self.marca,self.modelo,self.años,self.alas,self.aerolinea)

class Barco(Transporte):
    def __init__(self, color, marca, modelo, años, peso,puerto_salida) -> None:
        super().__init__(color, marca, modelo, años)
        self.peso=peso
        self.puerto_salida=puerto_salida
    def show_attr(self):
        return "Color: {}, Marca: {}, Modelo: {}, Año: {}, Peso: {}Tn, Puerto: {}".format(self.color,self.marca,self.modelo,self.años,self.peso,self.puerto_salida)


corolla=Carro('Rojo','Toyota','Corolla',2011,4)
yaris=Carro('Blanco','Toyota','Yaris',2024,2)
print('Carros\n')
print(corolla.show_attr())
print(yaris.show_attr())

boeing=Avion('Blanco','Boeing',735,2018,2,'Conviasa')
challenger=Avion('Negro','Challenger',350,2024,2,'Laser')
print('\nAvion\n')
print(boeing.show_attr())
print(challenger.show_attr())

monterey=Barco('Blanco','Monterey','238SS',2024,27,'Monaco')
cranchi=Barco('Gris','Cranchi','Zaffiro 34',2007,36,'Puerto la cruz')
print('\nBarco\n')
print(monterey.show_attr())
print(cranchi.show_attr())