# character encoding

with open('example.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('Some data')

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)


# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
