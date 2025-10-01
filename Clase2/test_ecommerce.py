from ecommerce import Category, Product, Inventory, Order

if __name__ == "__main__":
    # Crear inventario
    inventory = Inventory()

    my_category = Category("Electrónica")

    # Crear productos
    p1 = Product("Laptop", "SKU123", 1200, 10, categories=[my_category])
    p2 = Product("Mouse", "SKU456", 25, 100)
    p3 = Product("Keyboard", "SKU789", 50, 50)
    p4 = Product("Monitor", "SKU101", 300, 20)

    # Añadir productos al inventario
    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)
    inventory.add_product(p4)

    # Crear pedidos
    order1 = Order("ORDER001")
    order1.add_product(p1, 2)
    order1.add_product(p2, 5)

    order2 = Order("ORDER002")
    order2.add_product(p3, 3)
    order2.add_product(p4, 1)

    order3 = Order("ORDER003")
    order3.add_product(p2, 10)
    order3.add_product(p4, 2)
    print(order3.get_order_summary())

    # Procesar compras
    print(order1.buy())
    print(order2.buy())
    print(order3.buy())

    # Mostrar estado final del inventario
    print("\nInventory Report:\n")
    print(inventory.generate_inventory_report())
