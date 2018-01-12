#定义一个列表存放name
names = []

#定义一个函数打印各项功能，增删改查
def print_menu():
	print("*"*50)
	print("欢迎使用名片管理系统v1.0")
	print("请根据提示选取想使用的功能：")
	print("---> 1.新增名字")
	print("---> 2.删除名字")
	print("---> 3.修改名字")
	print("---> 4.查找名字")
	print("---> 5.查看所有名字")
	print("---> 6.保存文件")
	print("---> 7.退出系统")
	print("*"*50)

#增加
def add_name():
	new_name = input("请输入想新增的名字:\n")
	names.append(new_name)
	print(names)

#删除
def del_name():
	re_name = input("请输入想要删除的名字:\n")
	names.remove(re_name)
	print(names)

#修改
def update_name():
	print(names)
	up_num = int(input("请输入想修改名字的序号:\n"))
	up_name = input("请输入新的名字:\n")
	names[up_num-1] = "%s"%up_name
	print(names)

#查找
def find_names():
	find_name = input("请输入想要查找的名字：\n")
	if find_name in names:
		print("您想要查找的名字在列表中！！！")
	else:
		print("查无此人。。。")

#显示所有名字
def print_all_name():
	print(names)

#保存文件函数
def save_2_file():
	f = open("update.lidata","w")
	f.write(str(names))
	f.close

#根据用户输入的各项指令进行相应的功能。
def main():
	#读取储存记录
	try:
		global names

		f = open("update.lidata")

		names = eval(f.read())

		f.close

	except Exception:
		pass


	while True:
		print_menu()
		num = int(input("请输入您想使用的功能："))
		if num == 1 :
			add_name()
		elif num == 2 :
			del_name()
		elif num == 3 :
			update_name()
		elif num == 4 :
			find_names()
		elif num == 5 :
			print_all_name()
		elif num == 6 :
			save_2_file()
		elif num == 7 :
			break
		else:
			print("输入错误，请您重新输入！！！！！")


if __name__ ==  "__main__":
	main()
