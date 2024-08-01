import requests
from bs4 import BeautifulSoup
import pandas as pd

# Sites
urls = {
    'Koro': 'https://www.korodrogerie.de/en/nuts',
    'Snackss': 'https://snackss.de/'
}

# Fiyatları toplamak için bir fonksiyon
def fetch_prices(url, site_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    
    # Koro sitesi için
    if site_name == 'Koro':
        products = soup.find_all('div', class_='product-item')
        for product in products:
            name_tag = product.find('h2', class_='product-title')
            price_tag = product.find('span', class_='price')
            if name_tag and price_tag:
                name = name_tag.text.strip()
                price = price_tag.text.strip()
                data.append((name, price))
    
    # Snackss sitesi için
    elif site_name == 'Snackss':
        products = soup.find_all('div', class_='product-item')
        for product in products:
            name_tag = product.find('h2', class_='product-title')
            price_tag = product.find('span', class_='price')
            if name_tag and price_tag:
                name = name_tag.text.strip()
                price = price_tag.text.strip()
                data.append((name, price))

    return data

# Verileri çek
koro_data = fetch_prices(urls['Koro'], 'Koro')
snackss_data = fetch_prices(urls['Snackss'], 'Snackss')

# Verileri DataFrame'e dönüştür
koro_df = pd.DataFrame(koro_data, columns=['Product', 'Price'])
snackss_df = pd.DataFrame(snackss_data, columns=['Product', 'Price'])

# Verileri karşılaştırma için birleştir
merged_df = pd.merge(koro_df, snackss_df, on='Product', how='outer', suffixes=('_Koro', '_Snackss'))

# Fiyatları karşılaştır
merged_df['Price_Difference'] = merged_df['Price_Koro'].str.replace('€', '', regex=False).astype(float) - merged_df['Price_Snackss'].str.replace('€', '', regex=False).astype(float)

# Sonuçları yazdır
print(merged_df)