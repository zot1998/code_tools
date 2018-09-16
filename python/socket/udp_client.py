# -*- coding: UTF-8 -*-
import socket
import sys

LOCAL_IP   = '127.0.0.1'
LOCAL_PORT = 11111
REMOTE_IP  = '127.0.0.1'
REMORT_PORT = 5555

address = (REMOTE_IP, REMORT_PORT)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((LOCAL_IP, LOCAL_PORT))
        
    args = sys.argv[1:]
    args = ' '.join(args)
    	
    if args:
        s.sendto(args, address) 
    else:
        s.sendto('This is a test message.', address) 

except Exception as e:
    print "Exception:"+str(e)

s.close()
