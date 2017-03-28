#!/usr/bin/env python
# -*-coding:UTF-8 -*-((
import requests
from lxml import etree
import time

class IpPool(object):
	def __init__(self):
		self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

	def collect_ip(self,page):#ip收集，page为页数
		for i in range(1,page):
			url = "http://www.xicidaili.com/nn/"+str(i)
			print(url)
			r = requests.get(url,headers=self.header).content
			
			s = etree.HTML(r)
			myips = s.xpath("//tr[@class='odd']/td[2]/text()")#取ip
			myports = s.xpath("//tr[@class='odd']/td[3]/text()")#取端口号
			with open("output.txt",'a') as fout:
				for i in range(len(myips)):
					fout.write("http://"+myips[i]+":"+myports[i]+"\n")

	def test_ip(self):#测试可用ip
		with open("output.txt","r") as f:
			with open("ok.txt","w") as ft:
				lines = f.readlines()

				for line in lines:				
					line = line.strip('\n')					
					proxies = {"http":line}
					try:
						req = requests.get("http://www.baidu.com",headers=self.header,proxies=proxies,timeout=5).content
						time.sleep(2)
						if r:							
								ft.write(line+"\n")
								print(line)
					except:
						time.sleep(2)
						continue

if __name__=="__main__":
	ip_pool = IpPool() #实例化ip池类
	t0 = time.time()
	ip_pool.collect_ip(2)
	ip_pool.test_ip()
	t1 = time.time()
	t10 = t1-t0
	t10 = str(t10)
	with open("timeo.txt","w") as oo:
		oo.write(t10)