from errors import InvalidUserInputError

def change_default_setting(settings : dict):
        print("Welcom to our app.", end=" ")
        print("This is our defualt setting.")

        for key,value in settings.items():
            if value:
                value  = "on"
            else:
                value = "off"
            print(f"{key} is {value}.")
            print("-" * 20)
            
        while True:
            try:
                user_input = input("Do you want to change default settings:[y/n] ")
                print("-" * 20)

                if user_input.lower() not in ['y', 'n']:
                    raise InvalidUserInputError
                if user_input.lower() == "y":
                    return True
                else:
                    return False
            
            except InvalidUserInputError:
                print("Your input is invalid. Please try again.")
                print("-" * 20)

