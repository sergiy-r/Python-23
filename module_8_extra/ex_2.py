"""
Примітки до прикладів тестів
1. У слові не можна, згідно з словником можливі два варіанти розміщення наголосу. Ці варіанти в словнику можуть бути перераховані в будь-якому порядку (тобто як спочатку cAnnot, а потім cannOt, так і навпаки). Дві помилки, здійснені Петей - це слова be (наголос взагалі не поставлено) і fouNd (наголос поставлено неправильно). Слово thE відсутня у словнику, але оскільки в ньому Петя поставив рівно один наголос, визнається вірним.
2. Неправильно розставлені наголоси у всіх словах, крім The (воно відсутнє у словнику, у ньому поставлено рівно один наголос). У решті слів або ударні всі літери (у слові PAGE), або поставлено жодного наголосу.
New
cAnnot
cannOt
fOund
pAge
thE pAge cAnnot be found
10:47
правильна відповідь  - 2
10:48
cAnnot
cannOt
fOund
pAge
The PAGE cannot be found
правильна відповідь  - 4
"""

dictionary_str = """
    cAnnot
    cannOt
    fOund
    pAge
"""

# text = "thE pAge cAnnot be found"
text = "The PAGE cAnnot be found"

def parse_dic(string):
    my_dict = {}
    for line in string.strip().split("\n"):
        my_dict.setdefault(line,[]).append(line)
    return my_dict


def check_text(string):
    count_err = 0
    for word in string.split():
        if word not in dictionary.get(word.lower(), []):
            if len(list(filter(str.isupper, word))) != 1:
               count_err += 1
    return count_err


dictionary = parse_dic(dictionary_str)

print(check_text(text))


