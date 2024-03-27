#
#  Searching for items in a list

a_list = ["Cat", "Dog", "Capybara", "Ferret", "Hamster", "Rabbit"]

animal = input("Enter an animal to find: ")

if animal.capitalize() in a_list: 
    i = a_list.index(animal.capitalize())
    print(animal, "is in the list at position", i)
else:
    print(animal, "is not in the list")
