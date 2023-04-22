import requests
from bs4 import BeautifulSoup

#help(requests)

URL = 'https://github.com/gleb226/leason-7.git'

r = requests.get(URL)

data = r.text

soup = BeautifulSoup (data, 'html.parser')

