phones = []
phones.append("07770001111")
print(phones)
phones.append("08881110000")
print(phones)
p_rem = "08881110000"
phones = [p for p in phones if str(p) != p_rem]
print(phones.)

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

f = Field("name")
print(f)