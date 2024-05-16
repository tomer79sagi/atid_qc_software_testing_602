class Product:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity

class ShoppingCart:
	def __init__(self):
		self.items = []
	def add_item(self, product, quantity):
		self.items.append((product, quantity))

	def get_product_count(self):
		return len(self.items)

	def get_total(self):
		total = 0
		for product, quantity in self.items:
			total += product.price * quantity
		return total

if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item(Product('Book', 99, 55), 2)
