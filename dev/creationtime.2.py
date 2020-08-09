import os, time, datetime

file = "covid_3.sql"
print(file)


created = os.path.getctime(file)

year,month,day,hour,minute,second=time.localtime(created)[:-3]

print(created)
print("the date of the file was downloaded")
print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))


print("the date of the file will be deprecated")
print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day+1,month,year,20,00,00))


# datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print("the date of today")
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d/%m/%Y %I:%M:%S %p")
print("Date created: "+reg_format_date)

#datetime.date(year=2000, month=1,day=1) < datetime.datetime(year=year,month=month,day=day,hour=hour) <= datetime.datetime.now()


def getLastUpdate(file):
    import os, time, datetime
    print(file)
    created = os.path.getctime(file)
    return created

def CheckDueDate(myfile,when):
    year,month,day,hour,minute,second=time.localtime(created)[:-3]

    # print(created)
    print("the date of the file was downloaded")
    print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))


    print("the date of the file will be deprecated")
    print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day+1,month,year,20,00,00))


    if when == "1 day at 8 pm":
        ##
        pass


    return False