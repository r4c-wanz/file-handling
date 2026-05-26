class Person:
    # function is method
    # init method
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    # pass

p1 = Person("Emil", 10, "Jakarta")
# p1.name = "Emil"
# p1.age = 10
# p2 = Person("Aaron")
# p2.name = "Aaron"
# p3 = Person("John")
# p3.name = "John"
# p4 = Person()

# we acces the object
print(f"My name is {p1.name}. Im {p1.age} years old. Img from {p1.city}")
