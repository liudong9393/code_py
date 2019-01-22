#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import urllib
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import time
import tkinter as tk
import re
def download(url,user_agent="wswp",num_retries=2,charset='utf-8',proxy=None):
	# print("Downloading:",url)
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

def parser_html(html):
	
	bsObj = BeautifulSoup(html,"html5lib")
	# node = bsObj.find("div",{'class':"para"}).text
	# print(node)
	try:
		nodes = bsObj.find("dd",{'class':"lemmaWgt-lemmaTitle-title"}).find_all('h2')[0].get_text()
		return nodes
	except Exception as e:
		nodes = bsObj.find("div",{'class':"para"}).text #.find_all('a')[0]

	# else:
	# 	nodes = bsObj.find_all("div",{'class':"para"})
		return nodes
			

def write_txt(wObj):
	with open('data/arr_num.txt','w') as file_w:
		file_w.write(str(wObj))
def read_txt():
	with open('data/arr_num.txt','r') as file_r:
		lists=file_r.read()
	return eval(lists)	

if __name__ == '__main__':
	read_txt()
	address = urllib.parse.quote("奉贤") 
	html = download("http://baike.baidu.com/item/"+ address) 
	parser = str(parser_html(html))
	# (?# pattern=r'([\u4e00-\u9fa5](?:是|于|，){2,5}?(?:省|自治区|市))'#中文正则表达式)
	r = re.search( r"(是|于|，|。)([\u4e00-\u9fa5]{2,10}?市)", parser, re.M|re.I)
	r1 = re.search( r"(是|于)([\u4e00-\u9fa5]{2,5}?市)", str(r), re.M|re.I)	
	print(r1.group(2))
	write_txt(r1.group(2))


