
import os, time, datetime
from datetime import timedelta
def getLastUpdate(file):
    print(file)
    created = os.path.getctime(file)
    return created

def CheckDueDate(mydate,when):
    year,month,day,hour,minute,second=time.localtime(mydate)[:-3]

    print(mydate)




    print()
    #print(time.localtime(mydate)[:-3])
    #print(mydate.strftime("%d/%m/%Y %I:%M:%S"))

    print("the date of the file was downloaded")
    print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))

    print()
    # firstdate = mydate.strftime("%d/%m/%Y %I:%M:%S")

    print("the date of the file will be deprecated")
    print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day+1,month,year,20,00,00))
    
    # deprecatedate = d_date.strftime("%d/%m/%Y %I:%M:%S")


    print()
    # datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("the date of today")
    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("%d/%m/%Y %I:%M:%S %p")
    reg_format_date = d_date.strftime("%d/%m/%Y %I:%M:%S")
    print("Date created: "+reg_format_date)



    print()
    print("the date of the file was downloaded")
    print(datetime.datetime.fromtimestamp(mydate))
    ggdate = datetime.datetime.fromtimestamp(mydate)
    print(ggdate.strftime("%d/%m/%Y %I:%M:%S"))


    
    print()
    tempo = ggdate.strftime("%d/%m/%Y %I:%M:%S")

    print(tempo)
    dt_object2 = datetime.datetime.strptime(tempo, "%d/%m/%Y %I:%M:%S")
    print(dt_object2)
    #tempo = tempo+datetime.datetime.timedelta(days=1)
    print(tempo)

    if when == "1 day at 8 pm":
        ##
        pass

    lastUpdate = datetime.datetime.now()
    print(lastUpdate)
    tomorrowVar = lastUpdate + timedelta(days=1)
    tomorrowVar = tomorrowVar.replace(hour=20, minute=00, second=00, microsecond=00)    
    print(tomorrowVar)

    # todayVar = datetime.datetime.now().hour
    todayVar = datetime.datetime.now()
    if todayVar < tomorrowVar:
        pass

    return False

CheckDueDate(getLastUpdate("covid_3.sql"),"1 day at 8 pm")

