import re 

email_policy = [
        '[@]',
        '[.]',
]

password_policy = [
        '[0-9]',
        '[a-z|A-Z]',
        '[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\\\|\;\:\'\"\,\<\.\>\/\?]',
        '.{8,}',
]

login_key_list = [
        'username', 
        'email', 
        'password', 
]

def check_character_policy(policies:list, character:str):

    check_policy=True

    for policy in policies:
        if not re.search(policy, character):
            raise Exception('KEY_ERROR')

    return check_policy


def check_dictionary_keys(check_dict:dict, necessary_key_list:list):

    check_dict_keys = check_dict.keys()

    for necessary_key in necessary_key_list:
        if necessary_key in check_dict_keys:
            check_keys_flag = True

        else:
            print("key list in http body:", set(check_dict_keys))
            print("necessary_key_list:", set(necessary_key_list))
            raise Exception('KEY_ERROR')

    return check_keys_flag



