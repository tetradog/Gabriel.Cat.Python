
import Serializar

class Test(Serializar.ISerializar):
	def __init__(self,*args):
		if len(args)==2:
			self.T=args[0]
			self.J=args[1]
		else:
			self.T='t'
			self.J=10

t=Test('Ja',1)
serializador=Serializar.GetSerialitzer(t)
tSerializado=serializador.Serializar(t)
j=serializador.Desserializar(Test(),tSerializado)

if t.T==j.T and t.J==j.J:
	print('funciona')
