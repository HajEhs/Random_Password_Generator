from change_settings import change_settings, update_settings
from default_setting import change_default_setting
from generate_password import find_true_options, generate_random_password

password_generation_options = {
    "lowercase": True,
    "uppercase": True,
    "symbol": False,
    "number": True,
    "space": False,
    "length": 8,
}

if change_default_setting(password_generation_options):
    new_settings = change_settings(password_generation_options)
    update_settings(password_generation_options, new_settings) 

true_options = find_true_options(password_generation_options)
random_password = generate_random_password(true_options)
print(random_password)