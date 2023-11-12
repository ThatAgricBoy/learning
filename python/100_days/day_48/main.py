#!/usr/bin/python3
"""
Scrapping with selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/max/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/dp/B0BRCTJH6G/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t&aref=C9976734F1E931BB280B15310B14B2F081D983025609A22C94DB73A4F33E389B")

price_element = driver.find_element(By.ID, "taxInclusiveMessage")
price = price_element.text
print(price)
print("hello")
driver.quit()
