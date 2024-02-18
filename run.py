from change_settings import change_settings, update_settings
from default_setting import change_default_setting
from generate_password import find_true_options, generate_random_password
from errors import InvalidUserInputError

password_generation_options = {
    "lowercase": True,
    "uppercase": True,
    "symbol": False,
    "number": True,
    "space": False,
    "length": 8,
}

def generate_first_random_password():
    if change_default_setting(password_generation_options):
        new_settings = change_settings(password_generation_options)
        update_settings(password_generation_options, new_settings) 

    true_options = find_true_options(password_generation_options)
    random_password = generate_random_password(true_options)
    return random_password

def generate_random_password_loop():
    true_options = find_true_options(password_generation_options)
    random_password = generate_random_password(true_options)
    return random_password

def ask_generate_random_password_again(random_password):
    first_password = random_password
    print(first_password)
    print("-"*20)
    final_password = first_password
    while True:
        try:
            user_input = input("Do you want another password:[y:yse/n:no] ")
            print("-"*20)
            if user_input not in ['y', 'n']:
                raise InvalidUserInputError
            if user_input == 'y':
                final_password = generate_random_password_loop()
                print(final_password)
            else:
                return final_password
        except InvalidUserInputError:
            print("You input is invalid. Please try again.")
            
random_password = generate_first_random_password()
final_password = ask_generate_random_password_again(random_password)

with open("password.txt", mode='a') as file:
    file.write(final_password)
    file.write("\n------------------------\n")
