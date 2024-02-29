# 
# 
# Counted Loop Example 
# 
# COMP 1701 
# Winter 2024
# A. Fedoruk 

# We are doing a counted loop, so we need to know 
# before hand how many times to execute the loop. 

n = int(input("Enter the number of times to loop: "))

# For a counted loop we need a loop counter. Typically we use i, j, k etc. 
# (There is a historical reason for this. FORTRAN variable names! Variables that 
# started with i-n were integers and all others were floats.)

# initialize the loop counter or Loop Control Variable (LCV)

i = 0 

# Now we have the while statement. The condition is the important part here. 
# if we start at 0 and go up by ones i = 0, 1, 2, 3, ... n-1 will be n iterations.

while i < n:
    print(f"Loop iteration {i}")
    # We always need to update the LCV in the loop otherwise loop will never end. 
    i = i + 1 



