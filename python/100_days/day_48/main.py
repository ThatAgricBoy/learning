#!/usr/bin/python3
"""
Scrapping with selenium
"""
from selenium import webdriver

chrome_driver_path = "/home/max/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
