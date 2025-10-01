from .product import Product

class Order:
    def __init__(self, order_id, products=None):
        self.order_id = order_id
        self.products = products or {}

    def add_product(self, product:Product, quantity):
        if product.sku in self.products:
            self.products[product.sku]['quantity'] += quantity
        else:
            self.products[product.sku] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_sku):
        if product_sku in self.products:
            del self.products[product_sku]

    def calculate_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.products.values())

    def get_order_summary(self):
        lines = [f"{item['product'].name} (x{item['quantity']}) - ${item['product'].price * item['quantity']:.2f}" for item in self.products.values()]
        return f"Order ID: {self.order_id}\n" + '\n'.join(lines) + f"\nTotal: ${self.calculate_total():.2f}"

    def buy(self):
        total = self.calculate_total()
        for _, item in self.products.items():
            product = item['product']
            quantity = item['quantity']
            if product.current_stock < quantity:
                raise ValueError(f"Insufficient stock for {product.name}. Available: {product.current_stock}, Requested: {quantity}")
            product.update_stock(-quantity)
        return f"Order ID: {self.order_id} - Total: ${total:.2f} - Purchase Completed"

    def __repr__(self):
        return f"Order(order_id='{self.order_id}', total_items={len(self.products)})"
