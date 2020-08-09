import os
import datetime
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)



d = modification_date("covid_3.sql")

print(repr(d))