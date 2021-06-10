'''
一、
num = 2 #标识符由字母数字下划线组成，汉字属于字母
print(num)
关键字不能命名
'''
'''
二、
import keyword
print(keyword.kwlist)

import os
mystr = input("请输入指令")
os.system(mystr)

这课设是真的难写 = 000
print(这课设是真的难写)
print(type(这课设是真的难写))#type显示变量类型
print(id(这课设是真的难写))#id显示变量地址

#python中变量可以改变数据类型
num1=10
print(num1)
print(type(num1))
print(id(num1))
num1=20
print(num1)
print(type(num1))
print(id(num1))
num1="calc"
print(num1)
print(type(num1))
print(id(num1))
'''

'''
三、
#变量赋值
num2 = 3
num3 = 3
print(num2,num3)#打印多个数据使用逗号分隔
print(id(num2),id(num3))
num2 = 4
print(num2,num3)
print(id(num2),id(num3))#python中是通过地址赋值
'''

'''
四、
num4=10
print("有点傻的点数",num4)
print(type(num4))
'''

'''
#五、赋值
num5=1
del num5 #del是删除变量
#num6=num7=10连续赋值
num5,num6=1,6
print(num5,num6)#赋值语句，但是必须对称（交互对称赋值）
'''

'''
#六、类型转换eval字符串转换为实数 使用type查看类型
R = input("请输入圆的半径")
print(R) #字符串不能参与运算
print(type(R))
R = eval(R) #字符串转换为实数
print(type(R))
print(R*R*3.1415926)
'''
'''
#七、换行
print(1+2+3+4+
      4+
      5)#运算符可以自动拆分换行,还有 / 可以换行
#多行归并为一行需要加上分号
num1=1;num2=2;num3=3;print(num1,num2,num3)

'''

'''#八
#data=100**10000000
#print(data)#计算机会报错，因为数字太大
num=3
print(type(num))
num=str(num) #数字转换为字符串
print(type(num))
num1=10.56
print(round(num1))#round是四舍五入操作
num3=10.59
print(round(num3))
'''

'''
九
#数学模块
import math
print(abs(-5)) #求绝对值
print(max(1,2,3,4))
'''
'''
十
ch1 = 'A'
print(ord(ch1))#ord用来求字符串编号,字符创长度只能为宜
print(chr(97))#char用来求编号为97的字符
'''
'''
十一
#print的高级用法，
print("a",end="")  #以空格键结束
print("b",end="")
print("b",end="")

print(1,2,3,sep="----") #sep 是连接 字符串的拼接
'''

'''
十二
import os
mystr1 = "node"
mystr2 = "pad"
os.system(mystr1+mystr2) #字符串加法表示连接
'''
'''
十三.关于类和对象自己在看看
print(type("abc")) #abc是字符串类型的对象
print("abc".upper()) #upper是将小写转大写lower转变为小写
print("abc".find("b"))#查找
#python所有的数据都是对象
'''

'''
#十四 数据格式化 format
print(format(10.1,"<10.8f"),10.123456) #<为左对齐而不加小于号为右对齐
print(format(10.123,"10.8f"),10.123456)#因为是浮点数就是用f
print(format(10.1234,"10.8f"),10.123456)
print(10.12345,10.123456)
print(10.123456,10.123456)
print(10.1234567,10.123456)#在此不一一示例
'''

'''
#十五 画图补充

import turtle as t
t.screensize(1080,1080)#设置屏幕大小
t.pensize(5)
t.write("hello",font = ("宋体",20,"normal"))#设定字体样式，大小
t.showturtle()
t.begin_fill() #开始填充
t.circle(100,steps = 5)#设置半径和边数
t.color("yellow")#填充颜色
t.end_fill()#结束填充
t.hideturtle()#隐藏箭头
t.rest()#重置
t.done()


'''
'''
import time
timedata = time.time()
print(int(timedata))
timedata = timedata%26
timedata = int(timedata)
print("%",timedata)
print(ord('w'))
print(chr(99))
'''

'''
#十六/有关if
if -1:#字符串非空为truel
    printf("hellow")
if "":#字符串为空为fource
    printf("good")

'''

'''
#十七 随机数
import random #导入随机数

num1 = random.randint(0,100)#randint是 rand + int

'''

'''
#十八 while
i=1
while i<5:#切勿忘记分号
    print("....")
    i+=1
'''
'''
#十九time.sleep
import time
num = 2.0
while num!=0:
    num-=0.1
    print(num)
    time.sleep(0.5)#程序暂停0.5秒
'''
'''
#二十循环
for i in range(1,100,10):  #不要忘记分号；步长为最后一个数，这里为10
    print(i)#不包含max即这里的100

for i in range(10):#i循环一次j循环5次
    for j in range(5):
        print(j,end=" ")
    print("_______",i)
'''

'''
import turtle as t
t.showturtle()
step = 20
for i in range(19):

    t.penup()
    t.goto(0,step*i)
    t.pendown()
    t.forward(step*18)
t.right(270)
for j in range(11):
    t.penup()
    t.goto(step*j,0)
    t.pendown()
    t.forward(step*10)
t.dot(30,"red")
t.done()

'''

'''
#分隔
line = 'a,b,c'
ooo = line.split(',')  #split()以某一字符作为风格
print(ooo)
'''
'''
samp_string = 'what fack'
print(samp_string[::2])
print(samp_string[0::3])
for i in range(0,len(samp_string)-1,2):
    print(samp_string[i]+samp_string[i+1])
    print("you"+"is"+samp_string[0:6])
rand_string =" life is a beautiful struggle"
rand_string = rand_string.lstrip()#删除左空格

'''
'''
#  join的使用
a_list = ["Bunch","of","random","words"]
print("".join(a_list))
print(",".join(a_list))#  join的使用
'''
# 关键字太try和expect捕捉错误
# try:
#     f = open('testfile.txt')
#     print(f.read())
# except Exception:
#     print('对不起文件不存在')

# bad_var = 'i am not a bad_var'
# try:
#     var = bad_var
# except NameError as e: #错误原因NameError使用系统给出就是as e
#     print(e)
# else:
#     print(var)
# finally:
#     print("...")









