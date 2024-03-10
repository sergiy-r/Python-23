# date from iso format string
from datetime import date
date_from_string = date.fromisoformat("2020-01-31")
print(date_from_string)

# date from any string format using strptime
# more details on www.strftime.org

from datetime import datetime
date_string = "01-31-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"
print(datetime.strptime(date_string, format_string))


