#!/usr/bin/env python
'''
Created on May 8, 2013

@author: dontommy
'''
import curses
import psutil
import sys
import time
import thread    

def dtCPU():
    psutil.cpu_times()
    cpu = str(psutil.cpu_percent(interval=1)) 
    cpu = cpu+"%"
    return cpu

def dtMemory():    
    mem = psutil.virtual_memory()    
    mem = str(mem[2])
    mem = mem+"%"
    return mem

def dtHDD():
    hdd = psutil.disk_usage('/')
    hdd = str(hdd[3])
    hdd = hdd+"%"
    return hdd

while True:
    myscreen = curses.initscr()
    curses.curs_set(0)
    myscreen.border(0)
    myscreen.addstr(5,20,"DT Server Monotoring",curses.A_BOLD)
    myscreen.addstr(7,20,"CPU:")
    myscreen.addstr(8,20,"Memory:")
    myscreen.addstr(9,20,"Harddisk:")
    
    myscreen.addstr(7,30,dtCPU())
    myscreen.addstr(8,30,dtMemory())
    myscreen.addstr(9,30,dtHDD())
    myscreen.refresh()
    myscreen.getch()
    curses.endwin()