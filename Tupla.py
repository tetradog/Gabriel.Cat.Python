
def Limpia(tupla):
	"""si se anidan metodos que usan argumentos con *args estos se van poniendo en tuplas anidadas, pues este metodo devuelve la tupla original como si se tratara del primer metodo"""
	length=len(tupla)
	while length==1 and  type(tupla)==type(tupla[0]):
			tupla=tupla[0]
			length=len(tupla)
	return tupla
			
		