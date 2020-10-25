from bs4 import BeautifulSoup
from utils import getDisplayMetrics

import requests

def crawl_proxies_Walpaper():
    #Парсит сайт walpeperscraft и достает ссылки на картинки в виде словаря, ключи которого - это имена картинок
    proxiesImage = {}
    link = "https://wallpaperscraft.ru/all/{}x{}/".format(getDisplayMetrics(0), getDisplayMetrics(1))

    r = requests.get(link)
    s = BeautifulSoup(r.text, 'html.parser')

    for i in s.find_all('img'):
        try:
            hrefImg = i.get('src')

            if (hrefImg[0:5] == "https"):
                #Имя картинки
                nameImg = hrefImg[40:-11]
                #Ссылка на картинку
                hrefImg = hrefImg[0:-11] + "{}x{}.jpg".format(getDisplayMetrics(0), getDisplayMetrics(1))

                proxiesImage[str(nameImg)] = hrefImg
            else: continue

        except:
            pass

    return proxiesImage
