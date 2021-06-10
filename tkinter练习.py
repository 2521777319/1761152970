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
window.geometry('372x100')
#窗口标题
window.title('中英互译')
#控件
label = Label(window,text = '输入要翻译的文字：',font=('幼圆',12),fg = 'red')
#位置 网格式的布局  grid  pack 包  place位置
label.grid()

label1 = Label(window,text = '翻译后的结果为：',font=('幼圆',12),fg = 'red')
#位置 网格式的布局  grid  pack 包  place位置
label1.grid(row = 1,column = 0)
#输入框
entry = Entry(window,font = ('幼圆',15))
#修改位置 row为行 column为列
entry.grid(row = 0,column = 2)

#输出框
res = StringVar()
entry1 = Entry(window,font = ('幼圆',15),textvariable = res)
#修改位置 row为行 column为列
entry1.grid(row = 1,column = 2)

#按钮
button = Button(window,text = '翻译',width = 10,command = translation)
button.grid(row = 2,column = 0,sticky = W)
button1 = Button(window,text = '退出',width = 10,command = window.quit)
button1.grid(row = 2,column = 2,sticky = E)
#显示窗口
window.mainloop()
