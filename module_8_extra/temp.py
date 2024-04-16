dictionary_str = """
    cAnnot
    cannOt
    fOund
    pAge
"""
# text = "thE pAge cAnnot be found"

def parse_dic(string) -> dict:
    my_dict = {}
    for line in string.strip().split("\n"):
        my_dict.setdefault(line.strip().lower(), []).append(line.strip())
    return my_dict


def check_text(string):
    count_err = 0
    for word in string.split():
        if word not in dictionary.get(word.lower, []):
            if len(list(filter(str.isupper, word))) != 1:
                count_err += 1
    return count_err


dictionary = parse_dic(dictionary_str)


print(parse_dic(dictionary_str))