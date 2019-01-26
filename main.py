import Console
import String
import Atributo
#no van String.Match,String.Search

class Test:
	T=10
	A='a'
	@staticmethod
	def _none(self):
		return ''
t=Test()
for atr in Atributo.GetAttributes(t):
	Console.WriteLine('Nombre={0} Tipo={1} Valor={2}',atr.Name,atr.Type,atr.Value)
