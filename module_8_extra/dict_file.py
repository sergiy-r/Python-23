"""
Умова
У файлову систему одного суперкомп'ютера проник вірус, який зламав контроль за правами доступу до файлів.
Для кожного файлу відомо, з якими діями можна звертатися до нього:
запис W,
читання R,
запуск X.

У першому рядку міститься число N — кількість файлів, що містяться в даній файловій системі.
У наступних N рядках містяться імена файлів і допустимих операцій, розділені пробілами.
Далі вказано число M – кількість запитів до файлів. В останніх M рядках вказано запит виду Операція Файл.
До одного і того ж файлу може бути застосована будь-яка кількість запитів.

Вам потрібно відновити контроль над правами доступу до файлів (ваша програма для кожного запиту повинна буде
повертати OK якщо над файлом виконується допустима операція, або Access denied, якщо операція неприпустима).
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
"""
"""
second set:
tmp_796487715 X R W
tmp_31144126 X R
tmp_967334538 R
tmp_264755563 R W
3
read tmp_264755563
execute tmp_796487715
execute tmp_796487715
"""

accesses = """
    helloworld.exe R X
    pinglog W R
    nya R
    goodluck X W R
"""
queries = """
    read nya
    write helloworld.exe
    execute nya
    read pinglog
    write pinglog
"""

# def str_parse(string)
# file_access


class File:
    def __init__(self, filename, read=False, write=False, execute=False):
        self.filename = filename
        self.read = read
        self.write = write
        self.execute = execute

    def __repr__(self):
        return f'{self.filename} {"X" if self.read else ""} {"X" if self.read else ""} {"X" if self.read else ""}'


operations = {"R": "read", "W": "write", "X": "execute"}


def accesses_parse(string):
    my_dict = {}
    for line in string.strip().split("\n"):
        name, *accesses = line.split()
        my_dict[name] = File(name)
        for access in accesses:
            my_dict[name].__dict__[operations[access]] = True


def queries_parse(string):
    my_dict = {}
    for line in string.strip().split("\n"):
        operation, name = line.split()
        my_dict[line] = data[name].__dict__[operation]


data = accesses_parse(accesses)


print(queries_parse(queries))
