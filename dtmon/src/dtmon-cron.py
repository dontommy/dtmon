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
db = sql.connect("HOST","USER","PASS","DB")
cs = db.cursor()


def pingtime():
    pingtime = subprocess.check_output("ping google.com -c 3 | grep icmp_req=3",shell=True)
    pingtime = str(pingtime)
    pingtime = pingtime.split("time=")
    pingtime = str(pingtime[1])
    pingtime = pingtime.split(" ")
    pingtime = str(pingtime[0])
    thetime = str(time.time())
    query = "INSERT INTO pingtimes (pingtime,thetime,thesite) VALUES ('"+pingtime+"','"+thetime+"','1')"
    cs.execute(query)
    return True
def dtCPU():
    psutil.cpu_times()
    cpu = str(psutil.cpu_percent(interval=1)) 
    return cpu

def dtMemory():    
    mem = psutil.virtual_memory()    
    mem = str(mem[2])
    return mem

def dtHDD():
    hdd = psutil.disk_usage('/')
    hdd = hdd[3]
    hdd = str(hdd)
    return hdd


query = "INSERT INTO info (cpu,hdd,ram) VALUES ('"+dtCPU()+"','"+dtHDD()+"','"+dtMemory()+"')"
cs.execute(query)

pingtime()

db.commit()

print("DONE!")
db.close()
