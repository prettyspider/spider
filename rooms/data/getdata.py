import requests
from bs4 import BeautifulSoup
def get_data(url):
       headers = {
           'user-agent': 'Mozilla/5.0',
       }
       web_page = requests.get(url, headers=headers)
       web_page.encoding = 'utf-8'
       web_text = web_page.text
       # with open('web.html','w',encoding='utf-8')as f:
       #        f.write(web_text)
       soup = BeautifulSoup(web_text, 'html.parser')
       return soup
