def greet(name, message="Hello", punctuation='!'):
    match punctuation:
        case '.':
            print(f"{message}, {name}.")
        case '?':
            print(f"{message}, {name}?")
        case '.':
            print(f"{message}, {name}!")
        case _:
            print(f"{message}, {name}!")

greet('Sergiy')

greet('Sergiy', 'How are you','?')
