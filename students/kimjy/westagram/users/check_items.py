import re 
from varname import nameof

email_policy = [
        '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        'email_policy'
]
password_policy = [
        "((?=.*[0-9])(?=.*[a-z|A-Z])(?=.*[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\\\|\;\:\'\"\,\<\.\>\/\?]).{8,})",
        'password_policy'
]
login_key_list = [
        'username', 
        'email', 
        'password', 
]

def check_character_policy(policy:list, character:str):

    check_policy = True

    if not re.search(policy[0], character):
        raise KeyError('KEY_ERROR was occured from '+policy[1])

    return check_policy

def check_dictionary_keys(check_dict:dict, necessary_key_list:list):

    check_dict_keys = check_dict.keys()
    
    if set(necessary_key_list).issubset(set(check_dict_keys)):
        check_keys_flag = True

    else:
        required_keys = set(necessary_key_list) \
                      - set(necessary_key_list).intersection(set(check_dict_keys))

        error_message='' 
        for required_key in required_keys:
            error_message += required_key + ", "

        raise KeyError("["+error_message+"] was not found in http body")
    return check_keys_flag
