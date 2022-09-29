def make_class(name):
    class Dog(object):
        def __init__(self, name):
            super().__init__()
            self.name = name

        def bark(self):
            print(self.name + "Bark!")

    return Dog(name)

def make_class_1():
    class Dog(object):
        def __init__(self, name):
            super().__init__()
            self.name = name

        def bark(self):
            print(self.name + "Bark!")

    return Dog

def make_class_2():
    class Dog(object):
        def __init__(self, dog):
            super().__init__()
            self.dog = dog

        def bark(self):
            print(self.dog.name + "Bark!")

    return Dog

make_class("Hulk").bark()
make_class_1()("Hulk").bark()
# print(make_class_2()(make_class_1()("Hulk")).bark)
make_class_2()(make_class_1()("Hulk")).bark()

            