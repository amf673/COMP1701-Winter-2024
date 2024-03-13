# Lists


a = ["Calgary", "Edmonton", "Red Deer", "Lethbridge", "Medicine Hat", "Airdrie", "Coleman", "Fort MacMurray"]
b = [1300000, 1000000, 100000, 90000, 80000, 50000, 10000, 30000]

print(a)

# indexing

print( a[0])
l = len(a)
print(a[l-1])

# sorting a list
a.sort()
print(a)

# adding to a list 
new_city = input("Enter a city: ")
a.append(new_city)

a.remove("Lethbridge")
print(a)
city = a.pop(3)
print(city)
print(a)

new_city = input("Enter a city: ")
if new_city in a: 
    print(new_city, "is in the list")
    print(new_city, "Is the ", a.index(new_city), "Element")
