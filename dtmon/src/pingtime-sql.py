#!/usr/bin/env python
'''
Created on Mar 20, 2013

@author: dtpc
'''
import subprocess
import MySQLdb as sql
import time

def pingtime():
    pingtime = subprocess.check_output("ping google.com -c 3 | grep icmp_req=3",shell=True)
    pingtime = str(pingtime)
    pingtime = pingtime.split("time=")
    pingtime = str(pingtime[1])
    pingtime = pingtime.split(" ")
    pingtime = str(pingtime[0])
    return pingtime


def pingtime2():
    pingtime = subprocess.check_output("ping flotbutik.dthost.dk -c 3 | grep icmp_req=3",shell=True)
    pingtime = str(pingtime)
    pingtime = pingtime.split("time=")
    pingtime = str(pingtime[1])
    pingtime = pingtime.split(" ")
    pingtime = str(pingtime[0])
    return pingtime

def pingtime3():
    pingtime = subprocess.check_output("ping dontommy.com -c 3 | grep icmp_req=3",shell=True)
    pingtime = str(pingtime)
    pingtime = pingtime.split("time=")
    pingtime = str(pingtime[1])
    pingtime = pingtime.split(" ")
    pingtime = str(pingtime[0])
    return pingtime


theping = pingtime()
theping2 = pingtime2()
theping3 = pingtime3()
thetime = str(time.time())
db = sql.connect("HOST","USER","PASS","DB")
cs = db.cursor()

query = "INSERT INTO pingtimes (pingtime,thetime,thesite) VALUES ('"+theping+"','"+thetime+"','1')"

cs.execute(query)

cs = db.cursor()

query = "INSERT INTO pingtimes (pingtime,thetime,thesite) VALUES ('"+theping2+"','"+thetime+"','2')"

cs.execute(query)

cs = db.cursor()

query = "INSERT INTO pingtimes (pingtime,thetime,thesite) VALUES ('"+theping3+"','"+thetime+"','3')"

cs.execute(query)


db.commit()

print("DONE!")
db.close()
