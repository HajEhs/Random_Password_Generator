from default_setting import password_generation_options as options
from errors import InvalidUserInput


new_setting = []
for key, value in options.items():
    if key != "length":
        print("enter -> {}".format(value))
        
        while True:
            user_choice = input(f"Do you want to have {key}:[y/n] ")
            print("-" * 20)
            try:
                if user_choice.lower() not in ['y', 'n', ""]:
                    raise InvalidUserInput
                else:
                    if user_choice == "":
                        user_choice = value
                    elif user_choice == "y":
                        user_choice = True
                    else:
                        user_choice = False
                    new_setting.append((key, user_choice))
                    break       

            except InvalidUserInput:
                print("Your input is invalid. Please enter y, n or enter.")
                print("-" * 20)
                 
print(new_setting)