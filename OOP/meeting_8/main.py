# name1 = "Joe"
# age1 = 10
# hobby1 = "badminton"

# name2 = "Jane"
# age2 = 9
# hobby2 = "swimming"

# name3 = "Jane"
# age3 = 9
# hobby3 = "swimming"

# print("Hello", name1)
# print("Your age is", age1, "years old")
# print("Your hobby is", hobby1)

# print()

# print("Hello", name2)
# print("Your age is", age2, "years old")
# print("Your hobby is", hobby2)

# def sayHello(name):
#     print("Hello", name)

# def sayAge(age):
#     print("Your age is", age, "years old")

# def sayHobby(hobby):
#     print("Your hobby is", hobby)

# sayHello(name1)
# sayAge(age1)
# sayHobby(hobby1)

# print()

# sayHello(name2)
# sayAge(age2)
# sayHobby(hobby2)

class Hero:
    # Init method
    def __init__(guy, name, role):
        guy.name = name
        guy.role = role

    # Show method
    def showBiodata(guy):
        print(f"Name: {guy.names}")
        print(f"Role: {guy.roles}")

hero1 = Hero("Hawkeye", "Archer")
hero2 = Hero("Hulk", "Melee")

# hero1.name = "Hawkeye"
# hero1.role = "Archer"

# hero2.name = "Hulk"
# hero2.role = "Melee"

# print(hero1.name)

hero1.showBiodata()
