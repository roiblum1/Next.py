"""
This function reads a text file named 'names.txt' and returns the longest name in the file.

:param None: This function does not take any parameters.
:return: The longest name in the 'names.txt' file.
"""
def longest_name():
    with open('names.txt', 'r') as f:
        print(max(f.readlines(), key=len).strip())

"""
This function calculates and prints the sum of the lengths of all names in the 'names.txt' file.

:param None: This function does not take any parameters.
:return: The sum of the lengths of all names in the 'names.txt' file.
"""
def sum_length():
    with open('names.txt', 'r') as f:
        print(sum(len(name.strip()) for name in f.readlines()))
  
"""
This function prints the shortest names in the 'names.txt' file.

:param None: This function does not take any parameters.
:return: None. This function prints the shortest names to the console.
"""        
def shortest_names(): 
    with open('names.txt', 'r') as f:
        names = f.readlines()
        [print(name.strip()) for name in names if len(name.strip()) == min(len(name.strip()) for name in names)]

"""
This function writes the length of each name in the 'names.txt' file to a new file named 'names_length.txt'.

:param None: This function does not take any parameters.
:return: None. This function writes the lengths of the names to a new file.
"""
def names_length_file():
    with open('names.txt', 'r') as f:
        with open('names_length.txt', 'w') as f2:
            f2.writelines([str(len(name.strip()))+"\n" for name in f.readlines()])

"""
This function allows the user to input a desired length of a name and then prints out all the names in the 'names.txt' file that have that length.

:param None: This function does not take any parameters.
:return: None. This function prints the names to the console.
"""
def find_num():
    with open('names.txt', 'r') as f:
        length = int(input("Enter the length of the name: "))
        [print(name.strip()) for name in f.readlines() if len(name.strip()) == length]
        
longest_name()
sum_length()
shortest_names()
names_length_file()
find_num()