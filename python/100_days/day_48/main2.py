#!/usr/bin/python3
"""
Scrapping with selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/max/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome()

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
driver.quit()