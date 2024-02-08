def change_default_setting():
        print("Welcom to our app.", end=" ")
        print("This is our defualt setting.")

        password_generation_option = {
            "lowercase": True,
            "uppercase": True,
            "symbol": False,
            "space": False,
            "number": True,
            "space": False,
            "length": 8,
        }

        for key,value in password_generation_option.items():
            if value:
                value  = "on"
            else:
                value = "off"
            print(f"{key} is {value}")
            print("-" * 20)
        2
       
        