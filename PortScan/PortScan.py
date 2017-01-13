# -*- coding: utf-8 -*-

import optparse
import socket
import sys

def connScan(targrt_host,target_port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((targrt_host,target_port))
        sock.send('PortScan\r\n')
        results = sock.recv(100)
        print '[+]%d/port open ' % target_port
        print '[+] ' + str(results)
        sock.close()
    except socket.error:
        print '[-]%d/port close' % target_port

def portscan(targrt_host,target_ports):
    try:
        targrt_IP = socket.gethostbyname(targrt_host)
    except:
        print "[-] Cannot resolve '%s': Unknown host" %targrt_host
        return
    try:
        target_name = socket.gethostbyaddr(targrt_IP)
        print '\n[+] Scan Result for : ' + target_name[0]
    except:
        print '\n[+] Scan Result for : ' + target_IP
    socket.setdefaulttimeout(1)
    for target_port in target_ports"""range(start_port,end_port)""":
        print 'Scan port ' + target_port
        connScan(targrt_host,int(target_port))

def main():
    parser = optparse.OptionParser("usage%prog 555")
    parser.add_option('-H', dest = 'target_host', type ='string',help='Your target host')
    parser.add_option('-p', dest = 'target_port',type = 'string',help='Your target port')

   
    (options,args) = parser.parse_args()
    
    host = options.target_host
    port = str(options.target_port).split(',')
    if (host == None) | (port[0] == None):
        print '[-] You must specify a target host and port.'
        exit(0)
    portscan(host,port)
    """
    start_port = options.start_port
    end_port = options.end_port
    
"""




if __name__ == '__main__':

    main()













