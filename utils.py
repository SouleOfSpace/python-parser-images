import os, ctypes, urllib, datetime

def getDisplayMetrics(index):
    #Возвращаем разрешение экрана
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()

    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)

    return [width, height][index]


def makeDir():
    # создаем директорию для хранения изображений
    try:
        os.mkdir('images')
    except OSError:
        return


def getDir():
    # возвращаем директорию для хранения изображений
    makeDir()
    return os.getcwd() + '\\images'

def checkInternetActive():
    #Проверяет подключен ли интернет
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except IOError:
        return False

def checkDateCreateImg():
    # Проверяет обновлялись ли фотографии текущим днем
    try:
        path = getDir()

        file_list = os.listdir(path)
        for i in file_list:
            imgUrl = os.path.join(path, i)

        dateCreate = datetime.datetime.fromtimestamp(os.path.getmtime(imgUrl))
        deadline = datetime.datetime.now()

        if (dateCreate.year == deadline.year and dateCreate.month == deadline.month and dateCreate.day == deadline.day): return False
        else: return True

    except:
        return True


