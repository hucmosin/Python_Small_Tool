#!/usr/bin/env python
# coding=utf-8

'''
====================================================================================
************************************************************************************
*
* lts.py - Port Forwarding.
*
* Copyright (C) 2017 .
*
* author:loveshell
* @date: 2012-7
*
* modify:mosin
* @date:2017-4
* @Blog:http://imosin.com
* python2.7 bulid
* Usage : D:\>lts.py
* ============================= Transmit Tool V1.0 ===============================
* =========== Code by Mosin & loveshell, Welcome to http://www.imosin.com ========
* ================================================================================
* :
* : [Usage of Port Forwarding:]
* :
* : [option:]
* : -listen
* : -tran
* : -slave
*
************************************************************************************
====================================================================================
'''

import socket
import sys
import threading
import time
import select

streams = [None, None]
LISTEN = "-listen"
SLAVE  = "-slave"
TRAN   = "-tran"

def usage():
    usage = '''
============================= Transmit Tool V1.0 ===============================
=========== Code by Mosin & loveshell, Welcome to http://www.imosin.com ========
================================================================================

[Usage of Packet Transmit:]
    lts.py -<listen|tran|slave> <option>
    lts.py -listen 4444 2222
    lts.py -tran 80 10.10.10.10:80
    lts.py -slave 10.10.10.10:4444 10.10.10.10:3389

[option:]

  -listen <ConnectPort> <TransmitPort>
  -slave  <ConnectHost>:<ConnectPort> <TransmitHost>:<TransmitPort>
  -tran   <TransmitPort> <ConnectHost>:<ConnectPort>
  
'''
    print usage
def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print ('[-] Create socket error.')
        return 0
    return sock
def switch_stream_flag(flag):
    if flag == 0:
        flag = "Server"
        return flag
    elif flag == 1:
        flag = "Client"
        return flag
    else:
        print "[!] Sock Error"
def get_stream(flag):
    if flag == 0:
        flag = 1
    elif flag == 1:
        flag = 0
    else:
        raise "[!] Socket ERROR!"
    while True:
        if streams[flag] == 'Exit':
            print("[-] Can't connect to the target, Exit!")
            sys.exit(1)
        if streams[flag] != None:
            return streams[flag]
        else:
            time.sleep(1)
def ex_stream(host, port, flag, server1, server2):
    flag_status = switch_stream_flag(flag)
    try:
        while True:
            buff = server1.recv(2048)
            if len(buff) == 0:
                print "[-] Data Send False. "
                break
            print  ('[*] %s Data Length %i Recv From => %s:%s' % (flag_status,len(buff),host,port))
            server2.sendall(buff)
            print  ('[*] %s:%i Send Data  => %s ' % (host,port,flag_status))
    except :
        print ('[-] Have One Connect Closed => %s' %(flag_status))
    try:
        server1.shutdown(socket.SHUT_RDWR)
        server1.close()
    except:
        print ('[!] %s => %s is down error.' % (host,port))
    try:
        server2.shutdown(socket.SHUT_RDWR)
        server2.close()
    except:
        print ('[!] %s => is down error.' % (flag_status))
    streams[0] = None
    streams[1] = None
    print ('[-] %s Closed.' %(flag_status))
def server(port, flag):
    host = '0.0.0.0' #端口复用修改
    server = create_socket()
    try:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(10)
    except:
        print ('[-] Bind False.')
    while True:
        conn, addr = server.accept()
        print ('[+] Connected from: %s:%s' % (addr,port))
        streams[flag] = conn
        server_sock2 = get_stream(flag) 
        ex_stream(host, port, flag, conn, server_sock2)
def connect(host, port, flag):
    connet_timeout = 0
    wait_time = 30
    timeout = 5
    while True:
        if connet_timeout > timeout:
            streams[flag] = 'Exit'
            print ('[-] Not connected %s:%i!' % (host,port))
            return None
        conn_sock = create_socket()
        try:
            conn_sock.connect((host, port))
        except Exception, e:
            print ('[-] Can not connect %s:%i!' % (host, port))
            connet_timeout += 1
            time.sleep(wait_time)
            continue
        print "[+] Connected to %s:%i" % (host, port)
        streams[flag] = conn_sock
        conn_sock2 = get_stream(flag) 
        ex_stream(host, port, flag, conn_sock, conn_sock2)
if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)
    t_list = []
    t_argv = [sys.argv[2], sys.argv[3]]
    for i in [0, 1]:
        s = t_argv[i] 
        if sys.argv[1] == LISTEN: 
            t = threading.Thread(target=server, args=(int(s), i))
            t_list.append(t)
        elif sys.argv[1] == SLAVE:  
            sl = s.split(':')
            t = threading.Thread(target=connect, args=(sl[0], int(sl[1]), i))
            t_list.append(t)
        elif sys.argv[1] == TRAN:
            try:
                if i == 0:
                    t = threading.Thread(target=server, args=(int(s), i))
                    t_list.append(t)
                elif i == 1:
                    sl = s.split(':')
                    t = threading.Thread(target=connect, args=(sl[0], int(sl[1]), i))
                    t_list.append(t)
                else:
                    usage()
            except:
                usage()
                sys.exit(0)
        else:
            usage()
            sys.exit(1)
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    sys.exit(0)
