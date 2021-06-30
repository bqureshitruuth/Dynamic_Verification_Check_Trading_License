#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 02:29:59 2021

@author: bilalqureshi
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
df = pd.DataFrame(columns=['id','message'])

browser.implicitly_wait(6)
for x in range(71400,71450):
    browser.get('https://www.afca.org.au/make-a-complaint/findafinancialfirm/')
    try:
        browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))

        b=browser.find_element(By.XPATH, '/html/body/form/div[3]/div/div[4]/input')
        b.send_keys(str(x))
        button=browser.find_element(By.XPATH,'//*[@id="ctl00_body_btnSearch"]')
        button.click()
        textt=browser.find_element(By.XPATH,'//*[@id="ctl00_body_gvSearchResults"]')
        textv=browser.find_element(By.XPATH,'//*[@id="ctl00_body_gvSearchResults"]/tbody/tr/td/div[1]/span[1]/span') 
        message=''
        if(str(textv.text)!=str(x)):
            message="Invalid id"
            
        else:
                print(textt.text)
                
    except NoSuchElementException as exc:
        print("Invalid ID "+str(x))
