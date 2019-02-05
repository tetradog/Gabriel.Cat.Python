import re
import String
import InternetSource.charRead
import os

def WriteLine(obj,*remplace):
	Write(obj,remplace,end='\n')
def Write(obj,*remplace,end=''):
    print(String.Format(obj,remplace),end=end)

def ReadLine(obj=''):
	return input(str(obj))
def ReadKey():
    strRead=str(InternetSource.charRead._Getch()())
    return strRead[2:-1]
def Clear():
	os.system('cls' if os.name=='nt' else 'clear')