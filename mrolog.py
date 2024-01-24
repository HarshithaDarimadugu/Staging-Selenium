from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time

class dept():
    def mrologin(self):
        driver = webdriver.Chrome()
        driver.get('https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm')
        driver.maximize_window()
        
        driver.refresh()
        e_1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        e_1.click()
        e_1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        e_1.clear()
        e_1.send_keys('ADB-ADB-MRO-1')
        
        e_2 = driver.find_element(By.XPATH,"//input[@name='password']")
        e_2.click()
        e_2 = driver.find_element(By.XPATH,"//input[@name='password']")
        e_2.clear()
        e_2.send_keys('123321')
        e_2.send_keys(Keys.ENTER) 
        
        
        e_3 = driver.find_element(By.LINK_TEXT,"Application Processing")
        e_3.click()
        
        e_5 = driver.find_element(By.LINK_TEXT,"Family Membership Certificate Requests")
        e_5.click()
        time.sleep(7)
        
        e_6 = driver.find_element(By.XPATH,"//input[@name='btnSearch']")
        e_6.click()
        time.sleep(5)
        
        e_7 = driver.find_element(By.XPATH,"//table[@id='Table1']/tbody/tr[2]/td/table/tbody/tr[12]/td/a[3]")
        driver.execute_script('arguments[0].scrollIntoView(true);',e_7)
        e_7.click()
        time.sleep(5)
        
        e_8 = driver.find_element(By.XPATH,"//table[@id='Table1']/tbody/tr[2]/td/table/tbody/tr[4]/td")
        e_8.click()
        time.sleep(5)
        
        e_9 = driver.find_element(By.XPATH,"//textarea[@name='txtRemarks']")
        e_9.click()
        e_9.send_keys("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
        
        e_10 = driver.find_element(By.XPATH,"//input[@name='btnProceed']")
        e_10.click()
        time.sleep(10)
        
        e_11= driver.find_element(By.XPATH,"//table[@id='rblActionTaken']/tbody/tr[5]/td/input")
        driver.execute_script('arguments[0].scrollIntoView(true);',e_11)
        e_11.click()
        
        e_12= driver.find_element(By.XPATH,"//table[@id='rblActionTaken']/tbody/tr[5]/td/input")
        driver.execute_script('arguments[0].scrollIntoView(true);',e_12)
        e_12.click()
        
        e_13 = driver.find_element(By.XPATH,"//select[@name='ddltobereview']")
        e_13.click()
        e_13 = Select(e_13)
        e_13.select_by_visible_text('Send for field verification')
        time.sleep(5)
        
        e_14 = driver.find_element(By.XPATH,"//input[@name='btnSubmit']")
        e_14.click()
        time.sleep(5)
        
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        
        time.sleep(5)
        driver.quit()
    
obj = dept()
obj.mrologin()