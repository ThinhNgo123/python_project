class Test(object):
	"""docstring for Test"""
	def __init__(self):
		super(Test, self).__init__()
		print("init: ", self)

	def __call__(self):
		print("Called: ", self)

	def __new__(cls):
		print(cls)
		return super().__new__(cls)

test = Test()
test()