class Registro:
    def registro(self):
        self.nombre=input('Escribe tu nombre:')
        while not self.nombre.isalpha():
            print('Dato invalido')
            self.nombre=input('Escribe tu nombre:')

        self.apellido=input('Escribe tu apellido:')
        while not self.apellido.isalpha():
            print('Dato invalido')
            self.apellido=input('Escribe tu apellido:')
        self.cedula=input('Escribe tu cedula:')
        while not self.cedula.isnumeric():
            print('Dato invalido')
            self.cedula=input('Escribe tu cedula:')
        print('Registro exitoso')



    def factura(self,producto_comprados,cantidad):
            precio_total=0
            print(f'Nombre:{self.nombre} Apellido:{self.apellido} Cedula:{self.cedula}')
            for producto in producto_comprados:
                print(f'{cantidad} x {producto.nombre} {producto.precio}')
                precio_total+=int(cantidad)*(producto.precio)
            print('--------------------------------------------------')
            print(precio_total,'$')