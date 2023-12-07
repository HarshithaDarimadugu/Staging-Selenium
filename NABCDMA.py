from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

class nonavailbirth():
    def birthappli(self):
        driver = webdriver.Chrome()
        browser = driver.get('https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm')
        driver.maximize_window()
        time.sleep(5)
		
		
        driver.refresh()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.click()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.clear()
        ele1.send_keys('TSGOPR0001')
		#ele1.send_keys(Keys.ENTER)
        
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.click()
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.clear()
        ele2.send_keys('123321')
        ele2.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        
        ele3 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele3.click()
        ele3 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele3.clear()
        ele3.send_keys('TSGOPR0001')
		#ele1.send_keys(Keys.ENTER)
        
        ele4 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele4.click()
        ele4 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele4.clear()
        ele4.send_keys('123321')
        ele4.send_keys(Keys.ENTER)
        time.sleep(5)
        
        alert = driver.find_element(By.XPATH,"//a[@class='close']").click()
        
        ele5 = driver.find_element(By.XPATH,"//input[@name='autocomplete']")
        time.sleep(5)
        ele5.send_keys('birth cdma')
        time.sleep(5)
        
        parent_handle = driver.current_window_handle
        print(parent_handle)
        
        ele6 = driver.find_element(By.XPATH,"//div[@id='outputcontent1']//h1[@class='f_headline'][normalize-space()='NON AVAILABILITY BIRTH CDMA']")
        ele6.click()
        time.sleep(5)
        
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                ele7 = driver.find_element(By.XPATH,"//input[@name='txtChildName']")
                ele7.click()
                ele7.send_keys('test child')
                ele7.send_keys(Keys.ENTER)
                # time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                
                ele8 = driver.find_element(By.XPATH,"//select[@name='ddlForH']")
                ele8.click()
                ele8= Select(ele8)
                ele8.select_by_visible_text('Daughter Of')
                # time.sleep(5)
                
                ele9  =driver.find_element(By.XPATH,"//input[@name='txtForHName']")
                ele9.click()
                ele9.send_keys('test father')
                ele9.send_keys(Keys.ENTER)
                # time.sleep(5)
				
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                
                ele10 = driver.find_element(By.XPATH,"//input[@name='txtMotherName']")
                ele10.click()
                ele10.send_keys('test mother')
                ele10.send_keys(Keys.ENTER)
                # time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                
                ele11 = driver.find_element(By.XPATH,"//input[@name='txtDateOfBirth']")
                ele11.click()
                ele12 = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
                ele12.click()
                ele12 = Select(ele12)
                ele12.select_by_visible_text('Jul')
                ele13 = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
                ele13.click()
                ele13 = Select(ele13)
                ele13.select_by_visible_text('2019')
                ele14 = driver.find_element(By.XPATH,"//a[normalize-space()='10']")
                ele14.click()
                time.sleep(5)
                
                ele15 = driver.find_element(By.XPATH,"//select[@name='ddlEventPlace']")
                ele15.click()
                ele15 = Select(ele15)
                ele15.select_by_visible_text('Hospital')
                time.sleep(5)
                
                ele16 = driver.find_element(By.XPATH,"//input[@name='txtHorRName2']")
                ele16.click()
                ele16.send_keys('Devi Hospital')
                ele16.send_keys(Keys.ENTER)
                # time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele17 = driver.find_element(By.XPATH,"//input[@name='txtHorRAddr1']")
                ele17.click()
                ele17.send_keys('ADILABAD')
                ele17.send_keys(Keys.ENTER)
                # time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele18 = driver.find_element(By.XPATH,"//input[@name='txtHorRAddr2']")
                ele18.click()
                ele18.send_keys('ADILABAD')
                ele18.send_keys(Keys.ENTER)
                # time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele19 = driver.find_element(By.XPATH,"//input[@name='txtHorRAddr3']")
                ele19.click()
                ele19.send_keys('ADILABAD')
                ele19.send_keys(Keys.ENTER)
                # time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele20 = driver.find_element(By.XPATH,"//select[@name='ddlDistrict']")
                ele20.click()
                ele20 = Select(ele20)
                ele20.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele21 = driver.find_element(By.XPATH,"//select[@name='ddlMPType']")
                ele21.click()
                ele21 = Select(ele21)
                ele21.select_by_visible_text('Greater Municipality')
                time.sleep(5)
                
                # ele22 = 
                break
                
                driver.close()
                time.sleep(5)
				

birth = nonavailbirth()
birth.birthappli()