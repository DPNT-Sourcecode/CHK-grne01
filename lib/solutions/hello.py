

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(string):
	if not isinstance(string, str):
		raise TypeError("Argument must be a string.")
	return "Hello, {}!".format(string)
