def test1():
    return print(f"Test")

class Mortgage:

    def __init__(self, quantity, monthly_salary, age):
        self.quantity = quantity
        self.monthly_salary = monthly_salary
        self.age = age
        self.__is_ok = False
        self._calculate()

    def _calculate(self):
        self.__is_ok = self.quantity < 100000

    def increase_quantity(self, quantity_to_add):
        self.quantity += quantity_to_add
        self._calculate()

    def imprimir_resultado(self):
        if self.__is_ok:
            print("Enhorabuena!! Concedida!!")
        else:
            print("Lo sentimos...")

def test2():
    return "Hola", "Adios"

def main():
    _, b = test2()
    print(b)
    print(_)

    c = test1()
    print(c)

    # Aprovechar que Python admite ambos tipos de comillas:
    d = {
        "clave": "Hola"
    }
    my_str = f"¡¡{d.get("clave")}!!"
    print(my_str)

    my_list = [1,2,3]
    my_list_por_dos = map(lambda x: 2*x, my_list)
    print(list(my_list_por_dos))

    # Clase hipoteca:
    my_hipoteca = Mortgage(50000, 2000, 30)
    my_hipoteca.imprimir_resultado()
    my_hipoteca.increase_quantity(100000)
    my_hipoteca._calculate()
    my_hipoteca.imprimir_resultado()

if __name__ == "__main__":
    main()
