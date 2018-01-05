#定一个函数，函数打印一段话
def print_school():
	print("w3school是世界上最好的学校！！！")

#使用该函数
print_school()


#定义第二个函数，其中设定一个参数，并且打印输出该参数
def print_school2(obj):
	print("世界上最好的学校是\t" + obj.title() + "\t吧！")
#使用该函数

print_school2("测试学校姓名") 
#测试函数传参的类型，是字符串还是int整数型
def point_int(num_1):
	a = 10
	b = 10
	c = a * b + num_1
	
	print("这个是c的值：%d\n这个是num_1的值：%d\n"%(c,num_1))

#使用该函数
point_int(140)

