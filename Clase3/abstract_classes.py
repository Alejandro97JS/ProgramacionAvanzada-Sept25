from abc import ABC, abstractmethod

class Animal(ABC):
	def __init__(self, nombre):
		self.nombre = nombre
	
	@abstractmethod
	def hacer_sonido(self):
		"""Método abstracto que debe ser implementado por las subclases"""
		raise NotImplementedError("Subclase debe implementar este método")

	def describir(self):
		"""Método normal que puede ser usado o sobrescrito por subclases"""
		return f"Soy un animal llamado {self.nombre}."

# Subclase concreta que implementa el método abstracto
class Perro(Animal):
	def hacer_sonido(self):
		return "Guau!"

	def describir(self):
		base = super().describir()
		return f"{base} Soy un perro."

# Ejemplo de uso
if __name__ == "__main__":
	mi_perro = Perro("Firulais")
	mi_perro.hacer_sonido()
	print(mi_perro.describir())
	print(f"Sonido: {mi_perro.hacer_sonido()}")
