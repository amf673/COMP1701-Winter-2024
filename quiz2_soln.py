# Quiz 2 
# 
# COMP 1701  Quiz 2
# A. Fedoruk
# 

# Q1 
num = 12163.687546
print (f'{num:20,.2f}')

# Q2

SEC_PER_MIN = 60 
MIN_PER_HOUR = 60
SEC_PER_HOUR = SEC_PER_MIN * MIN_PER_HOUR

input_seconds = int(input("Enter the number of seconds: "))

decimal_hours = input_seconds / SEC_PER_HOUR 

hours = input_seconds // SEC_PER_HOUR
remaining_seconds = input_seconds % SEC_PER_HOUR
minutes = remaining_seconds // SEC_PER_MIN
seconds = remaining_seconds % SEC_PER_MIN

print(f"{seconds} seconds is {decimal_hours:.2f}", end="")
print(f" hours, or {hours} hours, {minutes} minutes and {seconds} seconds", end="")
print(f" or more concisely {hours:02}:{minutes:02}:{seconds:02}")
