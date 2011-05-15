#! /usr/bin/python
# -*- coding: UTF-8 -*-

# @author: 	Visgean Skeloru 
# email: 	<visgean@gmail.com
# jabber: 	<visgean@jabber.org
# github: 	http://github.com/Visgean


import crypt
import sys
import subprocess
import pynotify
import shlex



def runCommand(commandString):
    "Run command outside python"
    cmd = subprocess.Popen(shlex.split(commandString),
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            )
    OUT, ERR = cmd.communicate()
    
    return OUT

def encrypt():
    cryptat.encryptFile()
    notifyString = "%s was encrypted." % filePath
    notif = pynotify.Notification("Gnomcrypt", notifyString)
    notif.show()

def decrypt():
    cryptat.decryptFile()
    notifyString = "%s was decrypted." % filePath
    notif = pynotify.Notification("Gnomcrypt", notifyString)
    notif.show()


filePath = " ".join(sys.argv[1:])



password = runCommand(commandString='''zenity --entry --title="Gnomcrypt" --text="Enter password:" --hide-text --window-icon=/usr/share/icons/gnome-colors-common/scalable/status/locked.svg''')
password = password.splitlines()[0] # there is for some reason line on the end of the string

cryptat = crypt.FileContainer(filePath, password)



if filePath[-4:] == ".aes" or filePath[-5:] == ".taes":
    decrypt()
else:
    encrypt()

