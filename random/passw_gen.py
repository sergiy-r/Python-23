# This function generates a password from ASCI characters, numbers, and punctuation marks.
# The user sets the length of passwords and characters to be excluded

def passw_gen(passw_length: int, exclude_str: str) -> str:

    import string
    import random

    all_char = string.ascii_letters + string.digits + string.punctuation  # characters for password before removal

    if exclude_str: # remove characters if not
        keys = exclude_str.replace(' ','').split(',')  # remove spaces and create a list by splitting on ','
        transl_tbl = {ord(key): '' for key in keys}  # create translation table from exclude_str
        print(transl_tbl)
        all_char = all_char.translate(transl_tbl)

    # all_char_new = str(set(all_char) ^ set(char_exclude))

    password = ''  # create blank password

    for i in range(passw_length):
        password += random.choice(all_char)
    # print(password)
    # print(all_char)
    return password


num_char = int(input('Enter the number of characters in the password: '))
exclude_str = input('Enter characters to be excluded, separated by commas: ')


print(passw_gen(num_char, exclude_str))

