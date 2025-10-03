class Perro:
    def __init__(self, nombre, variacion = None):
        self.nombre = nombre
        self.variacion = variacion or None
    
    def escribirPerro(self):
        if self.variacion is None:
            print('Tu perro es un: ' + self.nombre + ' y no tiene variación')
        else:
            print('Tu perro es un: ' + self.nombre + '\n de la variación: ' + self.variacion)
    
    def comprobarVariacion(self, variaciones):
        if len(variaciones) > 1:
            for i in variaciones:
                print(i)
            self.variacion = input('¿A cual de estas variaciones es tu perro?')
        elif len(variaciones) == 1:
            self.variacion = variaciones[0]
        else:
            print('Tu perro no tiene variaciones')