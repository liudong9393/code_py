#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import urllib
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import time
import tkinter as tk
texts = """我们是58策略平台，可以帮助您进行股民流量变现，主要做2到8倍的A股杠杆点买服务，所有的交易L2行情都可查，而且有集团背景，盘子很稳，可以帮助您进行股民流量变现，如有合作意向，可以联系18545177496，微信号也一致，辛苦。"""
infoObj = {"web":"https://www.ximalaya.com/zhubo/","id":'18904503071',"pwd":"a81336688133661","p1":1,"p2":2,"texts":texts,"result":"等待"}

def download(url,user_agent="wswp",num_retries=2,charset='utf-8',proxy=None):
	print("Downloading:",url)
	request = urllib.request.Request(url)
	request.add_header("User-agent",user_agent)
	try:
		if proxy:
			proxy_support = urllib.request.ProxyHandler({'http':proxy})
			opener = urllib.request.build_opener(proxy_support)
			urllib.request.install_opener(opener)
		resp = urllib.request.urlopen(request)
		cs = resp.headers.get_content_charset()
		if not cs:
			cs = charset
		html = resp.read().decode(cs)
	except (urllib.error.URLError,urllib.error.HTTPError) as e:
		print("Download error:",e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download(url,num_retries-1)
	return html
def parser_html(start,ends):
	arr_node = []
	page = ""
	arr_obj = {}
	count = int(start)
	str_num = ''
	reads = read_txt()
	print(reads)
	# print(str(start))
	while count <= int(ends):
		page = "https://www.ximalaya.com/search/zhubo/%E8%82%A1%E7%A5%A8/p" +str(count)
		htmls = download(page)
		bsObj = BeautifulSoup(htmls,"html5lib")
		nodes = bsObj.findAll("a",{'class':"anchor-link Qgwp"})
		count = count+1
		
		for node in nodes:

			str_num = str(node['href'].split('/')[-2])
			# print(str_num)
			arr_node.append(str_num)
			# print(read_txt()[str_num])
			if (str_num in read_txt() )and read_txt()[str_num] == 1:
				arr_obj[str_num]  =  1
			else:
				arr_obj[str_num] = 0
		reads.update(arr_obj)
	write_txt(reads)
	return arr_node

def every_page(p_htmls):
	texts = """我们是58策略平台，可以帮助您进行股民流量变现，主要做2到8倍的A股杠杆点买服务，所有的交易L2行情都可查，而且有集团背景，盘子很稳，可以帮助您进行股民流量变现，如有合作意向，可以联系18545177496，微信号也一致，辛苦。"""
	status =  read_txt()
	for p_html in p_htmls:
		if status[str(p_html)] == 1:
			continue
		elif status[str(p_html)] == 0:

			url = 'https://www.ximalaya.com/zhubo/'+ str(p_html) 
			driver = webdriver.Chrome()
			driver.get(url)
			driver.find_elements_by_class_name('v-m')[0].click()
			driver.find_elements_by_id('accountName')[0].send_keys("18904503071")
			driver.find_elements_by_id('accountPWD')[0].send_keys("a81336688133661")

			driver.find_elements_by_class_name('login-btn')[0].click()
			time.sleep(1)
			driver.find_elements_by_class_name('anchor-home-header-box-chat')[0].click()


			driver.find_elements_by_id('chatRoomTextarea')[0].send_keys(texts)
			# driver.find_elements_by_class_name('chat-modal-submit')[0].click()
			time.sleep(5)
			driver.quit()
			status[str(p_html)] = 1
			write_txt(status)
			# driver.close()


def read_txt():
	with open('data/arr_num.txt','r') as file_r:
		lists=file_r.read()
	return eval(lists)

def write_txt(wObj):
	with open('data/arr_num.txt','w') as file_w:
		file_w.write(str(wObj))


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
def logins(event):
	p_html = parser_html(infoObj['p1'] ,infoObj['p2'])
	every_page(p_html)
	
login.bind("<Button-1>",logins)
login.place(x= 80,y = 380)
cancel = tk.Button(text="退出",width=8,height=1, command=mygui.quit)
# def cancels(event):
	# driver.quit()
	# driver.close()
# 	# print(infoObj["web"])
# texts.bind("<FocusOut>",cancels)
cancel.place(x= 300,y = 380)
# 进入消息循环
mygui.mainloop()

# if __name__ == '__main__':
	
	
# 	p_html = parser_html()
# 	every_page(p_html)
	# print(htmls)