#插入import头文件
import os
import os.path



#定一个路径
user_path = "/home/admin/Desktop/dome"


#开始循环
#os.walk()函数列表中，
#[0]下标是：目标文件夹具体路径，是一个字符串
#[1]下标是：dome文件夹下所有文件夹的名字，是一个列表
#[2]下标是：包含了该目录下非文件夹的所有文件，但是并没有具体目录信息，需要得到具体目录信息还需调用其他函数
'''
print("*"*50)
for i in os.walk(user_path):
	for i_s in i:	
		print("这里显示的是[0],也就是目标文件具体路径：")
		print(i_s)
		print("\n\t")
	for name in i:
		print("这里显示的是[1],显示该文件夹下所有文件夹的名字：")
		print(name)
		print("\n\t")
	for x in i:
		print("这里显示的是[1],显示该文件夹下所有文件夹的名字：")
		print(x)
		print("\n\t"
print("*"*50)
'''


for i,j,k in os.walk(user_path):	
	print("这里显示的是[0],也就是目标文件具体路径：")
	print(i)
	print(j)
	print(k)
	print("*"*50)
	for ii in i:
		print(ii)
		print("*"*50)
