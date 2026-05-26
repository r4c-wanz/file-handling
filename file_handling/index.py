import os

file_name = "fruits.txt"

def load_data():
  # If they do not have file called "fruits.txt"
  if not os.path.exists(file_name):
    return []
  # If they have file called "fruits.txt"
  with open(file_name, "r") as file:
    return [line.strip() for line in file.readlines()]

def save_data(data):
  with open(file_name, 'w') as file:
    for name in data:
      file.write(name + '\n')

def show():
  data = load_data()
  print("\n--- List of the Fruits ---")
  if not data:
    print("No fruit yet.")
  else:
    for i, fruit in enumerate(data, 1):
      print(f"{i}. {fruit}")

def add():
  name = input("Enter the fruit name want to add: ")
  data = load_data()
  data.append(name)
  save_data(data)
  print("Successfully added!")

def edit():
  data = load_data()
  show()
  if data:
    idx = int(input("\nSelect the number you want to change: ")) - 1
    if 0 <= idx < len(data):
      new_name = input("Enter the new name: ")
      data[idx] = new_name
      save_data(data)
      print("Successfully changed!")

def delete():
  data = load_data()
  show()
  if data:
    idx = int(input("\nSelect the number you want to delete: ")) - 1
    if 0 <= idx < len(data): # Security guard
      data.pop(idx)
      save_data(data)
      print("Successfully deleted!")

while True:
  print()
  print("--- Menu option ---")
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
