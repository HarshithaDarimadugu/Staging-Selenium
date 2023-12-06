from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

import time

class renewalofcinemalicense():
    def renewal(self):
        driver = webdriver.Chrome()
        browser = driver.get('https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm')
        driver.maximize_window()
		
        driver.refresh()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.click()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.clear()
        ele1.send_keys('TSGOPR0002')
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.click()
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.clear()
        ele2.send_keys('123321')
        ele2.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.click()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.clear()
        ele1.send_keys('TSGOPR0002')
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.click()
        ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
        ele2.clear()
        ele2.send_keys('123321')
        ele2.send_keys(Keys.ENTER)
        time.sleep(5)
        
        alert = driver.find_element(By.XPATH,"//a[@class='close']").click()
        
        ele3 = driver.find_element(By.XPATH,"//input[@name='autocomplete']")
        time.sleep(5)
        ele3.send_keys('cinema')
        time.sleep(5)
        
        parent_handle = driver.current_window_handle
        print(parent_handle)
        
        ele4 = driver.find_element(By.XPATH,"//h1[normalize-space()='RENEWAL OF CINEMA LICENCE']")
        ele4.click()
        time.sleep(10)
        
        
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                ele6 = driver.find_element(By.XPATH,"//input[@name='txtTheaterOwnerName']")
                ele6.click()
                ele6.send_keys('Ramesh Babu')
                # ele6.send_keys(Keys.ENTER)
                time.sleep(5)
                
                # alert = driver.switch_to.alert
                # alert.accept()
                # time.sleep(5)
                
                ele7 = driver.find_element(By.XPATH,"//input[@name='txtAadharNo']")
                ele7.clear()
                ele7.send_keys('793182187432')
                # ele7.send_keys(Keys.ENTER)
                time.sleep(5)
            
                # alert1 = driver.switch_to.alert
                # alert1.accept()
                # time.sleep(5)
                
                ele8 = driver.find_element(By.XPATH,"//input[@name='txtFatHusName']")
                ele8.clear()
                ele8.send_keys('test father')
                # ele8.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele9 = driver.find_element(By.XPATH,"//select[@name='ddlGender']")
                ele9.click()
                ele9 = Select(ele9)
                ele9.select_by_visible_text('Female')
                time.sleep(5)
                
                ele10 = driver.find_element(By.XPATH,"//input[@name='txtMobile']")
                ele10.clear()
                ele10.send_keys('7386415182')
                time.sleep(5)
                
                ele11 = driver.find_element(By.XPATH,"//select[@name='ddlPerDistrict']")
                ele11.click()
                ele11 = Select(ele11)
                ele11.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele12 = driver.find_element(By.XPATH,"//select[@name='ddlPerMandal']")
                ele12.click()
                ele12 = Select(ele12)
                ele12.select_by_visible_text('ADILABAD RURAL')
                time.sleep(5)
                
                ele13 = driver.find_element(By.XPATH,"//select[@name='ddlPerVillage']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele13)
                # ele13 = driver.find_element(By.XPATH,"//select[@name='ddlPerVillage']")
                ele13.click()
                ele13 = Select(ele13)
                ele13.select_by_visible_text('HATTIGUTTA')
                time.sleep(5)
                
                ele14 = driver.find_element(By.XPATH,"//input[@name='txtPerLocality']")
                ele14.clear()
                ele14.send_keys('Hyderabad')
                time.sleep(5)
                
                ele15  = driver.find_element(By.XPATH,"//input[@name='txtTheaterName']")
                ele15.clear()
                ele15.send_keys('Satyam Theatres')
                time.sleep(5)
                
                ele16 = driver.find_element(By.XPATH,"//input[@name='txtLicenceNo']")
                ele16.click()
                ele16.send_keys('786586')
                time.sleep(5)
                
                ele17 = driver.find_element(By.XPATH,"//input[@name='txtLicenceDate']")
                ele17.click()
                time.sleep(3)
                ele18 = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
                ele18.click()
                ele18 = Select(ele18)
                ele18.select_by_visible_text('Oct')
                time.sleep(5)
                # ele19 = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
                # driver.execute_script('arguments[0].scrollIntoView(true);',ele19)
                # ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
                # driver.execute_script("window.scrollBy(0, -500);",ele19)
                # ele19.click()
                # ele19 = Select(ele19)
                # ele19.select_by_visible_text('2007')
                # ele19.send_keys('2007')
                ele19 = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
                ele20 = driver.find_element(By.XPATH,"//a[normalize-space()='16']")
                ele20.click()
                # ele19.send_keys(Keys.ENTER)
                ele19.click()
                time.sleep(5)
                
                ele21 = driver.find_element(By.XPATH,"//select[@name='ddlRenewalPeriod']")
                ele21.click()
                ele21 = Select(ele21)
                ele21.select_by_visible_text('2')
                time.sleep(5)
                
                ele22 = driver.find_element(By.XPATH,"//select[@name='ddlTheaterDistrict']")
                ele22.click()
                ele22 = Select(ele22)
                ele22.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele23 = driver.find_element(By.XPATH,"//select[@name='ddlTheaterMandal']")
                ele23.click()
                ele23 = Select(ele23)
                ele23.select_by_visible_text('ADILABAD RURAL')
                time.sleep(5)
                
                ele24 = driver.find_element(By.XPATH,"//select[@name='ddlTheaterVillage']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele24)
                # ele13 = driver.find_element(By.XPATH,"//select[@name='ddlPerVillage']")
                ele24.click()
                ele24 = Select(ele24)
                ele24.select_by_visible_text('ANUKUNTA')
                time.sleep(5)
                
                ele25 = driver.find_element(By.XPATH,"//input[@name='txtTheaterLocality']")
                ele25.clear()
                ele25.send_keys('Hyderabad')
                time.sleep(5)
                
                ele26 =driver.find_element(By.XPATH,"//input[@name='txtTheaterDoorNo']")
                ele26.click()
                ele26.send_keys('45/88/l')
                time.sleep(5)
                
                ele27 = driver.find_element(By.XPATH,"//input[@name='txtTheaterPinCode']")
                ele27.click()
                ele27.send_keys('500002')
                time.sleep(5)
                
                ele28 =driver.find_element(By.XPATH,"//input[@name='txtInformantName']")
                ele28.click()
                ele28.send_keys('test informant')
                time.sleep(5)
                
                ele29 = driver.find_element(By.XPATH,"//select[@name='ddlRelation']")
                ele29.click()
                ele29 = Select(ele29)
                ele29.select_by_visible_text('Father')
                time.sleep(5)
                
                ele30 =driver.find_element(By.XPATH,"//input[@name='chkApp$0']")
                ele30.click()
                time.sleep(3)
                ele31= driver.find_element(By.XPATH,"//input[@name='fileApp']")
                ele31.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele32 = driver.find_element(By.XPATH,"//input[@name='chkOriginalCinemaLicence$0']")
                ele32.click()
                time.sleep(3)
                ele33 = driver.find_element(By.XPATH,"//input[@name='fileOriginalCinemaLicence']")
                ele33.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele34 = driver.find_element(By.XPATH,"//input[@name='btnShowPayment']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele34)
                ele34.click()
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele35 = driver.find_element(By.XPATH,"//input[@name='btnConfirmPayment']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele35)
                ele35.click()
                time.sleep(5)
                
                ele38 = driver.find_element(By.XPATH,"//span[normalize-space()='CASH']")
                ele38.click()
                time.sleep(5)
                
                ele39 = driver.find_element(By.XPATH,"//input[@id='paymentsubmit']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele39)
                ele39.click()
                time.sleep(5)
                time.sleep(15)
                
                
                
                
                
                break
                driver.close()
                time.sleep(5)
license = renewalofcinemalicense()
license.renewal()