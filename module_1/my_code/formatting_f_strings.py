# formatting f strings
# https://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf

import math
variable = math.pi
print(f"Using Numeric {variable = }")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|\n")

print("\n", "*  " * 30, "\n")

import math
variable = 10
print(f"Using Numeric {variable = }")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:d}")
print(f"This prints also with formatting {variable:n}")
print(f"This prints with spacing {variable:10d}\n")
variable = math.pi
print(f"Using Numeric {variable = }")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:f}")
print(f"This prints with spacing {variable:20f}")


print("\n", "*  " * 30, "\n")

APPLES = .50
BREAD = 1.50
CHEESE = 2.25
numApples = 3
numBread = 10
numCheese = 6
prcApples = numApples * APPLES
prcBread = numBread* BREAD
prcCheese = numCheese * CHEESE
strApples = 'Apples'
strBread = 'Rye Bread'
strCheese = 'Cheese'
total = prcBread + prcCheese + prcApples
print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples:10s}{numApples:10d}\t${prcApples:>5.2f}')
print(f'{strBread:10s}{numBread:10d}\t${prcBread:>5.2f}')
print(f'{strCheese:10s}{numCheese:10d}\t${prcCheese:>5.2f}')
print(f'{"Total:":>20s}\t${total:>5.2f}')

abc = 1.23
print(f"{abc = }")