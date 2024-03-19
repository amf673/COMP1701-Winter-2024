# 
# Working with text files. 
# COMP 1701 
# A. Fedoruk 

# create a file object by open()ing a file for reading. 

input_file_name = input("Enter the file name to read: ")
input_file = open(input_file_name, "r") 

line = input_file.readline()    # read the first line
i = 0
while line != "":  # readline() returns a null string when the end of the file is reached. 
    i = i + 1 
    # strip off the newline
    nline = line.strip()
    print(f"{i}. {len(nline)} : {nline}")
    line = input_file.readline()    # read the next line

input_file.close() # tidy up.