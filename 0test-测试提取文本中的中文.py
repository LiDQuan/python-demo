# -*- coding: utf-8 -*-  
import re  
import sys  
reload(sys)  
sys.setdefaultencoding("utf8")  
  
def translate(str_1):  
    line = str_1.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等  
    p2 = re.compile(ur'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5  
    zh = " ".join(p2.split(line)).strip()  
    zh = ",".join(zh.split())  
    outStr = zh  # 经过相关处理后得到中文的文本  
    return outStr

def add_txt(account):
            #新建一个文件
         f = open('testnmae.txt','w')
            #写入一个hello world
         f.write(account)
            #最后保存并且关闭该文档
         f.close()


path = '/home/admin/Desktop/dome/test000.txt'
print(translate(path))
