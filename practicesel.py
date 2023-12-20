from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(5)

###########ID
# ele1 = driver.find_element(By.ID, 'name')
# ele1.click()
# ele1.send_keys('YG nd HSH')
# ele1.send_keys(Keys.ENTER)
# time.sleep(5)

###############name
# ele2 = driver.find_element(By.NAME,'gender')
# driver.execute_script('arguments[0].scrollIntoView(true);',ele2)
# ele2.click()
# time.sleep(5)                               

########### Relative XPATH
# ele3= driver.find_element(By.XPATH,"//label[@for='saturday']")
# ele3.click()
# time.sleep(5)

########## relative xpath of an alert
# ele4 = driver.find_element(By.XPATH,"//button[@onclick='myFunctionAlert()']")
# driver.execute_script('arguments[0].scrollIntoView(true);',ele4)
# ele4.click()
# time.sleep(5)
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(5)

############ class name
# ele5 = driver.find_elements(By.CLASS_NAME, "form-group")
# print(len(ele5))
# print(ele5[0].text)
# print("------------------------")
# print(ele5[1].text)
# print("------------------------")
# print(ele5[3].text)
# print("------------------------")
# print(ele5[4].text)
# print("------------------------")
# print(ele5[5].text)

# for i in ele5:
    # print(len(i))
    # if len(i)>len(ele5):
        # i[len(ele).click()]
# time.sleep(5)

