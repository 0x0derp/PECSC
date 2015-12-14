import sys
import socket

HOST = raw_input("Server IP: ")
PORT = input("Server Port: ")
MAXCLI = input("Maximum number of Clients: ")
userList = ["firstip"]

def updateClientList():
  print "update client list"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(MAXCLI)

for index in range(MAXCLI):
  conn, addr = sock.accept()
  print "Connection by: ", addr
  userList[index] = addr
  
# echo users' messages to each other (like a chatroom hopefully)
while True:
  retrieveMSG = sock.recv(1026)
  print retrieveMSG
  if retrieveMSG == "killserver":
    sys.exit(0)
  for ip in userList:
    sock.sendto(retrieveMSG, ip)
