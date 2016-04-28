import urllib2
from bs4 import BeautifulSoup
import time


url = "http://www.cricbuzz.com/"

requester = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})

url_opener = urllib2.urlopen(requester)

url_reader = url_opener.read()

soup = BeautifulSoup(url_reader, "lxml")

#text = soup.get_text()

for tags in soup.findAll(['script', 'style']):
 	tags.extract()


Feautred_list = soup.findAll('div',attrs={'class': 'cb-col-100 cb-col cb-hm-scg-blk'})


print soup	



