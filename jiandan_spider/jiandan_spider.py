# 爬取图片并保存

import requests
import urllib.request
from bs4 import BeautifulSoup
import time

url = 'http://jandan.net/ooxx/page-'  # from 1500
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }

def get_page(url):
    source_code = requests.get(url,headers = headers)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text,'lxml')

    download_links = []
    folder_path = 'E:\Workspace\python\jiandan_spider\download\\'

    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('div > div > div.text > p > img')

    for img in imgs:
        img_link = img.get('src')
        download_links.append(img_link)

    for item in download_links:
        urllib.request.urlretrieve(item,folder_path + item[-10:] )
        print('Done')

def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)

get_more_pages(1600,1620)