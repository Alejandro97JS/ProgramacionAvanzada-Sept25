import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. Crear un producto
product_data = {
    "name": "Producto de prueba 2",
    "description": "Descripción de prueba",
    "unit_price_cents": 1050,
    "stock": 100
}
response = requests.post(f"{BASE_URL}/products/", json=product_data)
print("Crear producto:", response.status_code, response.json())
assert response.status_code in [200, 201]
product_id = response.json().get("id")

# 2. Editar el producto
update_data = {
    "name": "Producto editado",
    "description": "Descripción editada",
    "unit_price_cents": 1200,
    "category_id": 1
}
response = requests.patch(f"{BASE_URL}/products/{product_id}", json=update_data)
print("Editar producto:", response.status_code, response.json())
assert response.status_code == 200

# 3. Crear una categoría
category_data = {
    "name": "Categoría de prueba",
    "description": "Descripción categoría",
    "is_promoted": True
}
response = requests.post(f"{BASE_URL}/categories/", json=category_data)
print("Crear categoría:", response.status_code, response.json())
assert response.status_code in [200, 201]
category_id = response.json().get("id")

# 4. Editar la categoría
update_category = {
    "name": "Categoría editada",
    "description": "Descripción editada"
}
response = requests.patch(f"{BASE_URL}/categories/{category_id}", json=update_category)
print("Editar categoría:", response.status_code)
assert response.status_code == 200

# 5. Enlazar producto y categoría
response = requests.patch(f"{BASE_URL}/products/{product_id}/category/{category_id}")
print("Enlazar producto y categoría:", response.status_code, response.json())
assert response.status_code == 200

# 6. Obtener la categoría de un producto
response = requests.get(f"{BASE_URL}/products/{product_id}/category")
print("Obtener categoría del producto:", response.status_code, response.json())
assert response.status_code == 200

print("Todas las pruebas pasaron correctamente.")
