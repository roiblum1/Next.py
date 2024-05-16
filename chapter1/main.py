"""
This function reads a text file named 'names.txt' and returns the longest name in the file.

:param None: This function does not take any parameters.
:return: The longest name in the 'names.txt' file.
"""
def longest_name():
    with open('names.txt', 'r') as f:
        print(max(f.readlines(), key=len).strip())

def sum_length():
    with open('names.txt', 'r') as f:
        print(sum(len(name.strip()) for name in f.readlines()))
        
def shortest_names(): 
    with open('names.txt', 'r') as f:
        names = f.readlines()
        [print(name.strip()) for name in names if len(name.strip()) == min(len(name.strip()) for name in names)]

def names_length_file():
    with open('names.txt', 'r') as f:
        with open('names_length.txt', 'w') as f2:
            f2.writelines([str(len(name.strip()))+"\n" for name in f.readlines()])

def find_num():
    with open('names.txt', 'r') as f:
        length = int(input("Enter the length of the name: "))
        [print(name.strip()) for name in f.readlines() if len(name.strip()) == length]
        
longest_name()
sum_length()
shortest_names()
names_length_file()
find_num()