#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
texts = """我们是58策略平台，可以帮助您进行股民流量变现，主要做2到8倍的A股杠杆点买服务，所有的交易L2行情都可查，而且有集团背景，盘子很稳，可以帮助您进行股民流量变现，如有合作意向，可以联系18545177496，微信号也一致，辛苦。"""
infoObj = {"web":"https://www.ximalaya.com/zhubo/","id":'18904503071',"pwd":"a81336688133661","p1":1,"p2":2,"texts":texts,"result":"等待"}
mygui = tk.Tk()
mygui.title('配置')
mygui.geometry('450x500') 
# 网址
website_name = tk.Label(mygui, text="网址:",   width=6, height=1)
website = tk.Text(mygui,width = 35,height=1)
website.insert('end',infoObj["web"])
def websites(event):
	infoObj["web"] = website.get('0.0','end')
	# print(infoObj["web"])
website.bind("<FocusOut>",websites)
website_name.place(x= 20,y = 10)
website.place(x= 100,y = 10)

# id
id_name = tk.Label(mygui, text="用户:",   width=6, height=1)
id = tk.Text(mygui,width = 35,height=1)
id.insert('end',infoObj["id"])
def ids(event):
	infoObj["id"] = id.get('0.0','end')
	# print(infoObj["web"])
id.bind("<FocusOut>",ids)
id_name.place(x= 20,y = 40)
id.place(x= 100,y = 40)

# pwd
pwd_name = tk.Label(mygui, text="密码:",   width=6, height=1)
pwd = tk.Text(mygui,width = 35,height=1)
pwd.insert('end',infoObj["pwd"])
def pwds(event):
	infoObj["pwd"] = pwd.get('0.0','end')
	# print(infoObj["web"])
pwd.bind("<FocusOut>",pwds)
pwd_name.place(x= 20,y = 70)
pwd.place(x= 100,y = 70)


# 搜索页数
page_name = tk.Label(mygui, text="页数:",width=6, height=1)
page1 =  tk.Label(mygui, text="开始",   width=3, height=1)
p1 = tk.Text(mygui,width = 3,height=1)
line = tk.Label(mygui, text="-",   width=3, height=1)
page2 = tk.Label(mygui, text="结束",   width=3, height=1)
p2 = tk.Text(mygui,width = 3,height=1)
p1.insert('end',infoObj["p1"])
p2.insert('end',infoObj["p2"])
def p1s(event):
	infoObj["p1"] = p1.get('0.0','end')
	# print(infoObj["web"])
def p2s(event):
	infoObj["p2"] = p2.get('0.0','end')
	# print(infoObj["web"])
p1.bind("<FocusOut>",p1s)
p2.bind("<FocusOut>",p2s)
page_name.place(x= 20,y = 100)
page1.place(x= 70,y = 120)
p1.place(x= 105,y = 122)
line.place(x= 130,y = 120)
page2.place(x= 160,y = 120)
p2.place(x= 195,y = 122)


# 内容
texts_name = tk.Label(mygui, text="密码:",   width=6, height=1)
texts = tk.Text(mygui,width = 40,height=8)
texts.insert('end',infoObj["texts"])
def textss(event):
	infoObj["texts"] = texts.get('0.0','end')
	# print(infoObj["web"])
texts.bind("<FocusOut>",textss)
texts_name.place(x= 20,y = 150)
texts.place(x= 80,y = 170)


# 状态
result_name = tk.Label(mygui, text="状态:", width=6, height=1)
result = tk.Label(mygui, text="等待配置", width=20, height=1)


# result.bind("<FocusOut>",results)
result_name.place(x= 20,y = 290)
result.place(x= 70,y = 290)


login = tk.Button(text="确认",width=8,height=1)
login.place(x= 80,y = 380)
cancel = tk.Button(text="退出",width=8,height=1, command=mygui.quit)
def logins(event):
	
texts.bind("<Button-1>",logins)

# def cancels(event):
# 	infoObj["texts"] = texts.get('0.0','end')
# 	# print(infoObj["web"])
# texts.bind("<FocusOut>",cancels)
cancel.place(x= 300,y = 380)
# 进入消息循环
mygui.mainloop()


