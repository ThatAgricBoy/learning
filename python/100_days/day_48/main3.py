#!/usr/bin/python3
"""
Scrapping with selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/max/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome()

driver.get("https://www.python.org/")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")
for event in events:
    event_time = event.find_element(By.TAG_NAME, "time")
    event_name = event.find_element(By.TAG_NAME, "a")
    event_date = event_time.get_attribute("datetime").split("T")[0]
    event_name = event_name.text
    print(f"{event_date}: {event_name}")
driver.quit()
