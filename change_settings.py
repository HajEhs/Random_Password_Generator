from errors import InvalidUserInputError, LengthLimitError

def change_settings(settings : dict):
    new_setting = []
    for key, value in settings.items():
        print("enter -> {}".format(value))
        
        if key != "length":
            while True:
                user_choice = input(f"Do you want to have {key}:[y:yse/n:no] ")
                print("-" * 20)
                try:
                    if user_choice.lower() not in ['y', 'n', ""]:
                        raise InvalidUserInputError
                    else:
                        if user_choice == "":
                            user_choice = value
                        elif user_choice == "y":
                            user_choice = True
                        else:
                            user_choice = False
                        new_setting.append((key, user_choice))
                        break       

                except InvalidUserInputError:
                    print("Your input is invalid.[y:yse/n:no/enter:default]")
                    print("-" * 20)
        
        else:
            while True:
                
                try:
                    length = int(input("length(between 4 to 20): "))
                    print("-" * 20)
                    if length < 4 or length > 20:
                        raise LengthLimitError
                    new_setting.append((key, length))
                    break
                    
                except ValueError:
                    print("You must enter an integer number.")
                    print("-" * 20)

                except LengthLimitError:
                    print("Your number must be between 4 to 20. ")
                    print("-" * 20)
    return new_setting
           
def update_settings(settings: dict, new_settings: list):      
    for item in new_settings:
        settings.update({item[0]: item[1]})
    return settings

      
