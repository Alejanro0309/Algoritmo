class Comida:
    def __init__(self,nombre,precio,cantidad,tipo) -> None:
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.tipo=tipo
    def show(self):
        print(f'Nombre:{self.nombre}\nPrecio:{self.precio}\nCantidad:{self.cantidad}\nTipo:{self.tipo}')

class Alimento(Comida):
    def __init__(self, nombre, precio, cantidad, tipo,fecha_caducidad) -> None:
        super().__init__(nombre, precio, cantidad, tipo)
        self.fecha_caducidad=fecha_caducidad
    def show(self):
        super().show()
        print(f'Fecha de caducidad:{self.fecha_caducidad}\n')
class Alimento_Comprado(Alimento):
    def __init__(self, nombre, precio, cantidad, tipo, fecha_caducidad,comprado) -> None:
        super().__init__(nombre, precio, cantidad, tipo, fecha_caducidad)
        self.comprado=comprado

class Bebida(Comida):
    def __init__(self, nombre, precio, cantidad, tipo,volumen,con_gas) -> None:
        super().__init__(nombre, precio, cantidad, tipo)
        self.volumen=volumen
        self.con_gas=con_gas
    def show(self):
        super().show()
        print(f'Volumen:{self.volumen}\nCon gas:{self.con_gas}\n')
class Bebidas_Comprados(Bebida):
    def __init__(self, nombre, precio, cantidad, tipo, volumen, con_gas,comprado) -> None:
        super().__init__(nombre, precio, cantidad, tipo, volumen, con_gas)
        self.comprado=comprado