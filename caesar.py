# 
# A simple Caesar cipher 
# 
# Encode a string by shifting letters by a key amount. 
# A. Fedoruk
# COMP 1701 W24

chars = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(len(chars))

N = int(input("Enter N: "))
phrase = input("Enter a phrase: ")
newphrase = ""

for ch in phrase:
    X = chars.index(ch)
    Y = X + N
    Z = Y % 27
    print( f"X = {X:4} Y = {Y:4} Z = {Z:4}")
    newphrase = newphrase + chars[Z]
    
print(newphrase)
    
