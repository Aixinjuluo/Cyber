## For part3 NO.2 :
## we can add a random funtion in python. and put the range of the ports in to a array ot list.
## then you randomly scan the the port from the array/list. After you scan it, you move it out from
## the array/list. In this way, you can randomly scan all the ports in your input port range.

from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr
import sys


target = raw_input("[*] Enter Target IP Address: ")
min_port = raw_input("[*] Enter Minumum Port Number: ")
max_port = raw_input("[*] Enter Maximum Port Number: ")


ports = range(int(min_port), int(max_port)+1)

SYNACK = 0x12 
RSTACK = 0x14

def checkhost(ip): 

    try:
        ping = sr1(IP(dst = ip)/TCP(dport = 80, flags = "S")) 
        print ("\n[*] Target is Up, Beginning Scan...")
    except Exception as e:
        print ("\n[!] Couldn't Resolve Target")
        print ("[!] Exiting...")
        sys.exit(1)

def scanport(port1): 
    try:
        srcport = RandShort()
        ans, unans = sr(IP(dst = target)/TCP(sport = srcport, dport = port1, flags = "S"))

        print (ans.summary())

        result = ans[0][1].sprintf("%TCP.flags%")
        print (result)
        
        if result == "SA":
            return True
        else:
            return False
        
    except:
  
        RSTpkt = IP(dst = target)/TCP(sport = srcport, dport = port, flags = "R") 
        send(RSTpkt)
        print ("\n[*] User Requested Shutdown...")
        print ("[*] Exiting...")
        sys.exit(1)


def writeTo1(inP):
  with open ("halfscan.txt", "a") as fullscan:
    fullscan.write("open port : {}".format(inP))
    fullscan.write("\n")

def writeTo2(inP):
  with open ("halfscan.txt", "a") as fullscan:
    fullscan.write("close port : {}".format(inP) )
    fullscan.write("\n")

checkhost(target) 

for port in ports:
    status = scanport(port) 
    if status == True:
        print("*****************************")
        print ("Port " + str(port) + ": Open")
        writeTo1(port)
    else:
        print("##############################")
        print ("Port " + str(port) + ": close")
        writeTo2(port)


print ("\n[*] Scanning Finished!") 

## For part3 NO.2 :
## we can add a random funtion in python. and put the range of the ports in to a array ot list.
## then you randomly scan the the port from the array/list. After you scan it, you move it out from
## the array/list. In this way, you can randomly scan all the ports in your input port range.
