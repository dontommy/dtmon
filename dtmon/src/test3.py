#!/usr/bin/env python
'''
Created on May 14, 2013

@author: dontommy
'''
import psutil
import time
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

BSsec = round(BSsec,2)
BRsec = round(BRsec,2)

