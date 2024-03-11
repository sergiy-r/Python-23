# Module 3 Exercise 3
# Author: Sergiy R

# def get_upcoming_birthdays(users:list) -> list:
#     # This function takes a list of dictionaries with 'name' and 'birthday' and returns a list of dictionaries
#     # with congratulation_date
#
#     import datetime
#
#     today = datetime.today().date()
#
#     for user in users:
#         birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
#         birthday_this_year =
#         if birthday_this_year < today

import datetime

# Create a sample datetime object
birthday = datetime.date(2000, 3, 15)

# Replace the year with a new value (e.g., 2023)
this_year = datetime.datetime.now().year
print(this_year)
birthday_this_year = birthday.replace(year=this_year)
print(birthday, birthday_this_year)
if birthday_this_year.isoweekday() in [6,7]:
    # set congratulation_date to week +1 day 1 in isoformat
    congratulation_date = birthday_this_year.isoweekday()

