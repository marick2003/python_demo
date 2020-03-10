import requests
from bs4 import BeautifulSoup
import time

resp = requests.get('https://code-gym.github.io/spider_demo/')
soup = BeautifulSoup(resp.text, 'html5lib')
print(soup.find('h1').text)
nav= soup.find(id=='nav')
header=nav.parent.find(id=='header')
ul = soup.find('ul')
print(header)
for li in ul.children:
    print(li.find('a'))

def pttMSG(self, parameter_list):
    pass