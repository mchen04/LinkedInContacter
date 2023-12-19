import requests
from bs4 import BeautifulSoup
from lxml import etree

html_text = requests.get('https://www.zillow.com/homes/riverside_rb/?utm_medium=cpc&utm_source=google&utm_content=302449236|21530175156|kwd-1002616223|217524502787|&semQue=null&gad_source=1&gclid=Cj0KCQiA3uGqBhDdARIsAFeJ5r3SxbrKxNS-zK5Ypc3-HMG8jTVNsjBEYzRk3WtNJkd6Xsgi1H-3mtsaAirZEALw_wcB')
html_text = html_text.content
soup = BeautifulSoup(html_text, 'lxml') 
address = soup.find_all('div', class_= 'hdp__sc-13x5vko-0 laMHWb')
print(address)
