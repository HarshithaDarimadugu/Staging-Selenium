from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

class templesevaboooking():
    def sevabooking(self):
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
        ele3.send_keys('raja')
        time.sleep(5)
        
        parent_handle = driver.current_window_handle
        print(parent_handle)
        
        ele4 = driver.find_element(By.LINK_TEXT,'SRI RAJA RAJESHWARA TEMPLE SEVA BOOKING').click()
        time.sleep(5)
        
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle !=parent_handle:
                driver.switch_to.window(handle)
                ele5 = driver.find_element(By.XPATH,"//select[@name='ddlSevaName']")
                ele5.click()
                ele5 = Select(ele5)
                # driver.execute_script("argument[0].scrollIntoView(true);",ele5)
                ele5.select_by_visible_text('Kalyanam')
                time.sleep(5)
                
                ele6 = driver.find_element(By.XPATH,"//select[@name='ddlBatches']")
                ele6.click()
                ele6 = Select(ele6)
                ele6.select_by_visible_text('10:30.AM to 12:30.PM')
                time.sleep(5)
                
                ele7 = driver.find_element(By.XPATH,"//input[@name='txtBookingDate']")
                time.sleep(2)
                el8 = driver.find_element(By.XPATH,"//img[@src='../../../Images/Calendar/cal.gif']").click()
                time.sleep(5)
                ele8 =driver.find_element(By.XPATH,"//a[@title='December 10']").click()     
                time.sleep(5)
                
                ele9 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtAadharNo']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele9)
                ele9.click()
                ele9 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtAadharNo']")
                ele9.clear()
                ele9.send_keys('968117817804')
                ele9.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele10 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtDevotName']")
                ele10.click()
                ele10 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtDevotName']")
                ele10.clear()
                ele10.send_keys('test devotee')
                ele10.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele11 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlProofDocument']")
                ele11.click()
                ele11 = Select(ele11)
                ele11.select_by_visible_text('ANY GOVT ID')
                time.sleep(5)
                
                docproofname = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtProofName']")
                # docproofname.click()
                # docproofname = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtProofName']")
                docproofname.clear()
                docproofname.send_keys('test doc')
                docproofname.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele12 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtProofNo']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele12)
                ele12.click()
                ele12 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtProofNo']")
                ele12.clear()
                ele12.send_keys('87866')
                ele12.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele13 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlGender']")
                ele13.click()
                ele13 = Select(ele13)
                ele13.select_by_visible_text('Female')
                time.sleep(5)
                
                ele14 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtMobile']")
                ele14.click()
                ele14 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtMobile']")
                ele14.clear()
                ele14.send_keys('7386415182')
                ele14.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele15 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlState']")
                ele15.click()
                ele15 = Select(ele15)
                ele15.select_by_visible_text('Telangana')
                time.sleep(5)
                
                ele16 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlDistrict']")
                ele16.click()
                ele16 = Select(ele16)
                ele16.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele17 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlMandal']")
                ele17.click()
                ele17 = Select(ele17)
                ele17.select_by_visible_text('ADILABAD RURAL')
                time.sleep(5)
                
                ele18 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlVillage']")
                ele18.click()
                ele18 = Select(ele18)
                ele18.select_by_visible_text('ANKAPUR')
                time.sleep(5)
                
                ele19 = driver.find_element(By.XPATH,"//input[@name='txtAppName']")
                ele19.click()
                ele19 = driver.find_element(By.XPATH,"//input[@name='txtAppName']")
                ele19.clear()
                ele19.send_keys('test Relation')
                ele19.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele20 = driver.find_element(By.XPATH,"//select[@name='ddlInfRelation']")
                ele20.click()
                ele20 = Select(ele20)
                ele20.select_by_visible_text('Husband')
                time.sleep(5)
                
                ele21 = driver.find_element(By.XPATH,"//input[@name='chkApplication']")
                ele21.click()
                time.sleep(3)
                ele21 = driver.find_element(By.XPATH,"//input[@name='fupApplication']")
                # ele21.click()
                ele21.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele22 = driver.find_element(By.XPATH,"//input[@name='chkProof']")
                ele22.click()
                time.sleep(3)
                ele22 = driver.find_element(By.XPATH,"//input[@name='fupProof']")
                # ele22.click()
                ele22.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele23 = driver.find_element(By.XPATH,"//input[@name='chkPhoto']")
                ele23.click()
                time.sleep(5)
                ele23 = driver.find_element(By.XPATH,"//input[@name='filePhoto']")
                # ele23.click()
                ele23.send_keys('C:/Users/USER/Desktop/ph.jpg')
                time.sleep(5)
                
                ele24 = driver.find_element(By.XPATH,"//input[@name='btnSubmit']")
                ele24.click()
                time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(10)
                
                ele25 = driver.find_element(By.XPATH,"//input[@name='chkAgree']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele25)
                ele25.click()
                time.sleep(3)
                
                ele26 = driver.find_element(By.XPATH,"//input[@name='btnConfirmPayment']")
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
        
		
booking = templesevaboooking()
booking.sevabooking()
