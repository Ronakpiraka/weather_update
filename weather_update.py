import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata= getdata("https://weather.com/en-IN/weather/today/l/21.1903,72.8644?par=google&temp=C/")
#htmldata = getdata("https://weather.com/en-IN/weather/today/l/a46cf32ca556e6d0f396fd2f2ba7f257b46d1aae334d8a16f7a1ff691cf5ee4d")
