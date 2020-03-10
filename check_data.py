n=10
for x in range(n):
    print(x)

x=99
while x>0 :
    x-=1
    print(x)

import requests
import json
import numpy as np
data=np.array([[0.9523,-0.246,00.0855],[0.5639,0.2397,0.9104]])
print(data.shape)


from bs4 import BeautifulSoup
import time
url = 'https://tip.railway.gov.tw/tra-tip-web/tip'
staDic = {}
today = time.strftime('%Y/%m/%d')
sTime = '06:00'
eTime = '12:00'

def getTrip():
    