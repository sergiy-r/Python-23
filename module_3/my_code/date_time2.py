from datetime import datetime

t = '05.03.2024'

d = datetime.strptime(t,'%d.%m.%Y')

print(d.date())

print(d.day, d.month, d.year)
