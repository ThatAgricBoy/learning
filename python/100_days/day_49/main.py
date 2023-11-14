#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:44:04 2021
scrapping data from a website
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "samueljohn3999@gmail.com"
ACCOUNT_PASSWORD = "Casemiro18?"
PHONE = "08138133145"

chrome_driver_path = "/home/max/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/view/3758777256/?alternateChannel=search&refId=GOs%2Be7tLPWC5FwTx0vHfFw%3D%3D&trackingId=Lre0wcFKlz9BoMDjLT9DGA%3D%3D")
time.sleep(5)

login_button = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn")
login_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
time.sleep(5)

sign_in_button = driver.find_element(
    By.CLASS_NAME, "login__form_action_container")
sign_in_button.click()

time.sleep(5)

apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
apply_button.click()

time.sleep(5)

phone_field = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone_field.text == "":
    phone_field.send_keys(PHONE)

submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")

if submit_button.get_attribute("data-control-name") == "continue_unify":
    submit_button.click()

review_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")

if review_button.get_attribute("data-control-name") == "review_unify":
    review_button.click()

time.sleep(5)
submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")

if submit_button.get_attribute("data-control-name") == "submit_unify":
    submit_button.click()
time.sleep(5)

driver.quit()
