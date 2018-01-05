import random
#1、打印菜单进入词语拼接，显示1-5组的操作菜单，退出系统
#2、实现功能，1-5组都拥有增删改查的功能，并且随机拼接语句
time = []
site = []
man = []
event = []
flag = True
num_flag = True
while flag :
	print("*"*50)
	print("语句组成系统v1.1")
	print("请根据菜单选择功能：")
	print("1、进行语句拼接")
	print("2、对第一组操作--时间组")
	print("3、对第二组操作--地点组")
	print("4、对第三组操作--人物组")
	print("5、对第四组操作--事件组")
	print("6、显示所有组的成员信息")
	print("7、退出系统")
	print("*"*50)
	num = int(input("请选择您想使用的功能:\n\t"))

	if num == 1:
	#开始定义各组的变量名
		len_time = len(time)
		len_site = len(site)	
		len_man = len(man)	
		len_event = len(event)
		print("%s%s%s%s?"%(time[random.randint(0,len_time-1)],site[random.randint(0,len_site-1)],man[random.randint(0,len_man-1)],event[random.randint(0,len_event-1)]))	
	#操作时间列表信息
	elif num == 2:
		#新增1组元素
		num_flag = True
		while num_flag :
			num_2 = int(input("您想对第一组进行什么操作：\n 1、新增\n 2、删除\n 3、修改\n 4、显示全部\n 5、退出\n\t"))
			if num_2 == 1: 
				new_time = input("输入您想添加的时间信息:\n\t") 
				time.append(new_time)
				print(time)
			#删除1组中元素，因为从0开始，因此-1
			elif num_2 == 2:
				new_time = int(input("输入你想删除的元素序号：\n\t"))				
				del time[new_time - 1]
				print(time) 
			#修改1组中元素，输入修改元素再进行修改 
			elif num_2 == 3:	
				new_time = int(input("输入你想修改的元素序号：\n\t"))				
				new_account = input("请输入更新后的内容：\n\t")
				time[new_time - 1] =  "%s"%new_account
				print(time)
			elif num_2 == 4:
				print("*"*50)
				print(time)
				print("*"*50)
			elif num_2 == 5:
				num_flag = False
				break
			else:
				print("输入错误！！！")
	#操作地点列表信息
	elif num == 3:
		#新增2组元素
		num_flag = True
		while num_flag :
			num_2 = int(input("您想对第二组进行什么操作：\n 1、新增\n 2、删除\n 3、修改\n 4、显示全部\n 5、退出\n\t"))
			if num_2 == 1: 
				new_site = input("输入您想添加的地点信息:\n\t") 
				site.append(new_site)
				print(site)
			#删除1组中元素，因为从0开始，因此-1
			elif num_2 == 2:
				new_site = int(input("输入你想删除的元素序号：\n\t"))				
				del site[new_site - 1]
				print(site) 
			#修改1组中元素，输入修改元素再进行修改 
			elif num_2 == 3:	
				new_site = int(input("输入你想修改的元素序号：\n\t"))				
				new_account = input("请输入更新后的内容：\n\t")
				time[new_site - 1] =  "%s"%new_account
				print(site)
			elif num_2 == 4:
				print("*"*50)
				print(site)
				print("*"*50)
			elif num_2 == 5:
				num_flag = False
				break
			else:
				print("输入错误！！！")	
	#操作人物列表
	elif num == 4:
		#新增1组元素
		num_flag = True
		while num_flag :
			num_2 = int(input("您想对第三组进行什么操作：\n 1、新增\n 2、删除\n 3、修改\n 4、显示全部\n 5、退出\n\t"))
			if num_2 == 1: 
				new_man = input("输入您想添加的人物信息:\n\t") 
				man.append(new_man)
				print(man)
			#删除1组中元素，因为从0开始，因此-1
			elif num_2 == 2:
				new_man = int(input("输入你想删除的元素序号：\n\t"))				
				del man[new_man - 1]
				print(man) 
			#修改1组中元素，输入修改元素再进行修改 
			elif num_2 == 3:	
				new_man = int(input("输入你想修改的元素序号：\n\t"))				
				new_account = input("请输入更新后的内容：\n\t")
				man[new_man - 1] =  "%s"%new_account
				print(man)
			elif num_2 == 4:
				print("*"*50)
				print(man)
				print("*"*50)
			elif num_2 == 5:
				num_flag = False
				break
			else:
				print("输入错误！！！")
	#操作事件信息
	elif num == 5:
		#新增1组元素
		num_flag = True
		while num_flag :
			num_2 = int(input("您想对第四组进行什么操作：\n 1、新增\n 2、删除\n 3、修改\n 4、显示全部\n 5、退出\n\t"))
			if num_2 == 1: 
				new_event = input("输入您想添加的事件信息:\n\t") 
				event.append(new_event)
				print(event)
			#删除4组中元素，因为从0开始，因此-1
			elif num_2 == 2:
				new_event = int(input("输入你想删除的元素序号：\n\t"))				
				del event[new_event - 1]
				print(event) 
			#修改1组中元素，输入修改元素再进行修改 
			elif num_2 == 3:	
				new_event = int(input("输入你想修改的元素序号：\n\t"))				
				new_account = input("请输入更新后的内容：\n\t")
				event[new_event - 1] =  "%s"%new_account
				print(event)
			elif num_2 == 4:
				print("*"*50)
				print(event)
				print("*"*50)
			elif num_2 == 5:
				num_flag = False
				break
			else:
				print("输入错误！！！")
	elif num == 6:
		print("*"*40)
		print("*"*30)
		print("第一组：时间组的成员有:\n\t")
		print(time)		
		print("*"*30)
		print("第二组：地点组的成员有:\n\t")
		print(site)		
		print("*"*30)
		print("第三组：人物组的成员有:\n\t")
		print(man)		
		print("*"*30)
		print("第四组：事件组的成员有:\n\t")
		print(event)		
	elif num == 7:
		break
	else:
		print("您输入的信息有误，请重新输入！！")
