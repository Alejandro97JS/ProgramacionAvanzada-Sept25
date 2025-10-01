# Versión hecha durante la clase, colaborativamente.

def check_stock_for_product(product_sku, requested_units: int, inventory):
    current_product = inventory.get(product_sku) # Buscar el producto por SKU
    if current_product is None:
        return False, 0
    # No hay suficientes productos
    if current_product.get("current_stock") < requested_units:
        return False, current_product.get("current_stock")
    return True, current_product.get("current_stock")

def show_inventory(inventory):
    # Mostrar estado final del inventario
    print("\nInventory Report:\n")
    for product in inventory.values():
        category_names = ", ".join([cat["name"] for cat in product["categories"]]) or "None"
        tag_names = ", ".join([tag["name"] for tag in product["tags"]]) or "None"
        print(f"Product: {product['name']} - Price: ${product['price']:.2f}, Stock: {product['current_stock']}, Categories: [{category_names}], Tags: [{tag_names}]")
    
def update_stock(product_sku, units_sol, inventory):
    product = inventory.get(product_sku)
    stock_previo = product["current_stock"]
    product["current_stock"] -= units_sol
    print(f"El stock previo de {product['name']} era {stock_previo} y el stock final es {product['current_stock']}.")
    return product

def process_orders(orders):
    for order in orders:
        order_id = order["order_id"]
        items = order["items"]
        total = 0
        for sku, quantity in items.items():
            stock, _ = check_stock_for_product(sku, quantity, inventory)
            if not stock:
                print("Error con la cantidad del producto. Lo siento")
                continue
            # Actualizar el stock
            product_stock_updated = update_stock(sku, quantity, inventory)
            total += product_stock_updated["price"] * quantity # type: ignore
        print(f"Order ID: {order_id} - Total: ${total:.2f} - Purchase Completed")

# Gestión de categorías
categories = [
    {"name": "Electronics", "description": "Devices and gadgets"},
    {"name": "Office", "description": "Office supplies and equipment"}
]

# Gestión de etiquetas (tags)
tags = [
    {"name": "On Sale"},
    {"name": "New Arrival"},
    {"name": "Best Seller"}
]

# Gestión de productos
products = [
    {"name": "Laptop", "sku": "SKU123", "price": 1200, "current_stock": 10, "categories": [categories[0]], "tags": [tags[1], tags[2]]},
    {"name": "Mouse", "sku": "SKU456", "price": 25, "current_stock": 100, "categories": [categories[0]], "tags": [tags[0]]},
    {"name": "Keyboard", "sku": "SKU789", "price": 50, "current_stock": 50, "categories": [categories[1]], "tags": [tags[2]]},
    {"name": "Monitor", "sku": "SKU101", "price": 300, "current_stock": 20, "categories": [categories[0]], "tags": []}
]

# Gestión del inventario
inventory = {product["sku"]: product for product in products}

# Procesar pedidos
orders_morning = [
    {"order_id": "ORDER001", "items": {"SKU123": 2, "SKU456": 5}},
    {"order_id": "ORDER002", "items": {"SKU789": 3, "SKU101": 1}},
    {"order_id": "ORDER003", "items": {"SKU456": 10, "SKU101": 2}}
]

orders_afternoon = [
    {"order_id": "ORDER001", "items": {"SKU123": 2, "SKU456": 5}}
]

# Procesar pedidos:
process_orders(orders_morning)
process_orders(orders_afternoon)

# Mostrar estado final del inventario
show_inventory(inventory)


# Un proceso automático para comprobar qué tengo que comprar.
# Considero que tengo que comprar cuando tengo < 5 unidades.
for product_sku in inventory.keys():
    tengo_suficiente, cantidad = check_stock_for_product(product_sku, 5, inventory)
    if not tengo_suficiente:
        print(f"HAY QUE ENCARGAR MÁS PRODUCTOS {product_sku} porque quedan solo {cantidad}")
    else:
        print(f"Del producto {product_sku} hay de sobra: {cantidad}")
