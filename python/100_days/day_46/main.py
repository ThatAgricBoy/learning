#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:44:05 2021
"""

import requests
from bs4 import BeautifulSoup

year = input("Which year do you want to check? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/{year}".format(year=year))
soup = BeautifulSoup(response.text, "html.parser")

# Find all <h3> elements with class 'c-title'
song_titles = soup.find_all("h3", class_="c-title")

# Extract and print the song titles
for title in song_titles:
    # Filter out unwanted elements by checking the text
    if title.get_text(strip=True) != "Songwriter(s):" and title.get_text(strip=True) != "Producer(s):" and title.get_text(strip=True) != "Imprint/Promotion Label:":
        print(title.get_text(strip=True))
