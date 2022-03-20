# Import date and time
import datetime

# Import date and time for now
now = datetime.datetime.now()

# Print
print("{}Hour {}Minute {}Second {}Date {}Month {}Year".format(
    now.hour,
    now.minute,
    now.second,
    now.day,
    now.month,
    now.year
))