#!/usr/bin/env python
'''
Created on May 8, 2013

@author: dontommy
'''
import psutil


# CPU % Usage
psutil.cpu_times()
cpu = psutil.cpu_percent(interval=1)
print "CPU % Usage: ",cpu

# RAM/Memory % Usage
mem = psutil.virtual_memory()
print "RAM/Memory % Usage: ",mem[2]

# Harddisk % Usage
hdd = psutil.disk_usage('/')
print "Harddisk % Usage: ",hdd[3]

