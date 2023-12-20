from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.alert import alert
import time

driver= webdriver.Chrome()
ele1 = driver.get('https://admin-demo.nopcommerce.com/login')
time.sleep(3)
ele2 = driver.find_element(By.XPATH,"//input[@name='Email']")
ele2.clear()
ele2.send_keys('admin@yourstore.com')
ele2.send_keys(Keys.ENTER)
time.sleep(3)
ele13 = driver.find_element(By.XPATH,"//input[@name='Password']")
ele13.clear()
ele13 = driver.find_element(By.XPATH,"//input[@name='Password']")
ele13.send_keys('admin')
time.sleep(5)
ele14  = driver.find_element('5600 metre/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button')
ele14.click
time.sleep(49)

