#!/usr/bin/env python
'''
Created on May 8, 2013

@author: dontommy
'''

import psutil
import sys
import time
    

def dtCPU():
    psutil.cpu_times()
    cpu = str(psutil.cpu_percent(interval=1)) 
    return cpu+"%"

def dtMemory():    
    mem = psutil.virtual_memory()    
    mem = str(mem[2])
    return mem+"%"

def dtHDD():
    hdd = psutil.disk_usage('/')
    hdd = str(hdd[3])
    return hdd+"%"
print("\n\t    --== DT SERVER MONITORING ==--")
print("\t\tRAM:\tCPU:\tHDD:")
while True:
    sys.stdout.write("\r")
    sys.stdout.write("\t\t"+dtMemory() + "\t" + dtCPU() + "\t" + dtHDD())
    sys.stdout.flush()
    time.sleep(.5)