def sum_all() -> int:
    """
    Prompts the user to enter positive integers one at a time, then displays the
    number and the running total. Finishes when a negative number is entered.
    Returns the final total.
    """
    prompt = "Enter a positive integer to sum, or negative integer to finish: "
    number = int(input(prompt))  # the priming read
    total = 0

    while number >= 0:
        # number = int(input(prompt))  # the internal read
        print(f"You entered {number}")
        total = total + number
        print(f"The running sum is {total}")
        number = int(input(prompt))  # the internal read

    return total

### 1. Body of loop is all the indented lines after while number > 0
### 2. LCV = number. The value of number will determine when the loop stops. 
### 3. Terminating condition: not (number >= 0) <===> number < 0
### 4. Initial conditions. number is set to a user input value and total is set to 0
### 5. LCV update: number = int(input(prompt))  # the internal read

### To fix sum_all() move the internal read from the start of the loop body to the end. 

def main():
    total = sum_all()
    print(f"\nThe final sum is {total}")


main()
