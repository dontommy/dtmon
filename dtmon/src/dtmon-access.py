#!/usr/bin/env python
'''
Created on Mar 20, 2013

@author: dtpc
'''
import subprocess
import MySQLdb as sql
import time
import psutil
import sys
db = sql.connect("localhost","root","muaiwqyt","system_info")
cs = db.cursor()


myFile = open("/var/log/apache2/access.log")
while True:
    log = str(myFile.readline())
    if log == "":
        break
    if "GET" in log:
        thebuf = log.split('"GET')
        thepath = thebuf[1]
        thepath = thepath.split('HTTP/')
        thepath = str(thepath[0])


        cs.execute("SELECT COUNT(id) FROM accesslog WHERE thepath = '"+thepath+"'")
        result = cs.fetchone()
        tjek = result[0]
        if tjek == 0:
            query = "INSERT INTO accesslog (hits,thepath) VALUES (1,'"+thepath+"')"
            cs.execute(query)
            db.commit()
        if tjek != 0:
            query = "UPDATE accesslog SET hits = (hits+1) WHERE thepath = '"+thepath+"'"
            cs.execute(query)
            db.commit()
#db.commit()

print("DONE!")
db.close()
