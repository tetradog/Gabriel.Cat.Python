import re
from GabrielCatPython import String
from GabrielCatPython.InternetSource import charRead
import os

def WriteLine(obj,*remplace):
	Write(obj,remplace,end='\n')
def Write(obj,*remplace,end=''):
    print(String.Format(obj,remplace),end=end)

def ReadLine(obj=''):
	return input(str(obj))
def ReadKey():
    strRead=str(charRead._Getch()())
    if len(strRead)>1:
        strRead=strRead[2:-1]
    return strRead
def Clear():
	os.system('cls' if os.name=='nt' else 'clear')
