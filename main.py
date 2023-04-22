import requests
from bs4 import BeautifulSoup

#help(requests)

URL = 'https://coinmarketcap.com/'

r = requests.get(URL)

data = r.text

soup = BeautifulSoup (data, 'html.parser')

a = soup.find_all('a', {"href":"/currencies/bitcoin/markets/"
})
b = soup.find_all('a', {"href":"/currencies/ethereum/markets/"
})

print(a[0].text)
print(b[0].text)
