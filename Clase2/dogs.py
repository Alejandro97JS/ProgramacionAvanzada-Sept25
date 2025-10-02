import requests
from Perro import Perro

url = "https://dog.ceo/api/breeds/list/all"

response = requests.get(url)
response.raise_for_status() 

data = response.json()
raza = list(data["message"].keys())
print(raza)
seguir = True

while seguir:
    nombre = input('Escribe el nombre de una raza: ')
    while nombre not in raza:
        print('Esta raza no existe')
        print('Vuelve a probar')
        nombre = input('Escribe el nombre de una raza: ')

    variaciones = data["message"][nombre]

    perro1 = Perro(nombre, variaciones)

    perro1.comprobarVariacion(variaciones)

    perro1.escribirPerro()
    
    seg = input('¿Quieres seguir? 1-Si 2-no')
    if seg == '2':
        seguir = False