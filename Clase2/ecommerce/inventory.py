
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.sku not in self.products:
            self.products[product.sku] = product

    def remove_product(self, sku):
        if sku in self.products:
            del self.products[sku]

    def get_product(self, sku):
        return self.products.get(sku)

    def list_products(self):
        return list(self.products.values())

    def find_by_name(self, name):
        return [p for p in self.products.values() if name.lower() in p.name.lower()]

    def get_total_inventory_value(self):
        return sum(p.calculate_total_value_in_stock() for p in self.products.values())

    def generate_inventory_report(self):
        report = [p.get_info() for p in self.products.values()]
        return '\n'.join(report)

    def __repr__(self):
        return f"Inventory({len(self.products)} products)"
