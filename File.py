import Tupla

def WriteLines(pathFile,*lines):
	lines=Tupla.Limpia(lines)
	with open(pathFile,'w') as file:
		for line in lines:
			file.write(str(line)+'\n')
def ReadLines(pathFile):
	lines=[]
	with open(pathFile,'r') as file:
		lines=file.readlines()
	return lines