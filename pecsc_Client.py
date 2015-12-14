from Tkinter import *
import tkMessageBox
import socket
import base64

HEIGHT = 200
WIDTH = 100
keeplooping = True
HOST = raw_input("Server IP: ")
PORT = input("Server Port: ")

# FUNC DEF's
def encode(key, clear):
  enc = []
  for i in range(len(clear)):
    key_c = key[i % len(key)]
    enc_c = chr(ord(clear[i]) + ord(key_c) % 256)
    enc.append(enc_c)
  return base64.urlsafe_b64encode("".join(enc))
  
def decode(key, enc):
  dec = []
  enc = base64.urlsafe_b64decode(enc)
  for i in range(len(enc)):
    key_c = key[i % len(key)]
    dec_c = chr(ord(enc[i]) - ord(key_c) % 256)
    dec.append(dec_c)
  return "".join(dec)

def getUsername():
  username = raw_input("Username: ")
  return username

def getUsers():
  print "get user list"

def callback():
  print "callback for testing purposes"
  
def about():
  print "open about box"
  tkMessageBox.showinfo("About PECSC", "PECSC - Python Encrypted Chat Server/Client - coded by: 0x0derp")

def sendMessage():
  user = usernameEntry.get()
  msg = messagebox.get()
  key = encryptionKeyEntry.get()
  encodedMSG = encode(key, msg)
  messagebox.delete(0, "end")
  sock.send(encodedMSG)
  print "%s: %s" % (user, msg)
  print "%s: %s" % (user, encodedMSG)
  
def refreshChat():
  print "refresh chat"
# END FUNC DEF's

# connect to the chat server first
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
sock.connect((HOST, PORT))

# CLIENT GUI CODE
root = Tk()
content = Frame(root)
content.grid(column=0, row=0)
root.title("PECSC - Client")
frame = Frame(content, height=HEIGHT, width=WIDTH)
frame.grid(column=0, row=0, columnspan=2, rowspan=2)
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
usernameLabel = Label(content, text="username:")
usernameLabel.grid(column=0, row=0)
usernameEntry = Entry(content)
usernameEntry.grid(column=1, row=0)
encryptionKeyLabel = Label(content, text="En/De-cryption Key:")
encryptionKeyLabel.grid(column=0, row=1)
encryptionKeyEntry = Entry(content)
encryptionKeyEntry.grid(column=1, row=1)
messagebox = Entry(content)
messagebox.grid(column=0, row=2)
sendButton = Button(content, text="Send", command=sendMessage)
sendButton.grid(column=1, row=2) 
root.mainloop()
# END CLIENT GUI CODE

# main client loop - mostly looping to check for messages from the other clients
"""
while keeplooping == True:
  refreshChat()
  refreshUserList()
  userlist = getUsers()
  
"""
