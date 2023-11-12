#!/usr/bin/python3
"""
Scrapping with selenium
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/home/max/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome()

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Max")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Muster")
email = driver.find_element(By.NAME, "email")
email.send_keys("sammynatures2@gmail.com")
button = driver.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(5)
driver.quit()