dictionary_str = """
    cAnnot
    cannOt
    fOund
    pAge
"""
text = "The PAGE cannot be found"
def parse_dict(string):
    my_dict = {}
    for line in string.strip().split("\n"):
        my_dict.setdefault(line,[]).append(line)
    return my_dict
def check_text(string):
    count_err = 0
    for word in string.split():
        if word not in dictionary.get(word.lower(),[]):
            if len(list(filter(str.isupper,word))) != 1:
                count_err += 1
    return count_err
dictionary = parse_dict(dictionary_str)
print(check_text(text))