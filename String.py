import re
import Tupla

def Format(string,*args):
	i=0
	string=str(string)
	args=Tupla.Limpia(args)
	f=len(args)
	while i<f:
		ptrn='\{'+str(i)+'\}'
		patron=re.compile(ptrn)
		strAPoner=str(args[i])
		string=patron.sub(strAPoner,string)
		i+=1
	return string

def Split(string,*strsSplit):
	strSplit=''
	strsSplit=Tupla.Limpia(strsSplit)
	if len(strsSplit)==0:
		strsSplit=(';')#mejor pongo un caracter por defecto
		#raise Exception()#se necesitan caracteres para el split
	for s in strsSplit:
		strSplit+=s+'|'
	
	return re.split(strSplit[:-1],string)

	