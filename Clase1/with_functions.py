# Versión de ejemplo para programación modular con funciones

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

# Función para generar reportes de inventario
def generate_inventory_report(inventory):
    report_lines = []
    for product in inventory.values():
        category_names = ", ".join([cat["name"] for cat in product["categories"]]) or "None"
        tag_names = ", ".join([tag["name"] for tag in product["tags"]]) or "None"
        line = f"Product: {product['name']} (SKU: {product['sku']}) - Price: ${product['price']:.2f}, Stock: {product['current_stock']}, Categories: [{category_names}], Tags: [{tag_names}]"
        report_lines.append(line)
    return "\n".join(report_lines)

# Función para procesar pedidos
def process_order(order_id, items, inventory):
    total = 0
    for sku, quantity in items.items():
        product = inventory.get(sku)
        if not product:
            print(f"Error: Product with SKU {sku} not found.")
            continue
        if product["current_stock"] < quantity:
            print(f"Error: Insufficient stock for {product['name']}. Available: {product['current_stock']}, Requested: {quantity}")
            continue
        # Actualizar el stock
        product["current_stock"] -= quantity
        total += product["price"] * quantity
    print(f"Order ID: {order_id} - Total: ${total:.2f} - Purchase Completed")

# Crear y procesar pedidos
orders = [
    {"order_id": "ORDER001", "items": {"SKU123": 2, "SKU456": 5}},
    {"order_id": "ORDER002", "items": {"SKU789": 3, "SKU101": 1}},
    {"order_id": "ORDER003", "items": {"SKU456": 10, "SKU101": 2}}
]

for order in orders:
    process_order(order["order_id"], order["items"], inventory)

# Mostrar estado final del inventario
print("\nInventory Report:\n")
print(generate_inventory_report(inventory))
