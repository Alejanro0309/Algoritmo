from Clase_Comida import Comida,Bebida,Alimento,Alimento_Comprado,Bebidas_Comprados
from db import DB
from Clase_Registro import Registro
class APP:
    alimentos_obj=[]
    bebidas_obj=[]
    
    def star(self):
        self.constructor()
        productos_comprados=[]
        while True:
            print()
            opcion=input('Escribe que opcion deseas:\n1-Ver productos\n2-Comprar productos y Registrarte\n3-Ver factura\n4-Crear productos \n5-Salir\nopcion:')
            
            if opcion=='1':
                for alimentos in self.alimentos_obj:
                    alimentos.show()
                for bebidas in self.bebidas_obj:
                    bebidas.show()
            elif opcion=='2':
                persona=Registro()
                persona.registro()
                
                opcion2=input('Escribe el nombre del producto:')
                opcion3=input('Que cantidad desea de cada producto:')
                print()
                while not opcion3.isnumeric():
                    print('La cantidad no es un dato valido')
                    opcion3=input('Que cantidad desea de cada producto:')
                cantidad_compras=int(opcion3)
                for alimento in self.alimentos_obj:
                    if alimento.nombre==opcion2:
                        alimento_comprado=Alimento_Comprado(alimento.nombre,alimento.precio,alimento.cantidad,alimento.tipo,alimento.fecha_caducidad,cantidad_compras)
                        productos_comprados.append(alimento_comprado)
                        alimento.cantidad=alimento.cantidad-cantidad_compras
                for bebida in self.bebidas_obj:
                    if bebida.nombre==opcion2:
                        bebidas_comprados=Bebidas_Comprados(bebida.nombre,bebida.precio,bebida.cantidad,bebida.tipo,bebida.volumen,bebida.con_gas,cantidad_compras)
                        productos_comprados.append(bebidas_comprados)
                        bebida.cantidad=bebida.cantidad-cantidad_compras


                while len(productos_comprados)==0:
                    print('Dato invalido,no se encuentra el producto')
                    opcion2=input('Escribe el nombre del producto:')
                    for alimentos in self.alimentos_obj:
                        if alimentos.nombre==opcion2:
                            productos_comprados.append(alimentos)
                    for bebidas in self.bebidas_obj:
                        if bebidas.nombre==opcion2:
                            productos_comprados.append(bebidas)
                
            elif opcion=='3':
                persona.factura(productos_comprados,cantidad_compras)
            elif opcion=='4':
                break
                


                



    def constructor(self):
        #print(DB,'Base de datos')
        list_productos=DB
        #print(DB[0],'P')
        #print(list_productos)
        for produtos in list_productos:
            if produtos['tipo']=="alimento":
                self.alimentos_obj.append(Alimento(produtos["nombre"],produtos["precio"],produtos["cantidad"],produtos["tipo"],produtos["fecha_caducidad"]))
            else:
                self.bebidas_obj.append(Bebida(produtos["nombre"],produtos["precio"],produtos["cantidad"],produtos["tipo"],produtos['volumen'],produtos['con_gas']))
                                                   
        