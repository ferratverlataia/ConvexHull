class Puntos:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __add__(self,t):
		b= Vectores(self.x+t.x,self.y+t.y)
		return b
	
	