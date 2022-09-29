class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value
        print(a)
        return type(class_name, bases, a)
        
class Dog(metaclass=Meta):
    x = 5
    y = 8

    def bark(self):
        return "Gau!"

# d = Dog()
# print(d.BARK())
# print(Dog.mro())