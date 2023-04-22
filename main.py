try:
    import requests
    from bs4 import BeautifulSoup
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
except Exception as e:
    print(e)

#help(requests)

try:
    #URL1 = 'https://coinmarketcap.com/'
    URL2 = 'https://www.olx.ua/d/uk/transport/legkovye-avtomobili/'

    #r = requests.get(URL1)
    r = requests.get(URL2)

    data = r.text

    soup = BeautifulSoup (data, 'html.parser')

    c = soup.find_all('h6')
    d = soup.find_all('p')

    # a = soup.find_all('a', {"href":"/currencies/bitcoin/markets/"
    # })
    # b = soup.find_all('a', {"href":"/currencies/ethereum/markets/"
    # })
    #
    # print(a[0].text)
    # print(b[0].text)

    for c in c:
        print(c.text)
    for d in d:
        print(d.text)
except Exception as e:
    print(e)

try:
    uri = "mongodb+srv://gmedvede226:1234@cluster0.sx5570k.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
except Exception as e:
    print(e)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client['Medvediev']
    collection = db['Items']

    for c in c:
        print(c.text)
        collection.insert_one({'Item': c.text})


except Exception as e:
    print(e)

