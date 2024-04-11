from datetime import datetime, timedelta
from collections import UserDict

# Define a UserDict with names and birthdays
class BirthdayDict(UserDict):
    def __init__(self, data):
        super().__init__(data)

    def get_congratulations_dates(self):
        today = datetime.today()
        congratulations_dates = {}

        for name, birthday in self.data.items():
            # Calculate the next birthday
            next_birthday = datetime(today.year, birthday.month, birthday.day)
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

            # Calculate the congratulations date (3 days before the birthday)
            congratulations_date = next_birthday - timedelta(days=3)

            # If the congratulations date falls on a weekend (Saturday or Sunday), move it to the following Monday
            if congratulations_date.weekday() in [5, 6]:
                congratulations_date += timedelta(days=(7 - congratulations_date.weekday()))

            congratulations_dates[name] = congratulations_date

        return congratulations_dates

# Example data: names and birthdays
birthday_data = {
    "Alice": datetime(2000, 5, 15),
    "Bob": datetime(1995, 8, 20),
    "Charlie": datetime(1988, 12, 10),
    "David": datetime(1992, 3, 5),
}

# Create a BirthdayDict instance
birthday_dict = BirthdayDict(birthday_data)

# Get congratulations dates
congratulations_dates = birthday_dict.get_congratulations_dates()

# Sort by congratulations date
sorted_congratulations = sorted(congratulations_dates.items(), key=lambda x: x[1])

# Print the sorted congratulations dates and corresponding birthdays
print("Upcoming congratulations dates:")
for name, congratulations_date in sorted_congratulations:
    print(f"{name}: {congratulations_date.strftime('%Y-%m-%d')} (Birthday: {birthday_dict[name].strftime('%Y-%m-%d')})")
