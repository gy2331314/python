from bs4 import BeautifulSoup
import requests
from time import sleep

url = 'http://38.103.161.139/forum/forumdisplay.php?fid=143&filter=type&typeid=1255'
urls = ['http://38.103.161.139/forum/forumdisplay.php?fid=143&filter=type&typeid=1255@page={}'.format(str(i)) for i in range(2,52)]

def get_attractions(url,data=None):
    web_data = requests.get(url)
    sleep(5)
    soup = BeautifulSoup(web_data.text,'lxml')
    titles = soup.select('table > tbody > tr > th > span > a')
    times = soup.select('table > tbody > tr > td > em')
        #print(times)
    for title,time in zip(titles,times):
        data = {
            'title':title.get_text(),
            #'time':time.get_text(),
            'link':title.get('href'),
        }
        print(data)
#get_attractions(url)
#print(urls)
for loop in urls:
    get_attractions(loop)
