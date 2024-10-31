class Person:
    def __init__(self, name, age, hight="normal"):
        self.name = name
        self.age = age
        self.hight = hight

bonney = Person('Anne', 25, 'short')
rackham = Person('John', 25)

print(rackham.hight)
print(bonney.hight)