#-*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
import requests
def translation():
    """
    翻译
    :return:
    """
    #获取输入的内容
    content = entry.get()
    #去空格 split是切割
    content = content.strip()
    if content == '':
        messagebox.showinfo('提示',message = '请输入要翻译的内容')
    else:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {
            'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',

            # 'salt': '15827948097626',
            # 'sign': 'b9989465680493e466593f9539e05796',
            # 'ts': '1582794809762',
            # 'bv': '767d6b27f6caf88200654eb2a7b6e2eb',

            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        req = requests.post(url,data = data).json()
        tran = req['translateResult'][0][0]['tgt']
        # print(tran)
        res.set(tran)
        return tran


# 创建窗口
window = Tk()
#窗口大小
window.geometry('820x600')
#窗口标题
window.title('我的翻译软件')
#控件
label = Label(window,text = '输入要翻译的文字：',font=('幼圆',20),fg = 'LightSeaGreen')
#位置 网格式的布局  grid  pack 包  place位置
label.place(x=0, y=0)

label1 = Label(window,text = '翻译后的结果为：',font=('幼圆',20),fg = 'LightSeaGreen')
#位置 网格式的布局  grid  pack 包  place位置
label1.place(x=0, y=250)
#输入框
entry = Entry(window,font = ('幼圆',15))
#修改位置 row为行 column为列
entry.place(x=20,y = 45,heigh = 200,width=770)
# entry.place(width=600, height=350)


#输出框
res = StringVar()
entry1 = Entry(window,font = ('幼圆',15),textvariable = res,width=600)
#修改位置 row为行 column为列
entry1.place(x=20,y = 300,heigh = 200,width=770)
# entry1.place(width=150, height=50)


#按钮
button = Button(window,text = '翻译',font=('幼圆',12),width = 25,height = 2,fg = 'DimGray',command = translation)
button.place(x=0, y=600,anchor='sw')
button1 = Button(window,text = '退出',font=('幼圆',12),width = 25,height = 2,fg = 'DimGray',command = window.quit)
button1.place(x=820, y=600,anchor='se')
#显示窗口
window.mainloop()
