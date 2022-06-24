from pickle import *
class carro:
    
    def __init__(self, nombre, tipo, marca, color):
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.color = color

    def __str__(self):
         return self.nombre+' '+self.tipo +' '+self.marca+' '+self.color


carro1 = carro('Corolla', 'Sedán','Toyota', 'Dorado')
f = open ('fileCars.txt', 'w+b')
dump(carro1, f)
f.seek(0)
carro1 = load(f)
f.close()
print (carro1)


