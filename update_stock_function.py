def update_stock(product, units_sol):
    stock_previo = product["current_stock"]
    product["current_stock"] -= units_sol
    return print(f"El stock previo de {product['name']} era {stock_previo} y el stock final es {product['current_stock']}.")

for order in orders:
    order_id = order["order_id"]
    items = order["items"]
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
        update_stock(product, quantity)
  #      product["current_stock"] -= quantity
       total += product["price"] * quantity
    print(f"Order ID: {order_id} - Total: ${total:.2f} - Purchase Completed")
