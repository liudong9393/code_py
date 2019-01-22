#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
# import urllib
# from bs4 import BeautifulSoup
# from splinter import Browser
# from selenium import webdriver
# import time
# import tkinter as tk
# import re

# -*- coding: utf-8 -*-
import pythoncom
import pyHook
import time
import win32api
import win32con
from pymouse import PyMouse
from PIL import ImageGrab
mouse = PyMouse()
start = list()
end = list()
def on_mouse_left_down(event):
	global start
	start = mouse.position()
	return True
def on_mouse_left_up(event):
	global end
	end = mouse.position()
	if start[0] < end[0] and start[1] < end[1]:
		start_x = start[0]
		start_y = start[1]
		end_x = end[0]
		end_y = end[1]
	elif start[0] > end[0] and start[1] < end[1]:
		start_x = end[0]
		start_y = start[1]
		end_x = start[0]
		end_y = end[1]
	elif start[0] < end[0] and start[1] > end[1]:
		start_x = start[0]
		start_y = end[1]
		end_x = end[0]
		end_y = start[1]
	elif start[0] > end[0] and start[1] > end[1]:
		start_x = end[0]
		start_y = end[1]
		end_x = start[0]
		end_y = start[1]
	else:
		return True
	grab_tuple = (start_x, start_y, end_x, end_y)
	print (grab_tuple)
	im = ImageGrab.grab(grab_tuple)
	im.save("test.jpg", 'jpeg')
	return True
hm = pyHook.HookManager()
hm.MouseLeftDown = on_mouse_left_down
hm.MouseLeftUp = on_mouse_left_up
hm.HookMouse()
pythoncom.PumpMessages()
# import time
# import win32gui, win32ui, win32con, win32api
# def window_capture(filename):
# 	hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
# 	# 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
# 	hwndDC=win32gui.GetWindowDC(hwnd)
# 	# 根据窗口的DC获取mfcDC
# 	mfcDC = win32ui.CreateDCFromHandle(hwndDC)
# 	# mfcDC创建可兼容的DC
# 	saveDC = mfcDC.CreateCompatibleDC()
# 	# 创建bigmap准备保存图片
# 	saveBitMap = win32ui.CreateBitmap()
# 	# 获取监控器信息
# 	MoniterDev = win32api.EnumDisplayMonitors(None, None)
# 	w = MoniterDev[0][2][2]
# 	h = MoniterDev[0][2][3]
# 	# print w,h　　　#图片大小
# 	# 为bitmap开辟空间
# 	saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
# 	# 高度saveDC，将截图保存到saveBitmap中
# 	saveDC.SelectObject(saveBitMap)
# 	# 截取从左上角（0，0）长宽为（w，h）的图片
# 	saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
# 	saveBitMap.SaveBitmapFile(saveDC, filename)
# beg = time.time()
# for i in range(10):
# 	window_capture("haha.jpg")
# end = time.time()
# print(end - beg)




# from PIL import ImageGrab
# pic = ImageGrab.grab()
# pic.save("picture.jpg")

# from selenium import webdriver
# import time
# def capture(url, filename="capture.png"):
# 	browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# 	browser.set_window_size(1200, 900)
# 	browser.get(url) # Load page
# 	browser.execute_script("""
# 	(function () {
# 		var y = 0;
# 		var step = 100;
# 		window.scroll(0, 0);
# 		function f() {
# 		if (y < document.body.scrollHeight) {
# 		y += step;
# 		window.scroll(0, y);
# 		setTimeout(f, 50);
# 		} else {
# 		window.scroll(0, 0);
# 		document.title += "scroll-done";
# 		}
# 		}
# 		setTimeout(f, 1000);
# 		})();
# 	""")
# 	for i in range(30):
# 		if "scroll-done" in browser.title:
# 			break
# 		time.sleep(1)
# 	beg = time.time()
# 	for i in range(10):
# 		browser.save_screenshot(filename)
# 	end = time.time()
# 	print(end - beg)
# 	browser.close()
# capture("http://www.baidu.com")





# import win32gui
# from ctypes import *
# import ctypes
# from PIL import ImageGrab
# import win32api,win32con
# import pyHook
# import pythoncom

