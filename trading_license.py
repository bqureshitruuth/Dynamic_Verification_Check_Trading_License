#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 02:29:59 2021

@author: bilalqureshi
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

browser.implicitly_wait(15)

browser.get('https://www.afca.org.au/make-a-complaint/findafinancialfirm/')
browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))

b=browser.find_element(By.XPATH, '/html/body/form/div[3]/div/div[4]/input')
b.send_keys('71400')
button=browser.find_element(By.XPATH,'//*[@id="ctl00_body_btnSearch"]')
button.click()
browser.find_element(By.XPATH,'//*[@id="ctl00_body_gvSearchResults"]/tbody/tr/td/div[3]/a').click()

textt=browser.find_element_by_class_name("memForAcr")

print(textt.text)
