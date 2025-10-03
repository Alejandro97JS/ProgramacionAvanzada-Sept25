import requests
import json

def buscar_libros_por_autor(nombre_autor, limite=5):
    params = {
        "author": nombre_autor,
        "limit": limite
    }
    response = requests.get("https://openlibrary.org/search.json?", params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Número de libros encontrados de {nombre_autor}: {data['numFound']} se muestran a continuación {limite}:" )
        for book in data["docs"][:limite]:
            print(f"Título: {book['title']} - Autor: {book['author_name']} - Año de Publicación: {book['first_publish_year']}")
    else:
        print(f"Error: {response.status_code}")


def guardar_libros_por_autor(nombre_autor):
    params = {
        "author": nombre_autor
    }
    response = requests.get("https://openlibrary.org/search.json?", params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Número de libros guardados del {nombre_autor}: {data['numFound']}" )

    else:
        print(f"Error: {response.status_code}")

    with open("response_book.json", mode="w", encoding="utf-8") as f_out:
        json.dump(data, f_out, indent=3)

if __name__ == "__main__":
    buscar_libros_por_autor("tolkien")
    guardar_libros_por_autor("tolkien")