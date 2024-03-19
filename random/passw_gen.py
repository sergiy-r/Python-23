# This function generates a password from ASCII characters, numbers, and punctuation marks.
# The user enters the length of the password and may provide characters that need to be excluded.

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
exclude_str = input("Enter characters that need to be excluded, separated by commas, otherwise press 'Enter': ")


print('New password: ', passw_gen(num_char, exclude_str))
