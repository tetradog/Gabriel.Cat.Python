#los objetos complejos tendran un metodo para obtener un serializador los simples los obtendrán por aqui
#el serializador tendrá dos metodos uno Serializar y otro Desserializar
import String
import Atributo

try:
	import cpickle as pickle
except ImportError:
	import pickle

class ISerializador:
	_partes=None
	@abstractmethod
	def GetSerializador(self):
		if self._partes == None:
			self._partes={}
			for atr in Atributo.GetAttributes(self):
				sel._partes+=Serializador.GetSerialitzer(atr.Value)
		return Serializador(self._Serializar,self._Desserializar)
	
	def _Serializar(self,obj):
		objSerializado={}
		atrs=Atributo.GetAttributes(obj)
		i=0
		f=len(atrs)
		while i<f:
			objSerializado+=self._partes[i].Serializar(atrs[i].Value)
			i+=1
		return objSerializado
	
	def _Desserializar(self,objVacio,datos):
				atrs=Atributo.GetAttributes(obj)
		i=0
		f=len(atrs)
		while i<f:
			setattr(objVacio,atrs[i].Name,self._partes[i].Desserializar(atrs[i].Value,datos))
			i+=1
		return objVacio
			
class Serializador:
	def __init__(self,*args):
		self._set_Serializar(args[0])
		self._set_Desserializar(args[1])
#creo que asi van las propiedades		
	def get_Serializar(self):
			return self.__Serializar
	def get_Desserializar(self):
		return self.__Desserializar
	def _set_Serializar(self,serializar):
		self.__Serializar=serializar
	def _set_Desserializar(self,deserializar):
		self.__Desserializar=desserializar
	
	@staticmethod
	def GetSerialitzer(obj):
		'''Devuelve el serializador para el objeto, si es un tipo creado debe contener el metodo GetSerialitzer que devuelve un objeto Serializador valido para serializar el objeto en cuestión '''
		serialitzer=None
		if _IsSimpleType(obj):
			serialitzer=_GetSimpleTypeSerialitzer(obj)
		elif not hasattr(obj,'GetSerialitzer'):
			raise Exception()
		else:serialitzer= obj.GetSerialitzer()
		return serialitzer

	@staticmethod
	def _IsSimpleType(obj):
		return String.Contains(str(type(obj)).lower(),"int|boolean|char|string|float|complex|bytes|bytearray|memoryview|")#añadir todos los tipos basicos de Python!
	@staticmethod
	def _GetSimpleTypeSerialitzer(obj):
		return Serializador(pickle.dumbs,_ToObj)
		
	@staticmethod
	def _ToObj(objVacio,datos):#lo necesito para poderlo usar de forma generica con los objetos complejos
		return pickle.loads(datos)
			
		