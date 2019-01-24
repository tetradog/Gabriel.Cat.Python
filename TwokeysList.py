class TwoKeysList:
	
	#atributos
	_dic1=dict()
	_dic2=dict()
	_dic12=dict()
	_dic21=dict()
	
	_typePair=type({1,1})
		
	def Add(self,key1,key2,value):
		if key1 in self._dic1:
			raise KeyDuplicatedException(key1)
		elif key2 in self._dic2:
			raise KeyDuplicatedException(key2)
		self._dic1.update({key1:value})
		self._dic2.update({key2:value})
		self._dic12.update({key1:key2})
		self._dic21.update({key2:key1})
		
	def ContainsKey1(self,key1):
		return key1 in self._dic1
	def ContainsKey2(self,key2):
		return key2 in self._dic2
	def ContainsKey(self,key):
		return self.ContainsKey1(key) or self.ContainsKey2(key)

	def GetValue(self,key):
		value=None
		if key in self._dic1:
			value=self.GetValueWithKey1(key)
		elif key in self._dic2:
			value=self.GetValueWithKey2(key)
		return value	
			
	def GetValueWithKey1(self,key1):
		if key1 not in self._dic1:
			raise KeyNotFoundException(key1)
		return self._dic1[key1]
	def GetValueWithKey2(self,key2):
		if key2 not in self._dic2:
			raise KeyNotFoundException(key2)
		return self._dic2[key2]

	def GetKey1(self,key2):
		if key2 not in self._dic2:
			raise KeyNotFoundException(key2)
		return self._dic21[key2]
	def GetKey2(self,key1):
		if key1 not in self._dic1:
			raise KeyNotFoundException(key1)
		return self._dic12[key1]
	
	def RemoveWithKey1(self,key1):
		self._Remove(self._dic1,self._dic2,self._dic12,self._dic21,key1)

	def RemoveWithKey2(self,key2):
		self._Remove(self._dic2,self._dic1,self._dic21,self._dic12,key2)

	def Remove(self,key):
		if key in self._dic1:
			self.RemoveWithKey1(key)
		elif key in self._dic2:
			self.RemoveWithKey2(key)
	def UpdateValue(self,key,value):
		if key in self._dic1:
			self.UpdateValueWithKey1(key,value)
		elif key in self._dic2:
			self.UpdateValueWithKey2(key,value)

	def GetKey(self,key):
		other=None
		if key in self._dic1:
			other=self.GetKey2(key)
		elif key in self._dic2:
			other=self.GetKey1(key)
		return other

	def UpdateValueWithKey1(self,key1,value):
		self._UpdateValue(self._dic1,self._dic2,self._dic12,key1,value)

	def UpdateValueWithKey2(self,key2,value):
		self._UpdateValue(self._dic2,self._dic1,self._dic21,key2,value)		
	def _UpdateValue(self,dic1,dic2,dic12,key1,value):
		if key1 not in dic1:
			raise KeyNotFoundException(key1)
		dic1[key1]=value
		dic2[dic12[key1]]=value

	def UpdateKey1(self,key1Old,key1New):
		if key1Old not in self._dic1:
			raise KeyNotFoundException(key1Old)
				
		key2=self._dic12[key1Old]
		value=self._dic1[key1Old]
		self.RemoveWithKey1(key1Old)
		self.Add(key1New,key2,value)
		
	def UpdateKey2(self,key2Old,key2New):
		if key2Old not in self._dic2:
			raise KeyNotFoundException(key2Old)
				
		key1=self._dic21[key2Old]
		value=self._dic2[key2Old]
		self.RemoveWithKey2(key2Old)
		self.Add(key1,key2New,value)
		
			
	def _Remove(self,dic1,dic2,dic12,dic21,key1):
		if key1 in dic1:
			del dic1[key1]
			del dic2[dic12[key1]]
			del dic21[dic12[key1]]
			del dic12[key1]
	def Clear(self):
		self._dic1.clear()
		self._dic2.clear()
		self._dic12.clear()
		self._dic21.clear()
	def Count(self):
		return len(self._dic1)
	def Items(self):
		value=None
		for key1,key2 in self._dic12.items() :
			value=self._dic1[key1]
			yield (key1,key2,value)
	def Keys(self):
		return self._dic12.items()
	def Values(self):
		return self._dic1.values()

#actuar como dict https://stackoverflow.com/questions/4014621/a-python-class-that-acts-like-dict
	def __iter__(self):
		return self.Items()
	def __getitem__(self,key):
		return self.GetValue(key)
	def __setitem__(self,key,value):
		if hasattr(key,'__iter__'):#(key1,key2) es una array
			self.Add(key[0],key[1],value)
		else:
			self.UpdateValue(key,value)

	def __contains__(self,key):
		return self.ContainsKey(key)
	def __delitem__(self,key):
		self.Remove(key)
	def __len__(self):
		return self.Count()
class KeyNotFoundException(Exception):
	keyNotFound=None
	def __init__(self, *args, **kwargs):
		self.keyNotFound=args[0]
	def __str__(self):
		return str(self.keyNotFound)

class KeyDuplicatedException(Exception):
	keyDuplicated=None
	def __init__(self, *args, **kwargs):
		self.keyDuplicated=args[0]
	def __str__(self):
		return str(self.keyDuplicated)
