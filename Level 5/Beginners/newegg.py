'''Web Scrapping is the process of extracting and collecting data
from websites and storing in a database or local machine

I will be using BeautifulSoup and Requests package to scrape Newegg site.

Newegg is an eCommerce website,  I would be scrapping products from Gaming category.
I would save the product name, price, shipping type/price, volume discounts

To start scraping let's import requests, beautiful soup and get the website url
It is also important to understand the basics of HTML and CSS selectors. We target content 
from a website using HTML tags, classes or/and ids'''

'''import libraries'''
import requests
from bs4 import BeautifulSoup
from csv import writer

'''declare url variable for the website'''
url = "https://www.newegg.com/PS5-Systems/SubCategory/ID-3762?cm_sp=Cat_PlayStation_1-_-VisNav-_-PS5-Systems"

'''Use the requests get method to fetch the data from the url'''
response = requests.get(url)

'''Check status, anything other than 200 -which means the data fetching was successful- indicates there is an error'''
# print(response.status_code)

'''Using the beautifulSoup to parse content from the page,
content function allows us to get all the contents in the website, '''

content = response.content
soup = BeautifulSoup(content, 'html.parser')
# print(soup)
#<title>Computer Parts, PC Components, Laptops, Gaming Systems, and more - Newegg.com</title>

# print(soup.title.get_text())
# Computer Parts, PC Components, Laptops, Gaming Systems, and more - Newegg.com

# print(soup.body)
# This gives the body of the entire website

'''Now we want to get the data we are looking for, first we have to find the parent category, so we would
access all the data we need'''

sections = soup.find_all('div', class_ ='item-cell')
#We used the find_all to find all the products items, we would be using a loop
# to find the product name, price, type of shipping and its discount
# I used underscore after the class to indicate that this is not a python class 
# but CSS

# open csv file and write the data we got into the csv file
with open('newegg_products.csv', 'w', encoding='utf8', newline='') as f:
    '''The writer would be responsible for writing into the file'''
    thewriter = writer(f)
    '''Now lets create a header for the file'''
    header = ['Product_Name', 'Price', 'Shipping Type', 'Discount']
    thewriter.writerow(header)
    for section in sections:
        product_name = section.find('a', class_= 'item-title').get_text()
        product_price = section.find('li', class_= 'price-current').get_text()
        price = product_price[:7]
        product_ship_type = section.find('li', class_= 'price-ship').get_text()
        product_discount=  section.find('span', class_= 'price-save-percent')
        discount = 'NaN' if product_discount == None else product_discount.get_text()
        # print(discount)
        info = [product_name, price, product_ship_type, discount]
        thewriter.writerow(info)
    

