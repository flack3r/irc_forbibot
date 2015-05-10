import socket
import time
import datetime
from telnetlib import *
network = 'irc.hanirc.org'
port = 6667
prefix = '!'
 

irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

irc.connect ((network, port))
 
irc.send ('USER forbibot forbibot forbibot : flack_bot \n')
time.sleep(1)
print irc.recv(1024)
print "[*]send user"
irc.send ('NICK forbibot'+'\n')

buf = irc.recv(1024).split()
tmp = buf[1]
ping = tmp[1:]
print ping
irc.send ('PONG :'+ping+"\n")
irc.send ( 'JOIN #fbk\n' )

#irc.send ('PRIVMSG #fbk HI, forbidden~!')

while True:
	data = irc.recv (4096)
 	if data.find('PING') != -1:
 		print "[*]send pong~"
 		ping = data.split(":")[1]
 		irc.send('PONG :'+ping+"\n")

 	if data.find ( 'PRIVMSG' ) != -1:
		nick = data.split ( '!' ) [ 0 ].replace ( ':', '' )
		message = ':'.join ( data.split ( ':' ) [ 2: ] )
		print nick + ':', message

		if message.find('!hi') != -1:
			irc.send("privmsg #fbk hi\n")

		elif message.find('!time') != -1:
			now = time.localtime()
			s = "%04d-%02d-%02d/%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
			irc.send("privmsg #fbk "+s+'\n')

		