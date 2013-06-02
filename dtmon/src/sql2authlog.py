#!/usr/bin/env python
'''
Created on Jun 1, 2013

@author: Tommy Maersk
'''
import MySQLdb as sql
db = sql.connect("localhost","root","muaiwqyt","system_info")
cs = db.cursor()

def GetDate(mon,day,time):
    if mon == "Jan":
        themon = "01"
    if mon == "Feb":
        themon = "02"
    if mon == "Mar":
        themon = "03"
    if mon == "Apr":
        themon = "04"
    if mon == "May":
        themon = "05"
    if mon == "Jun":
        themon = "06"
    if mon == "Jul":
        themon = "07"
    if mon == "Aug":
        themon = "08"
    if mon == "Sep":
        themon = "09"
    if mon == "Oct":
        themon = "10"
    if mon == "Nov":
        themon = "11"
    if mon == "Dec":
        themon = "12"
    thestring = "2013-",themon,"-",day," ",time
    thestring = "".join(thestring)
    return thestring
    
        
    
theFile = open("/var/log/auth.log")
while True:
    theline = str(theFile.readline())
    if theline == "":
        break
    #thelinecount = theline.find("CRON")
    if "cron" in theline:
        continue
    theline = theline.replace("  ", " ")
    theline = theline.replace("'", "")
    theline = theline.replace("`", "")
    theline = theline.strip()
    theline = theline.split(" ",3)
    
    month = theline[0]
    day = theline[1]
    time = theline[2]
    
    thedate = GetDate(month,day,time)
    #print(thedate)
    
    thetext = theline[3]
    thetext = thetext.split(":",1)
    thetext = thetext[1]
    thetext = thetext.replace("\n", "")
    #print(thetext)
    
    cs.execute("SELECT COUNT(id) FROM authlog WHERE thetext = '"+thetext+"' AND thetime = '"+thedate+"'")
    result = cs.fetchone()
    tjek = result[0]
    if tjek == 0:
        query = "INSERT INTO authlog (thetime,thetext) VALUES ('"+thedate+"','"+thetext+"')"
        cs.execute(query)
        db.commit()
db.commit()
print("DONE!")
db.close()