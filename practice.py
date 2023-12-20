from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

driver= webdriver.Chrome()
ele1 = driver.get('https://admin-demo.nopcommerce.com/login')
time.sleep(3)
ele2 = driver.find_element(By.XPATH,"//input[@name='Email']")
ele2.clear()
time.sleep(5)
ele2 = driver.find_element(By.XPATH,"//input[@name='Email']")
ele2.send_keys('admin@yourstore.com')
ele2.send_keys(Keys.ENTER)
time.sleep(3)
ele3 = driver.find_element(By.NAME,"Password")
ele3.clear()
time.sleep(5)
ele3 = driver.find_element(By.NAME,"Password")
ele3.send_keys('admin')
ele3.send_keys(Keys.ENTER)
time.sleep(5)
ele4  = driver.find_element(By.XPATH,"//button[@type='submit']")
ele4.click
time.sleep(5)
driver.close()
time.sleep(5)

