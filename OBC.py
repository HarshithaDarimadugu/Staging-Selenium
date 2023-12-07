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
        ele5.send_keys('obc')
        time.sleep(5)
        
        parent_handle = driver.current_window_handle
        print(parent_handle)
        
        ele6 = driver.find_element(By.XPATH,"//h1[normalize-space()='OBC CERTIFICATE']")
        ele6.click()
        time.sleep(5)
        
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                ele6 = driver.find_element(By.XPATH,"//input[@name='txtAppName']")
                ele6.click()
                ele6.send_keys('test name')
                time.sleep(5)
				
                ele7 = driver.find_element(By.XPATH,"//select[@name='ddlRelation']")
                ele7.click()
                ele7 = Select(ele7)
                ele7.select_by_visible_text('D/O')
                time.sleep(5)
                
                ele8 = driver.find_element(By.XPATH,"//input[@name='txtFather']")
                ele8.click()
                ele8.send_keys('test relation')
                time.sleep(5)
                
                ele9 = driver.find_element(By.XPATH,"//select[@name='ddlGender']")
                ele9.click()
                ele9 = Select(ele9)
                ele9.select_by_visible_text('Female')
                time.sleep(5)
                
                ele10 = driver.find_element(By.XPATH,"//select[@name='ddlPerDistrict']")
                ele10.click()
                ele10 = Select(ele10)
                ele10.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele11 = driver.find_element(By.XPATH,"//select[@name='ddlPerMandal']")
                ele11.click()
                ele11 = Select(ele11)
                ele11.select_by_visible_text('ADILABAD (URBAN)')
                time.sleep(5)
                
                ele12 = driver.find_element(By.XPATH,"//select[@name='ddlPerVillage']")
                ele12.click()
                ele12 = Select(ele12)
                ele12.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele13 = driver.find_element(By.XPATH,"//input[@name='txtMobile']")
                ele13.click()
                ele13.send_keys('7386415182')
                time.sleep(5)
                
                ele14= driver.find_element(By.XPATH,"//select[@name='ddlDelivery']")
                ele14.click()
                ele14 = Select(ele14)
                ele14.select_by_visible_text('Manual')
                time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele15 = driver.find_element(By.XPATH,"//select[@name='ddlPerState']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele15)
                ele15.click()
                ele15 = Select(ele15)
                ele15.select_by_visible_text('Telangana')
                time.sleep(5)
                
                ele16 = driver.find_element(By.XPATH,"//select[@name='ddlIssuedCertificate']")
                ele16.click()
                ele16 = Select(ele16)
                ele16.select_by_visible_text('Yes')
                time.sleep(5)
                
                ele17 = driver.find_element(By.XPATH,"//select[@name='ddlCasteClaimed']")
                ele17.click()
                ele17 = Select(ele17)
                ele17.select_by_visible_text('Mudiraj')
                time.sleep(5)
                
                ele18 = driver.find_element(By.XPATH,"//select[@name='ddlEcaste']")
                ele18.click()
                ele18 = Select(ele18)
                ele18.select_by_visible_text('Yes')
                time.sleep(5)
                
                ele19 = driver.find_element(By.XPATH,"//select[@name='ddlPurpose']")
                ele19.click()
                ele19 = Select(ele19)
                ele19.select_by_visible_text('CENTRAL GOVERNMENT')
                time.sleep(5)
                
                ele20 = driver.find_element(By.XPATH,"//select[@name='ddlReligion']")
                ele20.click()
                ele20 = Select(ele20)
                ele20.select_by_visible_text('Hindu')
                time.sleep(5)
                
                ele21 = driver.find_element(By.XPATH,"//input[@name='txtIncome']")
                ele21.click()
                ele21.send_keys('10000')
                time.sleep(5)
                
                ele22 = driver.find_element(By.XPATH,"//input[@name='chkOBCApp$0']")
                ele22.click()
                time.sleep(5)
                
                ele23 = driver.find_element(By.XPATH,"//input[@name='FileOBCApp']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele23)
                ele23.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele24 = driver.find_element(By.XPATH,"//input[@name='chkDec']")
                ele24.click()
                time.sleep(5)
                
                ele25 = driver.find_element(By.XPATH,"//input[@name='btnSubmit']")
                ele25.click()
                time.sleep(5)
				
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele26 = driver.find_element(By.XPATH,"//input[@name='btnConfirmPayment']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele26)
                ele26.click()
                time.sleep(5)
                
                ele27 = driver.find_element(By.XPATH,"//span[normalize-space()='CASH']")
                ele27.click()
                time.sleep(5)
                
                ele28 = driver.find_element(By.XPATH,"//input[@id='paymentsubmit']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele28)
                ele28.click()
                time.sleep(5)
                time.sleep(15)
                
                break
                
                driver.close()
                time.sleep(5)
				

birth = nonavailbirth()
birth.birthappli()