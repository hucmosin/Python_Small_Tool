#!/usr/bin/env python

 
def telnetdo(HOST=None, USER=None, PASS=None, COMMAND=None): #define a function
    import telnetlib, sys
    if not HOST:
        try:
            HOST = sys.argv[1]
            USER = sys.argv[2]
            PASS = sys.argv[3]
            COMMAND = sys.argv[4]
        except:
            print "Usage: telnetdo.py host user pass command"
            return
    msg = ['Debug messages:\n'] #
    tn = telnetlib.Telnet() #
    try:
        tn.open(HOST)
    except:
        print "Cannot open host"
        return
     
        #msg.append(tn.expect(['login:'], 5)) #
     
        tn.read_until("login:")
    tn.write(USER + '\n')
    if PASS:
        #msg.append(tn.expect(['Password:'], 5))
        tn.read_until("Password:")
        tn.write(PASS + '\n')
        
        #msg.append(tn.expect([USER], 5))
     
        tn.write(COMMAND + '\n')
        tn.write("exit\n")
     
        #msg.append(tn.expect(['#'], 5))
     
        tmp = tn.read_all()
    tn.close()
    del tn
    return tmp
     
if __name__ == '__main__':
    print telnetdo()
