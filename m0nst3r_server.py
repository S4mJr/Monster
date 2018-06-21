#!/usr/bin/python

import socket
from os import system
from sys import exit
from banner import ban
print ban


def handler():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ip = raw_input("Ip > ")
	port = input("Port > ")
	try:
		server.bind((ip, port))
		server.listen(5)
		print "\nListening in:" + ip + ":" + str(port)	
		(client_socket, address) = server.accept()	
		print "Conection received from: " +address[0]	
		while True:
			data = client_socket.recv(1024)
			print data		 
		server.close()	
	except Exception as erro:
		print "Erro:" + str(erro) 
		server.close()

def help():
	print "Commands"
	print "========="
	print "help - show help"
	print "start - start the listener (server)"
	print "update - update the tool"
	print "exit - close the tool\n"

def update():
	system('cd .. && git clone https://github.com/universalhacking/m0nst3r')

def start():
        port = input("Port > ")
	system('sudo nc -vlp %(port)s' % locals())

print "\n[!] Use: help [!]\n"
select = raw_input("mstr > ")
if select == 'help':
	help()
	enter = raw_input("Press Enter to Continue ...")
	system('reset')
	system('sudo python m0nst3r_server.py')
if select == 'start':
	start()
if select == 'update':
	update()
if select == 'exit':
	exit()
