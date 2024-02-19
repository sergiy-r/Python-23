# Встановлюємо ціни на продукти
croissant_unit_price = 1.04
glass_unit_price = 0.34
coffee_pack_unit_price = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = num_croissants * croissant_unit_price + \
             num_glasses * glass_unit_price + \
             num_coffee_packs * coffee_pack_unit_price

# Визначаємо кількість повних доларів і центів
total_in_dollars = int(total_cost)
total_in_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_in_dollars} доларів")
print(f"Загальна вартість у центах: {total_in_cents} центів")
