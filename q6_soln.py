# 
# Quiz 6 Solution
# COMP 1701 Winter 24
#

# Q 1
def enter_list(prompt:str) -> list:
    """ Enter a list of strings, ending with a null string. 
    return the list"""

    list_of_strings = []
    resp = input(prompt)
    while resp != "":
        list_of_strings.append(resp)
        resp = input(prompt)
    return list_of_strings

bird_list = enter_list("Enter a bird, <CR> to end: ")
print(bird_list)

# Q 2
animals = [["Grizzy Bear", "Black Bear"], 
    ["Hoary Marmot", "Golden Mantled Ground Squirrel", "Chipmunk"],
    ["Moose", "Elk", "White Tailed Deer", "Black Tailed Deer", "Bighorn Sheep"], 
    ["Raven", "Crow", "Magpie", "Gray Jay", "Clarks Nutcracker"],
    ["Chickadee"]] 

print(animals)

# a) 
["Chickadee"]

# b) 
print(animals[len(animals)-1])

# c)
print(animals[3][2])

# d) 
print(animals[2][len(animals[2])-1])

# e) 

for animal_list in animals:
    for animal in animal_list: 
        print( animal, end=" ")
    print()

# OR 

for i in range(0,len(animals)):
    for j in range(0,len(animals[i])):
        print( animals[i][j], end=" ")
    print()

