from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from urllib.request import urlopen
import threading
eMails = []
urls = []
last_urls =[]

option = Options()
option.add_argument("--disable-infobars") 
browser = webdriver.Chrome('C:\webdr\chromedriver.exe',chrome_options=option)
# 'https://xn--90adear.xn--p1ai/check/auto' –  ГИБДД.РФ
browser.get('https://xn--90adear.xn--p1ai/check/auto')

    #Парсим полученную страницу
    soup = BeautifulSoup(page, 'html.parser')
    #Получаем все теги-ссылки
    page_urls = soup.findAll('a')
    
     #Добавляем адреса сайтов в список и запусткаем обработку полученного полученного сайта в отдельном потоке
    for element in urls_tag:
        urls.append(element.string)
        events.append(threading.Thread(target=startFinder,args=('http://' + element.string, 3,element.string)))
        #Запускаем поток
        events[-1].start()   
    i=i+1
i = 1
while i<=5:
    page = urlopen("https://esir.gov.spb.ru/category/22/?page="+str(i))
    soup = BeautifulSoup(page, 'html.parser')
    urls_tag = soup.findAll(attrs={"class":"small"})
    for element in urls_tag:
        urls.append(element.string)
        events.append(threading.Thread(target=startFinder,args=('http://' + element.string, 3,element.string)))
        events[-1].start()
    i=i+1  
   
    for element in page_urls:
        #Если тег не пустой
        if element.string != None:
            if element.string.find('@')>=0:
                # Мы нашли e-mail, возвращаем его
                eMail = element.string
                return eMail
            else:               
                # Если время жизни паука еще не кончилось
                if TTL > 0:
                    try:
                        #Проверяем, что ссылка на страницу и еще не была посещена и находится в пределах обыскиваемого сайта
                        if element['href'].find(mainUrl) >= 0 and last_urls.count(element['href'])<1:
                            #Добавляем ссылку в посещенные
                            last_urls.append(element['href'])
                            #Пробуем получить e-mail с этой страницы, уменьшив время жизни
                            eMail_1 = findEmail(element['href'], TTL-1,mainUrl)
                        #Если получили в результате адрес почты
                        if eMail_1.find('@')>=0:
                            return eMail_1
                    except Exception:
                        eMail_1 = ''
                            
    return eMail

#Фукция-обертка для удобного запуска потока
def startFinder(url, TTL, mainUrl):
    #Отчитываемся о том, что запустили поток
    print("thread " + mainUrl + " start \n")
    #Ищем адреса на сайте (mainUrl нужен для того, чтобы оставаться в пределах сайта)
    eM = findEmail(url, TTL,mainUrl)
    #Добавляем в список
    eMails.append(eM)

events = []
i = 1
while i<=26: #На сайте 26 страниц с полезной иформацией
    # Загружаем страницу
    page = urlopen("https://esir.gov.spb.ru/category/21/?page="+str(i)) 
    
    #Парсим страницу с помощью BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')
    
    #Получаем со страницы все теги с классом small
    urls_tag = soup.findAll(attrs={"class":"small"})
    
   
class TMSParser(object):
    """ Can interpret messages coming back from a TMS server conforming to the
        Dublin Core standard as customized by Fabrique.
        Check the tms/xsd folder to get a feel for the xml format
        The parse method reads an xml response and creates a list of Record(s)
    """
    def __init__(self,disable_validation=False):
        if disable_validation:
            self.disable_validation = True
        else:
            self.disable_validation = False

    def validate(self,xml_file, schema='apps/tms/xsd/fabrique-dc.cached.xsd'):
        if self.disable_validation:
            return True
        #parse the xsd
        xmlschema_doc = etree.parse(file(schema))
        xmlschema = etree.XMLSchema(xmlschema_doc)

        #parse xml message
        doc = etree.parse(xml_file)

        #validate
        return xmlschema.validate(doc)

    def _xml_parse_and_validate(self,xml_file, schema='apps/tms/xsd/fabrique-dc.cached.xsd'):
        #parse the xsd
        xmlschema_doc = etree.parse(file(schema))
        xmlschema = etree.XMLSchema(xmlschema_doc)

        #parse xml message
        doc = etree.parse(xml_file)

        #return validation result and actual parsed response
        return xmlschema.validate(doc),doc

    def _xml_parse(self,xml_file, schema='apps/tms/xsd/fabrique-dc.cached.xsd'):
        doc = etree.parse(xml_file)
        return doc
#Завершаем потоки
for e in events:
    e.join()
#Открываем файл на запись (Если файла нет, он создастся автоматически)
f = open( 'emails.txt', 'w' )
var a = 20

#Записываем по очереди на отдельные строки все элементы полученного списка
for item in eMails:
    #Если длинна больше трех (убираем пустые строки с сайтов, где не было найдено e-mail)
    if len(item) > 3:
        print(item)
        f.write("%s\n" % item)
#Закрываем файл
f.close()
