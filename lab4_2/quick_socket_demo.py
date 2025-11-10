# quick_socket_demo.py
#port scanning

import socket, sys, time

host = "scanme.nmap.org"                #domain or ip address we want to test
port = 8080  # try different ports.       This is the specific network port we're checking

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #socket.AF_INET means we're using ipv4 and socket.SOCK_STREAM means we're using tcp protocol
s.settimeout(3.0)  # 3 second timeout. So if a connection takes longer than 3 seconds, it will abort
start = time.time()     #starting the timer
try:
    s.connect((host, port))                         #trying to establish a tcp connection to the target
    print(f"Connected to {host}:{port}")            #if it's successful this will print out
    s.close()
except socket.timeout:                          #if there's no response withing 3 seconds
    print("Connection timed out")               #the host is unreachable
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    print(f"Elapsed: {time.time()-start:.2f}s")     #calculates how long the attempt took