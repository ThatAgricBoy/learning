#!/usr/bin/env python3
"""
Capstone web scrapping project.
using beautiful soup and selenium
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests


url = "https://www.zillow.com/fl/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A33.67588673962528%2C%22south%22%3A21.480662396646984%2C%22east%22%3A-74.55411271875002%2C%22west%22%3A-93.05508928125002%7D%2C%22mapZoom%22%3A6%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3A188055%2C%22max%22%3A564166%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A14%2C%22regionType%22%3A2%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Safari/537.36",
}

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfP1CN1paZo7vlHexPEy8HB5RSLDQJh5eLGSdbrZgPfVjtxWQ/viewform"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
all_links = soup.find_all(
    name="a", class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link")

all_links_list = []
for link in all_links:
    href = link.get("href")
    if "https" not in href:
        all_links_list.append(f"https://www.zillow.com{href}")
    else:
        all_links_list.append(href)

all_prices = soup.find_all(
    name="span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
all_prices_list = []
for price in all_prices:
    all_prices_list.append(price.getText())

all_addresses = soup.find_all(name="address")
all_addresses_list = []
for address in all_addresses:
    all_addresses_list.append(address.getText())


chrome_driver_path = "/home/max/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome()
driver.get(form_url)


for n in range(len(all_links_list)):
    driver.get(form_url)

    time.sleep(2)
    address = all_addresses_list[n]
    price = all_prices_list[n]
    link = all_links_list[n]

    # Find input elements
    address_input = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # Clear existing values
    address_input.clear()
    price_input.clear()
    link_input.clear()

    # Fill in the input fields
    address_input.send_keys(address)
    price_input.send_keys(price)
    link_input.send_keys(link)

    # Submit the form
    submit_button = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()

    # Wait for a while to ensure the submission is complete
    time.sleep(2)

driver.quit()
