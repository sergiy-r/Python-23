# toordinal
# toordinal gives the ordinal number of the day from 1 January 0001
from datetime import datetime

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since_ordinal = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(f"Days since Napoleon burned Moscow {days_since_ordinal}")

days_since = current_date - napoleon_burns_moscow
print(days_since) # difference in days, minutes, seconds, microsecords
print(days_since.days) # difference in days
print(days_since.total_seconds()) # difference in seconds 