# #定义结构体，存储当前窗口坐标
# class RECT(ctypes.Structure):
#     _fields_ = [('left', ctypes.c_int),
#                 ('top', ctypes.c_int),
#                 ('right', ctypes.c_int),
#                 ('bottom', ctypes.c_int)]
# rect = RECT()
# HWND = win32gui.GetForegroundWindow()#获取当前窗口句柄
# ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))#获取当前窗口坐标
# coordinate = (rect.left+2, rect.top+2, rect.right-2, rect.bottom-2)#转换为预截图窗口坐标
# pic = ImageGrab.grab(coordinate)#截图
# pic.save("321.jpg")#保存
# mygui = tk.Tk()
# mygui.title('配置')
# mygui.geometry('450x500') 
# # 网址
# website_name = tk.Label(mygui, text="网址:",   width=6, height=1)
# website = tk.Text(mygui,width = 35,height=1)
# website.insert('end',infoObj["web"])
# def websites(event):
# 	infoObj["web"] = website.get('0.0','end')
# 	# print(infoObj["web"])
# website.bind("<FocusOut>",websites)
# website_name.place(x= 20,y = 10)
# website.place(x= 100,y = 10)

# # id
# id_name = tk.Label(mygui, text="用户:",   width=6, height=1)
# id = tk.Text(mygui,width = 35,height=1)
# id.insert('end',infoObj["id"])
# def ids(event):
# 	infoObj["id"] = id.get('0.0','end')
# 	# print(infoObj["web"])
# id.bind("<FocusOut>",ids)
# id_name.place(x= 20,y = 40)
# id.place(x= 100,y = 40)

# # pwd
# pwd_name = tk.Label(mygui, text="密码:",   width=6, height=1)
# pwd = tk.Text(mygui,width = 35,height=1)
# pwd.insert('end',infoObj["pwd"])
# def pwds(event):
# 	infoObj["pwd"] = pwd.get('0.0','end')
# 	# print(infoObj["web"])
# pwd.bind("<FocusOut>",pwds)
# pwd_name.place(x= 20,y = 70)
# pwd.place(x= 100,y = 70)


# # 搜索页数
# page_name = tk.Label(mygui, text="页数:",width=6, height=1)
# page1 =  tk.Label(mygui, text="开始",   width=3, height=1)
# p1 = tk.Text(mygui,width = 3,height=1)
# line = tk.Label(mygui, text="-",   width=3, height=1)
# page2 = tk.Label(mygui, text="结束",   width=3, height=1)
# p2 = tk.Text(mygui,width = 3,height=1)
# p1.insert('end',infoObj["p1"])
# p2.insert('end',infoObj["p2"])
# def p1s(event):
# 	infoObj["p1"] = p1.get('0.0','end')
# 	# print(infoObj["web"])
# def p2s(event):
# 	infoObj["p2"] = p2.get('0.0','end')
# 	# print(infoObj["web"])
# p1.bind("<FocusOut>",p1s)
# p2.bind("<FocusOut>",p2s)
# page_name.place(x= 20,y = 100)
# page1.place(x= 70,y = 120)
# p1.place(x= 105,y = 122)
# line.place(x= 130,y = 120)
# page2.place(x= 160,y = 120)
# p2.place(x= 195,y = 122)


# # 内容
# texts_name = tk.Label(mygui, text="密码:",   width=6, height=1)
# texts = tk.Text(mygui,width = 40,height=8)
# texts.insert('end',infoObj["texts"])
# def textss(event):
# 	infoObj["texts"] = texts.get('0.0','end')
# 	# print(infoObj["web"])
# texts.bind("<FocusOut>",textss)
# texts_name.place(x= 20,y = 150)
# texts.place(x= 80,y = 170)


# # 状态
# result_name = tk.Label(mygui, text="状态:", width=6, height=1)
# result = tk.Label(mygui, text="等待配置", width=20, height=1)


# # result.bind("<FocusOut>",results)
# result_name.place(x= 20,y = 290)
# result.place(x= 70,y = 290)


# login = tk.Button(text="确认",width=8,height=1)
# def logins(event):
# 	p_html = parser_html()
# 	every_page(p_html)
	
# login.bind("<Button-1>",logins)
# login.place(x= 80,y = 380)
# cancel = tk.Button(text="退出",width=8,height=1, command=mygui.quit)
# # def cancels(event):
# # 	infoObj["texts"] = texts.get('0.0','end')
# # 	# print(infoObj["web"])
# # texts.bind("<FocusOut>",cancels)
# cancel.place(x= 300,y = 380)
# # 进入消息循环
# mygui.mainloop()




