
import os, time, datetime
from datetime import timedelta


#get file date
def getLastUpdate(file):
    print(file)
    created = os.path.getctime(file)
    return created



#add time to a specific date to create the due date
def setPassDay(mydate):
    
    print("incoming date "+ str(mydate))

    theNextDay = mydate + timedelta(days=1)
    theNextDay = theNextDay.replace(hour=20, minute=00, second=00, microsecond=00) 

    print("outgoing date "+ str(theNextDay))

    return theNextDay



def CheckDueDate(mydate,when):

    print(mydate)
    print("the date of the file date is: "+str(datetime.datetime.fromtimestamp(mydate)))
   
    ggdate = datetime.datetime.fromtimestamp(mydate)


    if setPassDay(ggdate) < datetime.datetime.now():
        print("es mas grande")
        print("ya vencio")
        pass
    else:
        print("es mas chico")
        print("todavia no vencio")
        pass

    return False

CheckDueDate(getLastUpdate("covid_3.sql"),"1 day at 8 pm")

