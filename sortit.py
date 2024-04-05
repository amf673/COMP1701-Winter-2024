# 
# Example from last day of class 
# 
# 
# This program will read a list of number and put them in order using a technique called 'Bubble Sort'. 
# 
# 

def get_user_input () -> list[int]:
    """ Prompt the user for a list of integers separated by 
    whitespace. Return those integers as a list of ints. 
    """
    list_ints_str = input("enter list if int ")
    list_ints = list_ints_str.split("")
    int_list = []
    for num in list_ints:
        int_list.append(int(num))

    return int_list


def swap(nums: list[int], pos1: int, pos2: int) -> None:
    """ In the list nums swap the value from pos1 with the 
    value from pos2.
    """
    temp = nums[pos1]
    nums[pos1] = nums[pos2]
    nums[pos2] = temp


def loop_and_swap (nums: list[int]) -> bool:
    """ Go through the list nums. Compare adjacent 
    values and if they are out of order, call swap 
    to swap them. If a swap occurs, return True, else 
    return False. 
    """
    swapped = False
    for i in range(0, len(nums) - 1): 
        if nums[i] > nums[i+1]:
            swap(nums, i, i+1)
            swapped = True
    return swapped 


def process(nums: list[int]) -> None:
    """ Call loop_and_swap() until no swaps occur, 
    which means the list is in order. 
    """
    swapped = loop_and_swap(nums)
    while swapped: 
        swapped = loop_and_swap(nums)
    

def main () -> None:
    nums = get_user_input ()
    print("Before processing :", nums)
    process(nums)
    print("After processing :", nums)

main()
