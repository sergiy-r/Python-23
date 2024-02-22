# List of lists
languages_1 = ['C', 'C++', 'Java', 'Python', 'Rust', ['JS', 'mojo']]
languages_2 = ['C', 'C++', 'Java', 'Python', 'Rust']
languages_3 = [languages_1, languages_2]

print(languages_3)
print(languages_3[0][3])  # print element with index 3 from the first element (list)

# N.B. List can hold lists as elements at multiple levels

print(languages_3[0][5].index('JS'))