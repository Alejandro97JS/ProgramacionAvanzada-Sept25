def check_stock_for_product(product, requested_units):
    pass
def  update_stock(product, quantity):
    pass

def process_orders(orders):
    for order in orders:    
        order_id = order["order_id"]
        items = order["items"]
        total = 0
        for sku, quantity in items.items():
            stock,_ = check_stock_for_product(sku, quantity)
            # Actualizar el stock
            if stock:
                update_stock(sku, quantity)
            else :
                print(f"Error: Insufficient stock for {product['name']}. Available: {product['current_stock']}, Requested: {quantity}")
            total += product["price"] * quantity
        print(f"Order ID: {order_id} - Total: ${total:.2f} - Purchase Completed")
    