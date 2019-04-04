#full connection in python
# Gary Lewandowski
from socket import *

ip = input ("Enter your IP : ")
startPort = input ("Enter you start port : ")
endPort = input ("Enter your end port : ")

def writeTo1(inP):
  with open ("fullscan.txt", "a") as fullscan:
    fullscan.write("open port : {}".format(inP))
    fullscan.write("\n")

def writeTo2(inP):
  with open ("fullscan.txt", "a") as fullscan:
    fullscan.write("close port : {}".format(inP) )
    fullscan.write("\n")
  
def connectTo(host, port):
  serverName = host
  serverPort = port
  clientSocket = socket(AF_INET,SOCK_STREAM)
  clientSocket.settimeout(1)
  try:
    clientSocket.connect((serverName,serverPort))
    clientSocket.close()
    print ("connect")
    return True
  except Exception as e:
    # didn't connect
    clientSocket.close()
    print ("disconect")
    return False


scanPort = range (int(startPort), int(endPort)+1)
try:
  for port in scanPort:
    result = connectTo(ip, port)
    if result == 1:
      print ("open---------", port)
      writeTo1(port)
      
    else:
      print("close", port)
      writeTo2(port)
except Exception as e:
  # didn't connect
  clientSocket.close()


