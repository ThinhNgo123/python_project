def count(n = 0):
	while True:
		yield (yield n)
		n += 1

a = count()
next(a)
print(a.send(5))
print(next(a))
print(a.send("a"))
print(next(a))
print(next(a))
print(next(a))
