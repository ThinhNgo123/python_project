def count(n = 0):
	while True:
		yield (yield n)
		n += 1

a = count()
next(a)
print(a.send(5), end="")
print(a.send("a"))