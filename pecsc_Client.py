from Tkinter import *
import tkMessageBox
import socket
import ssl

HEIGHT = 200
WIDTH = 100
keeplooping = True
HOST = raw_input("Server IP: ")
PORT = raw_input("Server Port: ")

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
  messagebox.delete(0, "end")
  print "%s: %s" % (user, msg)
  
def refreshChat():
  print "refresh chat"
  
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
messagebox = Entry(content)
messagebox.grid(column=0, row=1)
sendButton = Button(content, text="Send", command=sendMessage)
sendButton.grid(column=1, row=1)
root.mainloop()  
# END CLIENT GUI CODE

# main client loop
"""
while keeplooping == True:
  refreshChat()
  refreshUserList()
  userlist = getUsers()
  
"""
























