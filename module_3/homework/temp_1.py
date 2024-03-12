from datetime import datetime

birthday_str = '2000-03-13'
# parse the input date
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
today = datetime.today().date()

# replace year in birthday to current year
birthday_this_year = birthday.replace(year=today.year).date()
print(birthday_this_year)

days_to_birthday = (birthday_this_year - today).days

if days_to_birthday >= 0 and days_to_birthday <= 7:

    print(f'Birthday is in {days_to_birthday} days')


else:
    print('Birthday is not today or next 6 days')

