#!/usr/bin/python3
"""
Price scraping on Amazon
"""
import requests
from lxml import html

url = "https://www.amazon.com/Bluetooth-Detachable-Surround-Mountable-Separable/dp/B0CH3BM6M8/ref=sr_\
    1_5?crid=3QAZ99PIYXNN8&keywords=home+theater+sound+system&qid=1699132693&refinements=p_36%3A1253504011&rnid=\386442011&s=electronics&sprefix=home+thea%2Caps%2C851&sr=1-5"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "PHPSESSID=09d96249599b5820f29cc768507b21a4"
}

product_name = "Bluetooth Sound Bars for TV"
response = requests.get(url, headers=headers)
response.raise_for_status()
data = html.fromstring(response.content)
product_title = data.xpath('//span[@id="productTitle"]/text()')
if product_name in product_title[0].strip():
    # Split the product title by spaces and select the first five words
    product_title_words = product_title[0].strip().split()[:5]
    product_title = " ".join(product_title_words)
    
    price = data.xpath('//span[@class="a-price"]/span[@class="a-offscreen"]/text()')
    print("We found what you are looking for: ", product_title)
    if price:
        print("The current price is:", price[0])
