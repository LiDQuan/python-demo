def add_txt():
	new_txt = input("请输入文档名字(如果不存在则新增，存在则输入内容会覆盖原有内容！！)\n\t")
	accont = input("请输入需要保存的文档：\n\t")
	#新建一个文件
	f = open('%s.txt'%new_txt,'w')
	#写入一个hello world
	f.write(accont)
	#最后保存并且关闭该文档
	f.close()

def read():
	#读取刚才存取的文件
	read_txt = input("请输入您想读取的文件名：\n\t")
	f = open('%s.txt'%read_txt,'r')
	print("***********下面是文件内容***********")
	print(f.read())
	print("***********上面是文件内容***********")
	#print("读取结束")
	f.close()

def change_txt():
	change_name = input("请输入您想追加内容的文件名：\n\t")	
	f = open('%s.txt'%change_name,'a')
	change_txt = input("请输入您想追加的内容：\n\t")	
	f.write(change_txt)
	f.close()

#主程序开始运行！！！！！！！！！！！！
while True:
#打印菜单
	print("")
	print("")
	print("")
	print("")
	print("*"*50)
	print("文件存取功能v0.1")
	print("1.新建文件")
	print("2.读取文件")
	print("3.追加内容")
	print("4.退出系统")
	print("*"*50)
	print("")
	print("")
	print("")
	print("")

#选择使用的功能
	num = int(input("输入功能序号:\n\t"))
	if num == 1:
		add_txt()
	elif num == 2:
		read()
	elif num == 3:
		change_txt()
	elif num == 4:
		break
	else:
		print("请输入正确的数字！！！！！！\n\t")
