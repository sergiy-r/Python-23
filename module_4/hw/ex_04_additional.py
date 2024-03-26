# Module 4 Homework: Exercise 4
### with extra functionality, contains errors on name adding or updating###


# This is program for a Command Line Interface bot that allows to interact with a contact list
# It allows a user to add, change, and retrieve a contact's phone number, as well as print all contacts
# Names are case-insensitive.
# For a list of commands enter 'help'

# This function checks if the name exists in the contacts and outputs a message if it does.
# if the name doesn't exist, it is added to contacts and the a message is returned

# import os


def add_contact(args, contacts):
    name, phone = args
    if name.lower() in (key.lower() for key in contacts):
        msg('name exists')
    else:
        contacts[name] = phone
        return print(f"{Color.BLUE}{name} " + f"{Color.END}" + "with phone number " + f"{Color.BLUE}{phone} "
                     + f"{Color.END}" + "has been added to contacts.\n")


# This function outputs all contacts
def all(contacts):
    if not contacts:
        msg('no contacts')
    else:
        for key, value in contacts.items():
            print(f"{key}: {value}")
    print("")


# This function updates the phone number for a contact. The name is case-insensitive.
def change_contact(args, contacts):
    change_name, phone = args
    for name in contacts:
        if name.casefold() == change_name.casefold():
            contacts[name] = phone
            return print(f"The phone number for {Color.BLUE}{name} " + f"{Color.END}" + "has been updated to " +
                     f"{Color.BLUE}{phone}{Color.END}\n")
        else:
            msg('no name match')


# This function checks if the number of arguments entered and returns the arguments if two were entered.
# It one or none were entered, it returns them and displays a message.
# If more than two arguments wer entered, it checks if the first two arguments are non-numeric and combines them to
# 'name' argument. If second and third or second, third and forth, or third forth and fifth are numeric then
# it combines them to 'phone' argument.
def check_args(args):
    match len(args):
        case 0:
            msg("no name or number")
            return args
        case 1:
            # num
            if args[0].isnumeric():
                msg("no name")
                return args
            else:
                msg("no number")
                return args
        case (2):
            # alpha num
            if args[0].isalpha() and args[1].isnumeric():
                return args
            else:
                msg("wrong details")
                return args
        case (3):
            # alpha alpha num
            if args[0].isalpha() and args[1].isalpha() and args[2].isnumeric():
                args = [f"{args[0]} {args[1]}", args[2]]
                return args
            # alpha num num
            elif args[0].isalpha() and args[1].isnumeric() and args[2].isnumeric():
                args = [{args[0]}, f"{args[1]} {args[2]}"]
                return args
            else:
                return msg('wrong details')
        case (4):
            # alpha alpha num num
            if args[0].isalpha() and args[1].isalpha() and args[2].isnumeric() and args[3].isnumeric():
                args = [f"{args[0]} {args[1]}", f"{args[2]}{args[3]}"]
                return args
            # alpha num num num
            elif args[0].isalpha() and args[1].isalpha() and args[2].isnumeric() and args[3].isnumeric():
                args = [f"{args[0]}", f"{args[1]}{args[2]}{args[3]}"]
                return args
            else:
                msg('wrong details')
                return args
        case (5):
            # alpha alpha num num num
            if (args[0].isalpha() and args[1].isalpha() and args[2].isnumeric() and args[3].isnumeric()
                    and args[3].isnumeric()):
                args = [f"{args[0]} {args[1]}", f"{args[2]}{args[3]}{args[4]}"]
                return args
            else:
                msg('wrong details')
                return args
        case _:
            msg('too many details')
            return args

#
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')


