accesses = """
    tmp_796487715 X R W
    tmp_31144126 X R
    tmp_967334538 R
    tmp_264755563 R W
    """
queries = """
    read tmp_264755563
    execute tmp_796487715
    execute tmp_796487715
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
        return f"{self.filename} {"R" if self.read else ""} {"W" if self.write else ""} {"X" if self.execute else ""}"
operations = {"R": "read", "W": "write", "X": "execute"}
def accesses_parse(string):
    my_dict = {}
    for line in string.strip().split("\n"):
        name, *accesses = line.split()
        my_dict[name] = File(name)
        for access in accesses:
            my_dict[name].__dict__[operations[access]] = True
    return my_dict
def queries_parse(string):
    my_dict = {}
    for line in string.strip().split("\n"):
        operation, name = line.split()
        my_dict[line] = data[name].__dict__[operation]
    return my_dict
data = accesses_parse(accesses)
print(queries_parse(queries))