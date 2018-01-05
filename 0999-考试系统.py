class Stu:
	"""定义一个学生类用于考试"""
	def __init__(self, new_name, new_sex):
		"""初始化学生的各科成绩和姓名，性别"""
		self.name = new_name
		self.grade_all = 0
		self.sex = new_sex

	def __str__(self):
		"""打印学生的当前情况函数"""
		return "当前的学生信息为:\n姓名:\n\t%s\n性别:\n\t%s\n总成绩:\n\t%d"%(self.name, self.sex, self.grade_all)

	def get_name(self):
		"""返回学生名字"""
		return self.name

	def get_sex(self):
		"""返回学生性别"""
		return self.sex

	def get_grade(self):
		"""返回学生总成绩"""
		pass
	
class Test():
	"""考试测试类"""
	def __init__(self):
		"""初始化各科成绩"""
		self.chinese_grade = 0                         #语文成绩
		self.match_grade = 0                           #数学成绩  
		#self.choose_num = 0                            #选择器

	def __str__(self):
		"""返回打印学生成绩"""
		pass

	def testing(self):
		"""开始考试"""
		print("i like sun")



	def print_menu(self, new_stu):
		"""打印考试系统菜单"""
		print("*"*50)
		print("**********欢迎进入考试系统**********")
		print("考生 %s 欢迎你进入考试系统"%(new_stu.name))
		print("1、开始考试")
		print("2、退出系统")
		print("*"*50)
		self.choose_num()

	def choose_num(self):
		flag = True
		while flag:
			self.choose_num = input("请选择你想使用的功能：\n\t")
			if str(self.choose_num).isdigit() == True:
				self.choose_num = int(self.choose_num)
				if self.choose_num == 1:
					self.testing()
				elif self.choose_num == 2:	
					flag = False
					break
				else:
					print("*"*50)
					print("\n\t您输入的数字错误，请重新输入!!!\n\t")
					print("*"*50)
			else:
				print("*"*50)
				print("\n\t您输入的不是数字，请重新输入!!!\n\t")
				print("*"*50)


stu1 = Stu("laowang","男")
kaoshi = Test()
kaoshi.print_menu(stu1)
#print(stu1)

