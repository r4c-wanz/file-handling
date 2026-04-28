import os

fruits = []

def show():
  print(fruits)

def add():
  new_fruit = input("Enter the fruit name want to add: ")
  fruits.append(new_fruit)
  if not os.path.exists("fruits.txt"):
    open("fruits.txt", "x")
    f.write(new_fruit + "\n")
  else:
    with open("fruits.txt", "a") as f:
      f.write(new_fruit + "\n")

def edit():
  new_fruit = input("Enter the new fruit: ")
  index = int(input("Enter the index want to edit: "))
  fruits[index] = new_fruit

def delete():
  index = int(input("Enter the index want to delete: "))
  fruits.pop(index)

while True:
  print("1. Show")
  print("2. Add")
  print("3. Edit")
  print("4. Delete")
  print("5. Exit")
  option = int(input("Enter the number of menu: "))

  if option == 5:
    break
  elif option == 1:
    show()
  elif option == 2:
    add()
  elif option == 3:
    edit()
  elif option == 4:
    delete()
