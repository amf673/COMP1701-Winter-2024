# 
# Working with text files
# WRiting a file 
# COMP 1701 
# A. Fedoruk 

# create a file object by open()ing a file for writing. 

output_file_name = input("Enter the file name to write: ")
output_file = open(output_file_name, "w") 
i = 0
line = input("Enter a line to save to the file: ")
while line != "":  # readline() returns a null string when the end of the file is reached. 
    i = i + 1
    output_file.write(f"{i}. {len(line)} : {line}\n")
    line = input("Enter a line to save to the file: ")   # read the next line

output_file.close() # tidy up.