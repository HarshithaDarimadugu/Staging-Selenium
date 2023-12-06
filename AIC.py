from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class agricultuireincome():
    def agincomecert(self):
        driver = webdriver.Chrome()
        browser = driver.get('https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm')
        driver.maximize_window()
        time.sleep(5)
        
        driver.refresh()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.clear()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.click()
        ele1.send_keys('TSGOPR0001')
		#ele1.send_keys(Keys.ENTER)
        
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.clear()
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.click()
        ele2.send_keys('123321')
        ele2.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        
        ele3 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele3.clear()
        ele3 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele3.click()
        ele3.send_keys('TSGOPR0001')
		#ele1.send_keys(Keys.ENTER)
        
        ele4 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele4.clear()
        ele4 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele4.click()
        ele4.send_keys('123321')
        ele4.send_keys(Keys.ENTER)
        time.sleep(5)
        
        driver.close()
        time.sleep(5)

income = agricultuireincome()
income.agincomecert()