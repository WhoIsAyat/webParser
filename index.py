import requests
from bs4 import BeautifulSoup

# Site URL
url = 'https://openshop.uz/'

# Making an HTTP request to the site
response = requests.get(url)

# Opening a file for writing
with open('result.txt', 'w', encoding='utf-8') as file:
    if response.status_code == 200:
        #Find all product blocks (code adaptation may be required)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #Find all product blocks (code adaptation may be required)
        products = soup.find_all('div', class_='product-wrap')  #Example class, replace with the current one
        
        for product in products:
            # Retrieving the product name
            title = product.find('h3', class_='product-name')  #Example class, replace with the current one
            title_text = title.get_text(strip=True) if title else 'Title not found'
            
            # Retrieving the price of the product
            price = product.find('ins', class_='new-price')  #Example class, replace with the current one
            price_text = price.get_text(strip=True) if price else 'Price not found'
            
            #write information to a file
            file.write(f'Name: {title_text}\n')
            file.write(f'Price: {price_text}\n')
            file.write('-' * 40 + '\n')
    else:
        file.write('Failed to access the site\n')

print('results are saved in result.txt!')


