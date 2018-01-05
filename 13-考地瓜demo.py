class cook_digua:

	#初始化地瓜
	def __init__(self):
		"""开始初始化地瓜，并且设置属性"""
		self.cook_begin = "生的"
		self.cook_level = 0

	def __str__(self):
		"""打印信息"""
		return "当前的地瓜状态为%s,%d"%(self.cook_begin,self.cook_level)



digua = cook_digua()
digua.cook()
		
		
