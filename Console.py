import re
import String

def WriteLine(obj,*remplace):
	Write(obj,remplace,end='\n')
def Write(obj,*remplace,end=''):
    print(String.Format(obj,remplace),end=end)

def ReadLine(obj=''):
	return input(str(obj))