from bs4 import BeautifulSoup
import urllib.request
import re

riv_shops = []
riv_shops_count = 0
riv_closed_shops_count = 0
riv_city = 0
riv_oblast = 0
riv_url = "http://www.rivegauche.ru/shops/cities/sankt-peterburg"
riv_contents = urllib.request.urlopen(riv_url).read()
riv_soup = BeautifulSoup(riv_contents, 'html.parser')

for shop in riv_soup.find_all('div','shops_rivegauche'):
	riv_shops.append(shop)
	riv_shops_count += 1
	
for shop in riv_shops:
	if (shop.find('span','subway') and not shop.find(text=re.compile('Магазин закрыт'))):
		riv_city += 1
	if (shop.find(text=re.compile('Лен. Обл')) and not shop.find(text=re.compile('Магазин закрыт'))):
		riv_oblast += 1
	if (shop.find(text=re.compile('закрыт'))):
		riv_closed_shops_count += 1
		
print("Рив Гош в городе ", riv_city)
print("Рив Гош в области ", riv_oblast)
print("Рив Гош всего ", riv_oblast + riv_city)
print("Для проверки: всего открытых магазинов - ", riv_shops_count - riv_closed_shops_count)
print("Проверка считает разницу всех блоков с магазинами и всех слов 'закрыт'")
print('\n')

pod_shops = []
pod_shops_count = 0
pod_closed_shops_count = 0
pod_city = 0
pod_oblast = 0
pod_url = "https://www.podrygka.ru/shoplist/?set_filter=y&arrShopsSmartFilter_68=450215437"
pod_contents = urllib.request.urlopen(pod_url).read()
pod_soup = BeautifulSoup(pod_contents, 'html.parser')

for shop in pod_soup.find_all('div','shops-list-item'):
	pod_shops.append(shop)
	pod_shops_count += 1
	
for shop in pod_shops:
	if (shop.find(text=re.compile('Санкт-Петербург,'))):
		pod_city += 1
	else:
		pod_oblast += 1
	if (shop.find(text=re.compile('закрыт'))):
		pod_closed_shops_count += 1
		
print("Подружек в городе ", pod_city)
print("Подружек в области ", pod_oblast)
print("Подружек всего ", pod_oblast + pod_city)
print("Для проверки: всего магазинов - ", pod_shops_count)
print("Найдено слов 'закрыт' - ", pod_closed_shops_count)
print("Проверка считает количество блоков с магазинами и слов 'закрыт'")
print('\n')