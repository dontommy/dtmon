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

while 1:
    print("\n\t--== DT SERVER MONITORING--==\n")
    print("\tCPU Usage:\t"+dtCPU()+"%")
    print("\tRAM Usage:\t"+dtMemory()+"%")
    print("\tHDD Usage:\t"+dtHDD()+"%\n")
    
    network = psutil.network_io_counters()
    bytessend = network[0]
    bytesrecv = network[1]
    packsend = network[2]
    packrecv = network[3]


    uptime = psutil.get_users()
    uptime = uptime[0]
    upstart = uptime[3]

    upstop = time.time()

    secalive = upstop-upstart

    BSsec = bytessend/secalive
    BRsec = bytesrecv/secalive

    BSsec = str(round(BSsec/1024,2))
    BRsec = str(round(BRsec/1024,2))
    
    mbout = str(round(bytessend/1024,2))
    mbin = str(round(bytesrecv/1024,2))
    
    print("\tTraffic In:\t"+BRsec+" KB/Sec")
    print("\tTraffic Out:\t"+BSsec+" KB/Sec")

    print("\tTotal In:\t"+mbin+" KB")
    print("\tTotal Out:\t"+mbout+" KB\n")
    
    x = raw_input("Reload? y or n: ")
    if(x == 'y'):
        continue
    if(x == 'n'):
        break
