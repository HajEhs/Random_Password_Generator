import random
from string import ascii_lowercase, ascii_uppercase
from default_setting import password_generation_options as settings


def find_true_options(settings : dict):
    true_options = []
    for option in settings:
        if settings[option]:
            if  option == "length":
                true_options.append(settings[option])
            true_options.append(option)
    return true_options

def add_lowercase():
    choice = random.choice(ascii_lowercase)
    return choice

def add_uppercase():
    choice = random.choice(ascii_uppercase)
    return choice

def add_symbol():
    symbol_1 = random.choice(range(33, 48))
    symbol_2 = random.choice(range(91,97))
    symbol_3 = random.choice(range(123, 127))
    choice = random.choice([symbol_1, symbol_2, symbol_3])
    return chr(choice)

def add_number():
    choice = random.choice(range(0,10))
    return choice

def generate_random_password(true_options : list):
    my_password = ""
    
    len_password = true_options[-1]
    for password in range(len_password):
        random_choice = random.choice(true_options)
        
        if random_choice == "lowercase":
            password = add_lowercase()
            my_password += password
        
        elif random_choice == "uppercase":
            password = add_uppercase()
            my_password += password
        
        elif random_choice == "symbol":
            password = add_symbol()
            my_password += password
        
        elif random_choice == "number":
            password = add_number()
            my_password += password
        
        else:
            my_password += " "
    
    return my_password
            
    


        