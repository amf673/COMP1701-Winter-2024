# 
# Sentinel Loop Example 
# 
# COMP 1701 
# Winter 2024
# A. Fedoruk 

# We are doing a sentinel loop. In this case 
# we don't know how many times to execute the loop before hand. 
# We loop until some condition is true. 

# Let's input a list of positive numbers. When -1 is entered, stop. 
# This is known as a priming read. 

num = int(input("Enter a number, -1 to end: "))

# Now we have the while statement. Again the condition is the important part here. 
# In this case, if num is not -1 we want to continue the loop. 

while num != -1:
    print(f"num = {num}")
    # We always need to update the LCV in the loop otherwise loop will never end. 
    num = int(input("Enter a number, -1 to end: "))






