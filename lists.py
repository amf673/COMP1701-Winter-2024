# 
# Lists
# COMP 1701 
# A. Fedoruk

# Some examples of working with lists. 

cities = ["Calgary", "Edmonton", "Red Deer", 
          "Lethbridge", "Medicine Hat", "Airdrie", 
          "Coleman", "Fort MacMurray", "Edson"]

print(cities)

# 1. Indexing
#
# Lists are indexed from 0 to n-1. 
# To find out how many items are in a list, use len()

number_of_cities = len(cities)
print(f"There are {number_of_cities} cities in the list")

# To access individual members of the list use the index [i]

city = cities[0] # the first city 
city2 = cities[number_of_cities - 1] # the last city

# Iterating through the list of cities 

for i in range(0, len(cities)):
    print(cities[i])

# 2. Adding and deleting from lists

# .append() adds an item to the end of the list. 

new_city = input("Enter a city: ")
cities.append(new_city)
print(cities)

# .remove() will remove an item from the list. 

remove_city = input("Enter city to remove: ")
cities.remove(remove_city)

# 3. List membership 
# You can use the in keyword 

city_to_find = input("Enter a city: ")
if city_to_find in cities: 
    print("The city is in the list.")
else: 
    print("Not found.")

# 4. sorting a list
# Python provides a sort method. 

cities.sort()
print(cities)
