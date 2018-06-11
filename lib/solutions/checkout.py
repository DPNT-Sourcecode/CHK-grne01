

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	if isinstance(skus, str):
		cart = list(skus)
	else:
		cart = skus
		
	if skus is "" or isinstance(skus, int):
		return -1

	stock = {
		"A": 50,
		"B": 30,
		"C": 20,
		"D": 15
	}

	cart_value = 0
	
	# Check basket and group items (to check for offers)
	
	def deal(sku, count):
		if sku == "A":
			remainder = count % 3
			return (((count - remainder) / 3) * 130) + (remainder * 50)
		elif sku == "B":
			remainder = count % 2
			return (((count - remainder) / 2) * 45) + (remainder * 30)
		else:
			return False
			

	for k,v in stock.items():
		if k in cart:
			deal_value = deal(k, cart.count(k))
			if not deal_value:
				cart_value += skus.count(k) * v
			else:
				cart_value += deal_value

	return cart_value

