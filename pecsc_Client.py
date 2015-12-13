from Tkinter import *
import tkMessageBox

HEIGHT = 300
WIDTH = 300

# *************************
# FUNCTION CODE
def callback():
  print "callback for testing purposes"

def callback_connect():
  print "open connection box"
  
def about():
  print "open about box"
  tkMessageBox.showinfo("About PECSC", "coded by: 0x0derp")
# *************************

root = Tk()
root.title("PECSC - Client")
helloLabel = Label(root, text="PECSC Client")
helloLabel.pack()

# *************************
# FRAME CODE

# *************************

# *************************
# MENU CODE

# create menu object
menu = Menu(root)
root.config(menu=menu)
# menu inside of menu object
filemenu = Menu(menu)
# add menu button named "File"
menu.add_cascade(label="File", menu=filemenu)
# add options to the filemenu
filemenu.add_command(label="Connect...", command=callback_connect)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

# move onto the help menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
# *************************

root.mainloop()
