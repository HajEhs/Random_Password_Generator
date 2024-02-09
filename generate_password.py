from default_setting import password_generation_options as settings
import random

def find_true_options(settings : dict):
    true_options = []
    for option in settings:
        if settings[option]:
            true_options.append(option)
    return true_options

def generate_random_password(true_options : list):
    my_password = ""


        