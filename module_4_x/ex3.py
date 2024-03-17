"""
Тобі дано словник із акціями і їх цінами. Функція повинна повертати найдорожчу акцію.
Вхідні значення: Словник, у якому біржовий тікер (коротка назва) акції є ключем, а значенням є ціна цієї акції.
Вихідні значення: Біржовий тікер як рядок.
Приклади:

1
2
Передумови: Ціни є унікальними, тобто не повторюються.
"""
def best_stock(stocks: dict) -> str:
    best_stock = ''
    max_value = 0
    for stock in stocks:
        if stocks.get(stock) > max_value:
            best_stock = stock
            max_value = stocks.get(stock)
    print(best_stock,': ', max_value )
    return best_stock




assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"