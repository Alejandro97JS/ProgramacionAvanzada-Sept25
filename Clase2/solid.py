# S: Single Responsibility Principle (SRP)
# Cada clase debe tener una única responsabilidad.
class FileManager:
    """
    Clase base genérica para manejar archivos.
    SRP: Su única responsabilidad es definir el comportamiento genérico para managers de archivos.
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        """
        Lectura genérica de archivo como texto.
        Puede ser sobrescrita por subclases.
        """
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def write(self, data):
        """
        Escritura genérica de archivo como texto.
        Puede ser sobrescrita por subclases.
        """
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(str(data))

class TextFileManager(FileManager):
    """
    Maneja archivos de texto (.txt).
    """
    def read(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return str(f.read())

    def write(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(str(data))

class CSVFileManager(FileManager):
    """
    Maneja archivos CSV (.csv).
    """
    def read(self):
        import csv
        with open(self.filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)

    def write(self, data):
        import csv
        with open(self.filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            
    def file_to_excel(self, data):
        import pandas as pd
        df = pd.DataFrame(data)
        df.to_excel("output.xlsx", index=False)

# I: Interface Segregation Principle (ISP)
# Los clientes no deben depender de interfaces que no usan.
# Aquí, si se requieren funcionalidades adicionales, se pueden crear interfaces específicas.
from abc import ABC, abstractmethod
class Showable(ABC):
    @abstractmethod
    def show(self):
        pass

class ImageFileManager(FileManager, Showable):
    """
    Maneja archivos de imagen (.png, .jpg).
    ISP: Implementa solo las interfaces necesarias.
    """
    def read(self):
        from PIL import Image
        return Image.open(self.filepath)

    def write(self, image, format=None):
        """
        Guarda una imagen usando PIL.
        :param image: Objeto PIL.Image a guardar.
        :param format: Formato opcional (por ejemplo, 'PNG', 'JPEG').
        """
        if format:
            image.save(self.filepath, format=format)
        else:
            image.save(self.filepath)

    def show(self):
        from PIL import Image
        img = Image.open(self.filepath)
        img.show()

# D: Dependency Inversion Principle (DIP)
# Las clases deben depender de abstracciones, no de implementaciones concretas.
class FileAnalyzer:
    """
    Puede usar cualquier FileManager.
    DIP: Depende de la abstracción FileManager, no de una implementación concreta.
    """
    def __init__(self, manager: FileManager):
        self.manager = manager

    def analyze(self):
        data = self.manager.read()
        # Aquí se podría hacer algún análisis genérico
        print(f"Analizando archivo: {self.manager.filepath}")
        return data
