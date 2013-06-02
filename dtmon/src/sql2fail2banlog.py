#!/usr/bin/env python
'''
Created on Jun 1, 2013

@author: Tommy Maersk
'''
import MySQLdb as sql
db = sql.connect("HOST","USER","PASS","DB")
cs = db.cursor()


    
theFile = open("/var/log/fail2ban.log")
while True:
    theline = str(theFile.readline())
    if theline == "":
        break
    theline = theline.replace("  ", " ")
    theline = theline.replace("'", "")
    theline = theline.replace("`", "")
    theline = theline.strip()
    theline = theline.split(",",1)
    
    thedate = theline[0]
    thedate = thedate.strip()
    #print(thedate)
    
    thetext = theline[1]
    
    thetext = thetext.split(" ",1)
    thetext = thetext[1]
    thetext = thetext.strip()
    #print(thetext)
    
    cs.execute("SELECT COUNT(id) FROM fail2banlog WHERE thetext = '"+thetext+"' AND thetime = '"+thedate+"'")
    result = cs.fetchone()
    tjek = result[0]
    if tjek == 0:
        query = "INSERT INTO fail2banlog (thetime,thetext) VALUES ('"+thedate+"','"+thetext+"')"
        cs.execute(query)
        db.commit()
db.commit()
print("DONE!")
db.close()