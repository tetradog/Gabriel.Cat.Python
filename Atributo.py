import inspect

class Attribute:
	def _init_(self,*args):
		if len(args)==3:
			self.Type=args[0]
			self.Name=args[1]
			self.Value=args[2]
		else:
			self.Type=None
			self.Name=None
			self.Value=None
			
		
def GetAttribute(obj,attributeName):
	attribute=Attribute()
	attribute.Name=str(attributeName)
	atr=getattr(obj,str(attributeName))
	attribute.Type=type(atr)
	attribute.Value=atr
	return attribute
		
def GetAttributes(obj):
	for attr in dir(obj):
			if not attr.startswith('__'):
				if not callable(getattr(obj,attr)):
					yield GetAttribute(obj,attr)
		
