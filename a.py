#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import urllib
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import time
import tkinter as tk



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
def parser_html():
	arr_node = []
	page = ""
	arr_obj = {}
	count = 1
	str_num = ''
	while count <= 10:
		page = "https://www.ximalaya.com/search/zhubo/%E8%82%A1%E7%A5%A8/p" +str(count)
		htmls = download(page)
		bsObj = BeautifulSoup(htmls,"html5lib")
		nodes = bsObj.findAll("a",{'class':"anchor-link Qgwp"})
		count = count+1
		for node in nodes:

			str_num = str(node['href'].split('/')[-2])
			print(str_num)
			arr_node.append(str_num)
			# print(read_txt()[str_num])
			if (str_num in read_txt() )and read_txt()[str_num] == 1:
				arr_obj[str_num]  =  1
			else:
				arr_obj[str_num] = 0
	write_txt(arr_obj)
	return arr_node

if __name__ == '__main__':
	html = download("http://admin.xuanqiquan.com/cash.html")
	print(html)
