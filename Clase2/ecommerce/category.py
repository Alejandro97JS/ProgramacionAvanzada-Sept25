class Category:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description or ''

    def __repr__(self):
        return f"Category(name='{self.name}', description='{self.description}')"
    
    def __str__(self):
        return self.name
