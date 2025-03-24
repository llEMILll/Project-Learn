class vehiculo:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        pass
    def tipo_vehiculo(self):
        print('Tipo de auto: Coche')


    def mostrar_informacion(self):
        print('Información de Auto: ')
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')
    

class moto(vehiculo):


    def tipo_vehiculo(self):
        print('Tipo de auto: Moto')
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
    

auto1=vehiculo('Chevrolet', 'Grand Vitara')
moto1=moto('Susuki', 'Yamaha')

auto1.mostrar_informacion()

moto1.mostrar_informacion()