# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

# from datetime import datetime
#
# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
#
# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0
# print(difference.days) # 365

# from datetime import datetime, timedelta
#
# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)

# from datetime import datetime, timedelta
#
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)
#
# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

# from datetime import datetime as dt, timedelta as td
#
# now = dt.now()
# delta = td(weeks=4)
#
# print(f"Now: {now}")
# print(f"Now + 4 weeks: {now + delta}")
# print(f"Now - 4 weeks: {now - delta}")
#

# from datetime import datetime, date, time
#
# # Створення об'єкта datetime
# # date = datetime(year=2023, month=12, day=18)
# date_now = datetime.now()
# date_date = date.today()
# date_time = time(date_now.hour, date_now.minute, date_now.second)
# print(date_now)
# print(date_date)
# print(date_time)
#
#  # Отримання порядкового номера
# date_now_ordinal = date_now.toordinal()
# date_date_ordinal= date_date.toordinal()
# print(f"Порядковий номер дати {date_now} становить {date_now_ordinal}")
# print(f"Порядковий номер дати {date_date} становить {date_date_ordinal}")

from datetime import datetime as dt, date as d, timedelta as td

# today = d.today()
today = dt.now()
yesterday = today - td(days=1)
tomorrow = today + td(days=1)

print(f"Yesterday's date: {yesterday}")
print(f"Today's date: {today}")
print(f"Tomorrow's date: {tomorrow}")

print(today - yesterday)
print(tomorrow - yesterday)
print(yesterday - tomorrow)
