from errors import InvalidUserInput

password_generation_options = {
    "lowercase": True,
    "uppercase": True,
    "symbol": False,
    "number": True,
    "space": False,
    "length": 8,
}

def change_default_setting():
        print("Welcom to our app.", end=" ")
        print("This is our defualt setting.")

        for key,value in password_generation_options.items():
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
                    raise InvalidUserInput
                return user_input
            
            except InvalidUserInput:
                print("Your input is invalid. Please try again.")
                print("-" * 20)

