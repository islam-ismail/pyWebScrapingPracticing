import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.sultan-center.com/fresh-food.html/fruit-veg.html')

soup = BeautifulSoup(response.text,'html.parser') 

products = soup.findAll(class_='item product product-item')


with open('products.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Img URL','Measurement']

    for product in products:
        title = product.find(class_='product-item-link').get_text().replace('\n','')
        img_url = product.find(class_= 'product-image-wrapper').find('img')['src']
        product_measurement = product.find(class_='product_measurement').find('span').get_text().replace('\n','')
        csv_writer.writerow([title,img_url,product_measurement])