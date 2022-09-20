#!/usr/bin/python3
"""
Scrip so scraping the images and save in a folder
with respective Scientific name
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 


species = ['Axinaea macrophylla']


for specie in species:
    driver = webdriver.Chrome('C:/chromedriver.exe')
    #Opens up web driver and goes to Google Images
    driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')
    
    box = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    
    box.send_keys(specie)
    box.send_keys(Keys.ENTER)
    
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height
    
    
    for i in range(1, 1000):
        try:
            image = '//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(str(i))
            driver.find_element(By.XPATH, image).click()
            image_full = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img'
            driver.find_element(By.XPATH, image_full).screenshot('C:/Users/CARLOS/Desktop/Plant identification/Schinus mole/{}.png'.format(str(i)))
        except:
            pass