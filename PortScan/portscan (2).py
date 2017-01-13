# -*- coding: utf-8 -*-
#!/usr/bin/python
# Python:      2.7
# Platform:    Windows
# Program:     端口扫描
# History:     2017.1.10
# version:     v 1.0




Port = [80,21,23,22,25,110,135,443,1080,3306,3389,1521,1433]  
Server = ['HTTP','FTP','TELNET','SSH','SMTP','POP3','HTTPS','SOCKS','MYSQL','Misrosoft RDP','Oracle','Sql Server']  
result = []  
  
import socket   
import sys  
import threading  
import time  
  
  
def get_host_name(Domain):  
    try:  
        return socket.gethostbyname(Domain)  
    except socket.error,e:  
        print '%s: %s'%(Domain,e)  
        return 0  
  
def scan(Domain,port,server):  
    temp = []  
    try:  
        s = socket.socket() 
        s.connect((Domain,port))  
        temp.append(port)  
        temp.append(server)  
        result.append(temp)  
        s.close()  
    except:  
        pass  
          
  
def output(Domain,IP):  
    if result:  
        print '\n'+Domain+': --> '+IP  
        print '\nThe Open Port:'  
        for i in result:  
            print Domain+': %4d -->%s'%(i[0],i[1])  
    else:  
        print 'None Port!'  
  
def main():  
    print ''' Port Scan 1.0\n\r\
 useag: PortScan [option] [IP] ./PortScan.py 127.0.0.1\n\r
'''
    arg = sys.argv
    IP = get_host_name(arg[1])
    print "Start Scan Port: " + IP
    print '\n'  
    for port,server in zip(Port,Server):  
        t = threading.Thread(target=scan,args=(arg[1],port,server,)) #每个端口开一个线程  
        t.setDaemon(True) #守护线程 
        t.start()  
        time.sleep(0.1) #线程时间间隔  
    output(arg[1],IP)  
  
if __name__=='__main__':  
    main()  


















