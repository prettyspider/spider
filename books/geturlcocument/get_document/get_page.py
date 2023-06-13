import requests
from bs4 import BeautifulSoup
"""
获取网页数据，解析数据，将相应的数据传出
"""
def get_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                     'Mobile Safari/537.36 Edg/114.0.1823.43'
    }
    resp=requests.get(url,headers=headers)
    soup=BeautifulSoup(resp.text,'html.parser')
    return soup