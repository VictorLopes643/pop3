#!/usr/bin/python
import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.100.8",110))
    r = s.recv(1024)
    print r
    s.send("USER test\r\n")
    r = s.recv(1024)
    print r
    s.send("PASS test\r\n")
    r = s.recv(1024)
    print r
    s.send("QUIT\r\n")
    r = s.recv(1024)
    print r
except:
    print "ERRO AO CONECTAR"
