# add cookies to requests in the next version

from bs4 import BeautifulSoup
import urllib.request
import json
import time
import re

magnit_url_lenobl = "https://magnitcosmetic.ru/local/ajax/get_city.php?region_id=1766"
magnit_url_spb = "https://magnitcosmetic.ru/local/ajax/get_city.php?region_id=1722"
city_url = "https://magnitcosmetic.ru/shops/?chcity="
magnit_ids_lenobl = []
magnit_ids_spb = []

lenobl_ids = urllib.request.urlopen(magnit_url_lenobl).read().decode('utf8')
time.sleep(2)
spb_ids = urllib.request.urlopen(magnit_url_spb).read().decode('utf8')

magnit_json_lenobl = json.loads(lenobl_ids)
magnit_json_spb = json.loads(spb_ids)

for id in magnit_json_lenobl:
	magnit_ids_lenobl.append(city_url + id.get('id'))

for id in magnit_json_spb:
	magnit_ids_spb.append(city_url + id.get('id'))

#def shop_counter(urls):
#	shops = 0
#	for url in urls:
#		html = urllib.request.urlopen(url).read()
#		soup = BeautifulSoup(html, 'html.parser')
#		shops += len(soup.find_all('div','shops__item')
#		time.sleep(2)
#	return shops

def url_printer(urls):
	for url in urls:
		print(url)

print("Магнит в области")
url_printer(magnit_ids_lenobl)
print("Магнит в городе")
url_printer(magnit_ids_spb)

#print("Магнит в области ", shop_counter(magnit_ids_spb))
#print("Магнит в городе ", shop_counter(magnit_ids_lenobl))