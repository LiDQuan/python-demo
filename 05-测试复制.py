#1、打印菜单进入词语拼接，显示1-5组的操作菜单，退出系统

print("*"*50)
print("语句组成系统v1.0")
print("请根据菜单选择功能：")
print("1、进行语句拼接")
print("2、对第一组操作--时间组")
print("3、对第二组操作--地点组")
print("4、对第三组操作--人物组")
print("5、对第四组操作--事件组")
print("6、退出系统")
print("*"*50)

#2、实现功能，1-5组都拥有增删改查的功能，并且随机拼接语句
time = []
site = []
man = []
event = []
num = int(input("请选择您想使用的功能:\n"))
while True :
	if num == 1:
		pass
	elif num == 2:
		num_3 = int(input("您想对第二组进行什么操作：\n 1、新增\n 2、删除\n 3、修改\n 4、查找\n"))
		new_time = input("输入您想添加的时间信息:\n")
		if num_2 == 1:
			time.append(new_time)
			print(time)
		elif num_2 == 2:
			pass  #调用删除函数
	elif num == 3:
		pass
	elif num == 4:
		pass
	elif num == 5:
		pass
	elif num == 6:
		break
	else:
		print("您输入的信息有误，请重新输入！！")
