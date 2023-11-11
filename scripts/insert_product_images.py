import requests
import pandas 
from app.models import Product

electronics = pandas.read_csv('electronics.csv')

basepath = 'media/product_images'

def download_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        filepath = basepath + '/' + url.split('/')[-1]
        with open(filepath, 'wb') as fp:
            fp.write(response.content)

electronics.apply(lambda row: download_url(row['imgUrl']), axis = 1)