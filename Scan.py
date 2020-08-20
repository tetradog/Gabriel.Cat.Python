#!/usr/bin/env python #2.7
import socket
import subprocess
import sys
from datetime import datetime
from GabrielCatPython import Console

class ScannedPort:
	def __init__(self,port,isOpen):
		self.Port=port
		self.IsOpen=isOpen

# Print a nice banner with information on which host we are about to scan
def Scan(ip,initPort,endPort):
	try:
		for port in range(initPort,endPort):
			sock = socket.socket(socket.AF_INET, 			   socket.SOCK_STREAM)
			result = sock.connect_ex((ip, port))
			isOk=result == 0
			if isOk:
				sock.close()	
			yield ScannedPort(port,isOk)
	except KeyboardInterrupt:
		Console.WriteLine("You pressed Ctrl+C")
	except socket.gaierror:
		Console.WriteLine ('Hostname could not be resolved. Exiting')
	except socket.error:
		Console.WriteLine("Couldn't connect to server")

def GetOpenPorts(ip,initPort,endPort):
	for port in Scan(socket.gethostbyname(ip),initPort,endPort):
		if port.IsOpen:
			yield port.Port
			
def GetOpenPortsArray(ip,initPort,endPort):
	portOpened=[]
	for port in GetOpenPorts(ip,initPort,endPort):
		portOpened.append(port)
	return portOpened
	
