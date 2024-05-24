def check_id_valid(id_number):
    """
    Check if the given ID number is valid according to the specific algorithm.
    :param id_number: The ID number to check.
    :return: True if the ID is valid, False otherwise.
    """
    id_number = str(id_number)
    id_number = [int(num) * 2 if (i + 1) % 2 == 0 else int(num) for i, num in enumerate(id_number)]
    id_number = [num if num < 10 else num - 9 for num in id_number]  
    return sum(id_number) % 10 == 0  

class IDIterator():
    """
    An iterator to generate valid ID numbers starting from a given ID number.
    """
    def __init__(self, id_):
        """
        Initialize the iterator with the starting ID.
        :param id_: The starting ID number.
        """
        self.id = id_
        self.max = 999999999
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """
        Return the next valid ID number.
        :return: The next valid ID number.
        :raises StopIteration: When the maximum ID number is reached.
        """
        self.id += 1  
        while self.id <= self.max:
            if check_id_valid(self.id):
                valid_id = self.id
                self.id += 1
                return valid_id
            self.id += 1
        raise StopIteration()

def gen_valid_id(id_number):
    """
    A generator to yield valid ID numbers starting from a given ID number.
    :param id_number: The starting ID number.
    :yield: The next valid ID number.
    """
    current_id = id_number + 1 
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1
        
if __name__ == '__main__':
    id_number = int(input("Enter ID: "))
    it_or_gen = str(input("Enter 'it' for iterator or 'gen' for generator: "))
    while(it_or_gen != 'it' and it_or_gen != 'gen'):
        it_or_gen = str(input("Enter 'it' for iterator or 'gen' for generator: "))
  
    if(it_or_gen == 'it'):
        print("Using iterator: ")
        id_iter  = IDIterator(id_number)
        for id in range(10):
            print(next(id_iter))
    else:
        print("Using generator: ")
        id_gen = gen_valid_id(id_number)
        for _ in range(10):
            print(next(id_gen))
    