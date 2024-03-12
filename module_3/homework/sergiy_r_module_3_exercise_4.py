# Module 3 Exercise 4
# Author: Sergiy R

def get_upcoming_birthdays(users:list) -> list:
    # This function takes a list of dictionaries with 'name' and 'birthday' and returns a list of dictionaries
    # with 'name' and 'congratulation_date'

    from datetime import datetime, timedelta
    today = datetime.today().date()

    # create an empty list for output
    users_congrats_next_7_days = []

    # iterate through users
    for user in users:
        # parse the input date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # replace year in birthday to current year
        birthday_this_year = birthday.replace(year=today.year)  # .date()?

        # calculate number of days to birthday this year
        days_to_birthday = (birthday_this_year - today).days

        if days_to_birthday >= 0 and days_to_birthday <= 7:
            match birthday_this_year.isoweekday():
                case 6:
                    congratulation_date = birthday_this_year + timedelta(days= 2)
                case 7:
                    congratulation_date = birthday_this_year + timedelta(days= 1)
                case _:
                    congratulation_date = birthday_this_year

            # create a dictionary for a user
            user_congrats = dict(name=user['name'], congratulation_date=congratulation_date.strftime(format="%Y.%m.%d"))

            # add user to list
            users_congrats_next_7_days.append(user_congrats)

    if not users_congrats_next_7_days:
        print('There are no birthdays today or in the next 7 days')

    return users_congrats_next_7_days

# create users

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Bob Dyson", "birthday": "1987.03.16"},
    {"name": "Marta Stewart", "birthday": "1990.03.22"},
    {"name": "Teresa Torres", "birthday": "1980.03.18"},
    {"name": "Alice Braga", "birthday": "1980.03.17"}
]

print(f"List of upcoming birthdays: \n{get_upcoming_birthdays(users)}")