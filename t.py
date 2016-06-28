class myca(object):
	def __init__(self,name,value):
		self.name=name
		self.value=value
	def __repr__(self):
		return "%s repr %s"%(self.name,self.value)
	def __str__(self):
		return "%s str %s"%(self.name,self.value)
	@staticmethod
	def jingtaifun(self):
		return 'this is jingtai fangfa'
#c=myca('name.huang',78)

