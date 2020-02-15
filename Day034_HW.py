#!/usr/bin/env python
# coding: utf-8

# # 反爬：代理伺服器/IP
# 
# * 了解「IP 黑/白名單」的反爬蟲機制
# * 「IP 黑/白名單」反爬蟲的因應策略

# ## 作業目標
# 
# * 目前程式中的 proxy_ips 是手動輸入的，請根據 https://free-proxy-list.net/ 寫一個可自動化抓取可用 Proxy 的 proxy_ips。
# 
# 
# 

# In[5]:


import requests
from bs4 import BeautifulSoup
import random

proxy_ips = []


# In[7]:


r = requests.get('https://free-proxy-list.net/')
soup = BeautifulSoup(r.text, 'html5lib')
for ip_list in soup.find('tbody').find_all('tr'):
    ip = ip_list.find_all('td')[0].text
    port = ip_list.find_all('td')[1].text
    proxy_ips.append(ip + ':' + port)
print(proxy_ips)


# In[ ]:


for i in range(10):
    ip = random.choice(proxy_ips)
    print('Use', ip)
    try:
        resp = requests.get('http://ip.filefab.com/index.php',
                        proxies={'http': ip, 'https': ip}, timeout=10)
        soup = BeautifulSoup(resp.text, 'html5lib')
        print(soup.find('h1', id='ipd').text.strip())
    except:
        print('Fail')


# In[ ]:




