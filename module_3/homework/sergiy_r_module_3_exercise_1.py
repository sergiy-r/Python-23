# Module 3 Exercise 1
# Author: Sergiy R

def get_days_from_today(date: str) -> int:
    # This function returns the number of days between today's date and supplied date.
    # if supplied date > today, the result will be negative, if < today, result will be positive.

    from datetime import datetime
    str_format = '%Y-%m-%d'  # define date format for input string

    try:
        input_date = datetime.strptime(date, str_format)  # convert string to date as per str_format
        today = datetime.today()  # get today's date
        days_diff = today.date() - input_date.date()  # calculate difference between entered date and today's date

        if days_diff.days == 0:  # message if entered date is the same as today's date
            print(f"The entered day is today, {input_date.date()}, so the difference is 0 days.")

        else:  # message if entered date is different from today
            print(f"The difference between today's date, {today.date()}, and the entered date, {date},"
                  f" is {days_diff.days} day(s).")

        return days_diff.days

    except ValueError:  # return error message if input format is incorrect
        print(f"The entered date '{date}' does not match the format 'YYYY-MM-DD'")


print(get_days_from_today('2024-03-01'))
