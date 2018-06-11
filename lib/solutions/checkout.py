

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	stock = {
		"A": 50,
		"B": 30,
		"C": 20,
		"D": 15
	}

	cart_value = 0
	cart = list(skus)
	# Check basket and group items (to check for offers)
	for k,v in stock.items():
		if k in skus:
			cart_value += skus.count(k) * v

	return cart_value

print checkout("AA")