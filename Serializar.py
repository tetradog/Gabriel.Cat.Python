import Atributo
import String
try:
    import cpickle as pickle
except ImportError:
    import pickle

def Serialitze(obj):
	return None

def _Serialitze_Obj(obj):
    atributos=Atributo.GetAttributes(obj)
	#por mirar
    for atr in atributos:
        if IsSimpleType(atr.Type):
			yield _SerialitzeSimpleType(atr.Value)
        elif hasattr(atr.Value,"__iter__"):
            yield _SerialitzeSimpleType(len(atr.Value))#serializo la longitud de la array para poderla cargar
            for atrArray in atr.Value:
				#simple o complejo y falta la longitud...???
                if _IsSimpleType(atrArray):
                    yield _SerialitzeSimpleType(atrArray)
                else:
                    for atrArrayBin in _Serialitze_Obj(atrArray):
                        yield atrArrayBin
        else:
			for atrBin in _Serialitze_Obj(atr.Value):
				yield atrBin
def _IsSimpleType(obj):
	#si es un tipo simple devuelve true
    return String.Contains(str(type(obj)).lower(),"int|boolean|char|string|float|complex|bytes|bytearray|memoryview|")#añadir todos los tipos basicos de Python!
def _SerialitzeSimpleType(obj):
    if not obj == None:#mirar que sea así!
        bytes={0x1} + pickle.GET(obj)
    else:
        bytes={0x0}
    return bytes