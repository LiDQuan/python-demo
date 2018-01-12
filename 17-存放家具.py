class Room:
	def __init__(self, new_area, new_model, new_addr):
		"""初始化房子的属性"""
		self.area = new_area	#房子的总面积
		self.model = new_model	#房子的户型
		self.addr = new_addr	#房子的地理位置
		self.re_area = new_area	#房子的可用面积
		self.fur_item = []		#房子现有家具

	def __str__(self):
		"""开始打印房子的具体信息"""
		msg = "目前房子的信息：\n\t房子的总面积为：%d平方米，房子的户型为：%s，房子的位置在：%s。"%(self.area, self.model, self.addr)
		msg += "\n目前房子的具体信息为：\n\t房子的总面积为:%d,房子的可用面积为:%d,房子现有家具为:%s"%(self.area, self.re_area, str(self.fur_item))
		return msg

	def add_fur(self, item):
		"""增加家具进入房子函数"""
		self.re_area -= item.get_area() 
		self.fur_item.append(item.get_name())

class Bed:
	def __init__(self, new_area, new_name):
		""" 初始化床类家具的信息 """
		self.area = new_area	#家具的占地面积
		self.name = new_name	#家具的名字
		
	def __str__(self):
		"""打印床的具体属性"""
		return "该床的名字为\t%s\t,且该床的占地面积为\t%d\t"%(self.name, self.area)

	#get方法应该放在家具类中，让房子类进行调用，而不是放在房子类中
	def get_area(self):
		"""获取家具的属性"""
		return self.area

	def get_name(self):
		"""获取家具的属性"""
		return self.name

fangzi = Room(500,"十室三厅","南宁市 中窑路 11号 10栋 666房")
print(fangzi)

chuang = Bed(6,"西蒙斯床垫")
print(chuang)
fangzi.add_fur(chuang)

