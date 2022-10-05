# example 1
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(3, 3))

# example 2
class Property:
	def __init__(self):
		print("Initialize")

	def __call__(self, func):
		def decorator(msg):
			print("-----------------")
			func(msg)
			print("-----------------")
		return decorator

property = Property()

@property
def message(msg):
	print(msg)

message("Hello world")