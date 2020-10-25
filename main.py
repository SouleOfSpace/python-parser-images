#Прокси сканнер
from threading import Thread
import requests, os, time

from utils import getDir, checkInternetActive, checkDateCreateImg
from proxyScanner import crawl_proxies_Walpaper

class DownloadImg(Thread):
    def __init__(self, url, name):
        Thread.__init__(self)
        self.__url = url            #URL скачиваемого файла
        self.__name = name          #Имя которое присвоится скаченному файлу
        self.__path = getDir()      #Директория хранения изображений

    def run(self):
        #Ссылка на скачивание
        p = requests.get(self.__url)
        #Открытие директории
        out = open(self.__path + '\\{}.jpg'.format(self.__name), 'wb')
        #Запись в директорию
        out.write(p.content)
        #Закрытие директории
        out.close()

class DeleteOldImage(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__path = getDir()

    def __sortToDate(self):
        # Сортировка файлов по дате создания
        file_list = os.listdir(self.__path)
        full_list = [os.path.join(self.__path, i) for i in file_list]
        time_sorted_list = sorted(full_list, key=os.path.getmtime)

        return time_sorted_list

    def run(self):
        #удаление старых картинок (оставлет только последние 10 изображений)
        time_sorted_list = self.__sortToDate()

        length = len(time_sorted_list)

        for i in time_sorted_list:
            if (length > 10):
                os.remove(i)
                length -= 1

def downloadImg(contentImg):
    #Скачивает картинки по переданным ссылкам
    time.sleep(10)
    for key in contentImg:
        thread = DownloadImg(contentImg[key], key)
        thread.start()

def deleteOldImage():
    #Удаляет старые изображеня
    thread = DeleteOldImage()
    thread.start()

if __name__ == '__main__':
    if (checkDateCreateImg() and checkInternetActive()):
        content = crawl_proxies_Walpaper()
        downloadImg(content)
        time.sleep(10)
        deleteOldImage()
