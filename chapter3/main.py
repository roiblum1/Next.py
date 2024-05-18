import string  

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, indx, message = "Username contains illegal character"):
        self.indx = indx
        message += " at index " + str(self.indx)
        super().__init__(message)
class UsernameTooShort(Exception):
    def __init__(self, message = "Username is too short"):
        super().__init__(message)
class UsernameTooLong(Exception):
    def __init__(self, message = "Username is too long"):
        super().__init__(message)
class PasswordTooShort(Exception):
    def __init__(self, message = "Password is too short"):
        super().__init__(message)
class PasswordTooLong(Exception):
    def __init__(self, message = "Password is too long"):
        super().__init__(message)
class PasswordMissingCharacter(Exception):
    def __init__(self, what_missing, message = "The password is missing a character"):
        message += " (" + what_missing + ")"
        super().__init__(message)
class PasswordMissingUpper(PasswordMissingCharacter):
    def __init__(self):
        what_missing = "Uppercase"
        super().__init__(what_missing)
class PasswordMissingLower(PasswordMissingCharacter):
    def __init__(self):
        what_missing = "Lowercase"
        super().__init__(what_missing)
class PasswordMissingNumber(PasswordMissingCharacter):
    def __init__(self):
        what_missing = "Digit"
        super().__init__(what_missing)
class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self):
        what_missing = "Special"
        super().__init__(what_missing)
    
def check_username(username):
    
    for indx, c in enumerate(username):
        if not (c.isalpha() or c.isnumeric() or c == "_"):
            raise UsernameContainsIllegalCharacter(indx)
        
    if (len(username) < 3):
        raise UsernameTooShort()
    if (len(username) > 16):
        raise UsernameTooLong()
    return True

def check_password(password):
    if (len(password) < 8):
        raise PasswordTooShort()
    if(len(password) > 40):
        raise PasswordTooLong()
    upper_word = False
    lower_word = False
    number = False
    special_char = False
    for c in password:
        if c.isupper():
            upper_word = True
        if c.islower():
            lower_word = True
        if c.isnumeric():
            number = True
        if (c in string.punctuation):
            special_char = True
    if(upper_word == False):
        raise PasswordMissingUpper()
    if(lower_word == False):
        raise PasswordMissingLower()
    if(number == False):
        raise PasswordMissingNumber()
    if(special_char == False):
        raise PasswordMissingSpecial()
    return True
        
def check_input(username, password):
    return check_username(username) and check_password(password)
    

if __name__ == "__main__":
    test_cases = [
        ("1", "2"),
        ("0123456789ABCDEFG", "2"),
        ("A_a1.", "12345678"),
        ("A_1", "2"),
        ("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"),
        ("A_1", "abcdefghijklmnop"),
        ("A_1", "ABCDEFGHIJLKMNOP"),
        ("A_1", "ABCDEFGhijklmnop"),
        ("A_1", "4BCD3F6h1jk1mn0p"),
        ("A_1", "4BCD3F6.1jk1mn0p")
    ]

    for username, password in test_cases:
        try:
            if(check_input(username, password)):
                print("OK")
        except Exception as e:
            print(e)