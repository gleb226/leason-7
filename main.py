import requests
from bs4 import BeautifulSoup

#help(requests)

#URL1 = 'https://coinmarketcap.com/'
URL2 = 'https://www.olx.ua/d/uk/transport/legkovye-avtomobili/'

#r = requests.get(URL1)
r = requests.get(URL2)

data = r.text

soup = BeautifulSoup (data, 'html.parser')

c = soup.find_all('h6')

# a = soup.find_all('a', {"href":"/currencies/bitcoin/markets/"
# })
# b = soup.find_all('a', {"href":"/currencies/ethereum/markets/"
# })
#
# print(a[0].text)
# print(b[0].text)

for c in c:
    print(c.text)
