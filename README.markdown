	  ____                                             _   
	 / ___|_ __   ___  _ __ ___   ___ _ __ _   _ _ __ | |_ 
	| |  _| '_ \ / _ \| '_ ` _ \ / __| '__| | | | '_ \| __|
	| |_| | | | | (_) | | | | | | (__| |  | |_| | |_) | |_ 
	 \____|_| |_|\___/|_| |_| |_|\___|_|   \__, | .__/ \__|
										   |___/|_|        


What the shell is this?
=======================

	One day, I have woken up with feeling that my system is missing something.
	There was no way how to easily decrypt single files with symetric AES crypths.
	
	So I have implemented that by my own. That crypt.py lib may be little 
	random so if you have any ideas how to make it better feel free to say it.
	
What do I need to use it?
=========================
	- Zenity Framework
	- Nautilus-actions manager
	
How to install it?
==================
	- download source
	- import actions via nautilus-actions-manager
	- edit path to the executables
	- you are done.
	
How to use it?
==============
	When you click on a file, there should be icon with Gnomcrypt label, click it
	dialog should appear and than Gnomcrypt will encrypt/decrypt file. 
	(it´s automatically decrypting when file ends with ".aes" or ".taes")


TODO: 
=====
   1) review of the crypt library
