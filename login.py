#!/usr/bin/env python
# -*-coding:UTF-8 -*-
import requests
s= requests.Session()
data = {'username':'','password':''}
login_url = ''
index_url = ''
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
p = s.post(login_url,data=data,headers=header)
r = s.get(index_url,headers=header).content
with open('test.html','wb') as f:
	f.write(r)
