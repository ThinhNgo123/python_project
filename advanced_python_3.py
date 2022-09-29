# x = [i**2 for i in range(10000000000)]

# for el in x:
#     print(el)

class Generate:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last
        self.last += 1
        return rv

g = Generate(10000)

while True:
    try:
        print(next(g))
    except StopIteration:
        break
        
import sys
print(sys.getsizeof(g))