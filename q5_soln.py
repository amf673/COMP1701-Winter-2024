
# Quiz 5 
# COMP 1701 
# A. Fedoruk
# 
# Rewrite this for loop as a while. 

a = [2, 4, 5, 8]
sum = 0
for j in range(1, len(a)): 
    sum = sum + a[j]

print(sum, sum/len(a))

## 
# 
# This is a counted loop. We know how many 
# iterations there will be, len(a). So we set up a counter
# j and initialize it to 1. We also need to accumulate the 
# sum so we intialize that to 0
j = 1
sum = 0 
# The for loop runs from 1 to len(a)-1 So we set up the 
# while to to that. 
while j < len(a):
    # update the accumulator same as the for loop
    sum = sum + a[j]
    # update the counter. 
    j = j + 1

print(sum, sum/len(a))
