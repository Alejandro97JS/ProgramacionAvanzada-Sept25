
class Product:
    def __init__(self, name, sku, price, current_stock=0, categories=None, tags=None):
        self.name = name
        self.sku = sku
        self.price = price
        self.current_stock = current_stock
        self.categories = categories or []
        self.tags = tags or []
        self.price_history = [(price, 'Initial Price')]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def remove_category(self, category):
        if category in self.categories:
            self.categories.remove(category)

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def update_stock(self, amount):
        self.current_stock += amount

    def is_in_stock(self):
        return self.current_stock > 0

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)
        self.price_history.append((self.price, f"Discount applied: {percentage}%"))

    def calculate_total_value_in_stock(self):
        return self.price * self.current_stock

    def get_info(self):
        categories = ', '.join([cat.name for cat in self.categories]) or 'NO HAY'
        tags = ', '.join([tag.name for tag in self.tags]) or 'None'
        return f"Product: {self.name} (SKU: {self.sku}) - Price: ${self.price:.2f}, Stock: {self.current_stock}, Categories: {categories}, Tags: [{tags}]"

    def __repr__(self):
        return f"Product(name='{self.name}', sku='{self.sku}', price={self.price}, current_stock={self.current_stock})"
