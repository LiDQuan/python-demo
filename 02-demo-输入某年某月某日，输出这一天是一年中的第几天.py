
#让用户输入年月日
year = input("请输入年:\n\t")
month = input("请输入月份:\n\t")
days = input("请输入天数:\n\t")

#润年1-12月份元组
run_year = [0,31,60,91,121,152,182,213,244,274,305,335,366]
#平年1-12月份元组
ping_year = [0,31,59,90,120,151,181,212,243,273,304,334,365]

#定义一个函数，判断是否是数字，如果不是数字，则返回提示重新输入
def if_num(i):
	if str(i).isdigit() == True:
		return True

#判断年月日，如果都是数字，则返回三个数的值
def if_all(i,j,k):
	if if_num(i) and if_num(j) and if_num(k) == True:
		return year,month,days
	else:
		print("输入的不是数字，请重新输入！！")

#定义一个函数，如果用户输入的是润年则使用润年元组进行计算
def run_days(year,month,days):
	#print("用户输入的是润年！")
	if int(month) == 1 or 2 or 3 or 5 or 7 or 8 or 10 or 12 :
		if 0 < int(days) and int(days)< 32:
			sum_num = run_year[int(month) - 1]
			return int(sum_num) + int(days)
		else:
			print("%s月份只有31天，请重新输入"%month)
	else:
		print("%s月份只有31天，请重新输入"%month)
			#print(sum_num)

#定义另一个函数，如果用户输入的是平年，则使用平年元组进行计算
def ping_days(year,month,days):
	#print("用户输入的是平年！")
	if int(month) == 2 or 4 or 6 or 9 or 11:
		if 0 < int(days) and int(days) < 31:
			sum_num = ping_year[int(month) - 1]
			return int(sum_num) + int(days)
		else:
			print("%s月份只有30天，请重新输入"%month)
	else:
		print("%s月份只有30天，请重新输入"%month)
			#print(SUm_num)

#定义一个函数，判断用户输入的是润年还是平年
def if_year_run_or_ping(year):
	if int(year)%4 == 0:
		return run_days(year,month,days)
	elif int(year)%4 != 0:
		return ping_days(year,month,days)
	else:
		print("输入错误！！")


if_all(year,month,days)
infor = if_year_run_or_ping(year)
try:
	print("您输入的日期是今年的第%d天"%infor)
except TypeError:
	print("您输入的数据不正确，请重新输入！")

