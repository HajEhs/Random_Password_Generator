import random
from string import ascii_lowercase
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

def generate_random_password(true_options : list):
    my_password = ""
    
    len_password = true_options[-1]
    for password in range(len_password):
        random_choice = random.choice(true_options)
        
        if random_choice == "lowercase":
            password = add_lowercase()
            my_password += password
            
            
            
    


        