# Definition of Color class for Color output
class Color:
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# This function output a list of commands for interacting with the bot
def help():
    print(f"\n{Color.BOLD}You can use one of the following commands to interact with the bot:{Color.END}\n",
          f"\n{Color.BLUE}Add Name Number{Color.END} \t- add a name with number to contacts",
          f"\n{Color.BLUE}All{Color.END} \t\t\t\t- display all records in contacts",
          f"\n{Color.BLUE}Close{Color.END} \t\t\t\t- terminate the program",
          f"\n{Color.BLUE}Change Name Number{Color.END} \t- change the phone number for a contact",
          f"\n{Color.BLUE}Exit{Color.END} \t\t\t\t- terminate the program",
          f"\n{Color.BLUE}Hello {Color.END}  \t\t\t- greet the bot",
          f"\n{Color.BLUE}Hi {Color.END} \t\t\t\t- greet the bot",
          f"\n{Color.BLUE}Phone Name{Color.END} \t\t\t- display the phone number for a contact",
          f"\n{Color.BLUE}Update Name Number{Color.END} \t- change the phone number for a contact",
          "\n"
          )


# This function returns error handling messages
def msg(msg_key):
    responses = {
        "welcome": f"Welcome to the assistant bot!\nFor a list of valid commands enter: "
                   f"{Color.BLUE}help{Color.END}\n",
        "hi": "Hello! How can I help you?\n",
        "hi again": "Hello again! How can I help you?\n",
        "bye": "Good bye! Nice chatting with you. Talk to you soon!",
        "invalid1": "You entered an invalid command. Please try again. For a list of valid commands enter: "
                    f"{Color.BLUE}help{Color.END}\n",
        "name exists": "This name already exists in contacts. To update the phone number please use: "
                       f"{Color.BLUE}Change Name Number{Color.END}\n",
        "no contacts": "There are no entries in the contacts list.\n",
        "no name found": "No entries found for this name.\n",
        "no name match": f"No user found with such name. To view all contacts use: {Color.BLUE}All{Color.END}\n",
        "no name or number": "You did not enter a name and a phone number. Please try again by entering: "
                             f"{Color.BLUE}Add Name Number{Color.END}\n",
        "no name": "You did not enter a name. Please try again by entering: "
                   f"{Color.BLUE}Add Name Number{Color.END}\n",
        "no number": "You did not enter a phone number. Please try again by entering: "
                     f"{Color.BLUE}Add Name Number{Color.END}\n",
        "too many details": "You entered too many details.Please try again by entering: "
                            f"{Color.BLUE}Add Name Number{Color.END}\n",
        "wrong details": "The details you entered are incorrect. Please try again by entering: "
                         f"{Color.BLUE}Add Name Number{Color.END}\n"
    }
    return print(responses[msg_key])


# This function parses user input and splits it on space ' ' into arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# This function outputs all contacts from the contacts list
def show_phone(args, contacts):
    search_name = args[0]
    print(search_name)
    for name in contacts:
        if name.casefold() == search_name.casefold():
            print(f"{Color.BLUE}{name}'s{Color.END} phone number is:", end=' ')
            return print(f"{Color.BLUE}{contacts[name]}{Color.END}")
    else:
        return msg('no name found')


# This is the main function which processes user input and defines actions to be taken
def main():
    contacts = {}
    msg('welcome')
    hello_counter = 0
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "add":
            args_new = check_args(args)
            if len(args_new) == 2:
                add_contact(args_new, contacts)
        elif command == "all":
            all(contacts)

        elif command in ["bye", "close", "exit", "quit", "stop"]:
            msg('bye')
            break

        elif command in ["change", "update"]:
            args_new = check_args(args)
            if len(args_new) == 2:
                change_contact(args_new, contacts)

        elif command in ["hello", "hello!", "hi", "hi!"]:
            if hello_counter == 0:
                msg("hi")
                hello_counter += 1
            else:
                msg("hi again")
                hello_counter += 1

        elif command == "help":
            help()

        elif command == "how":
            if len(args) == 2:
                if args[0] == "are" and (args[1] == "you" or args[1] == "you?"):
                    if hello_counter == 0:
                        msg("hi")
                        hello_counter += 1
                    else:
                        msg("hi again")
                        hello_counter += 1
                else:
                    msg("invalid1")
            else:
                msg("invalid1")

        elif command == "phone":
            print(command, args)  # temporary for debugging
            if len(args) == 1:
                show_phone(args, contacts)

        else:
            msg('invalid1')


if __name__ == "__main__":
    main()
