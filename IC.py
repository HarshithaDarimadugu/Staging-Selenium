from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time


class multiple_windows():
    def multi_window(self):
    
        ## chrome driver in selenium
        driver =  webdriver.Chrome()
        element = driver.get("https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm")
        driver.maximize_window()
        
        driver.refresh()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.click()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.clear()
        ele1.send_keys('TSGOPR0001')
        ele2 = driver.find_element(By.XPATH, "//input[@id='password']")
        ele2 .click()
        ele2 = driver.find_element(By.XPATH, "//input[@id='password']")
        ele2.clear()
        ele2.send_keys('123321')
        ele2.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        
        ## entering the login name
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.click()
        ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
        ele1.clear()
        ele1.send_keys('TSGOPR0001')
        
        ## entering the password
        ele2 = driver.find_element(By.XPATH, "//input[@id='password']")
        ele2 .click()
        ele2 = driver.find_element(By.XPATH, "//input[@id='password']")
        ele2.clear()
        ele2.send_keys('123321')
        ele2.send_keys(Keys.ENTER)
        time.sleep(5)
        
        ## closing the alert notice
        alert = driver.find_element(By.XPATH,"//a[@class='close']").click()
        
        ## search item
        ele3 =  driver.find_element(By.ID,"autocomplete")
        ele3.send_keys('income')
        time.sleep(2)
        
        ## redirecting to the item page
        ele4 = driver.find_element(By.LINK_TEXT,'INCOME CERTIFICATE').click()
        
        ## Parent window
        parent_handle = driver.current_window_handle
        print(parent_handle) 
        time.sleep(3)
        
        ## handling the child window
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                time.sleep(3)
                field_clearing =  driver.find_element(By.XPATH,"//input[@name='btnClear']").click()
                
                ## switching to alert for clearing the fields
                alert = driver.switch_to.alert
                alert.send_keys('testing purpose')
                time.sleep(3)
                alert.accept()
                time.sleep(3)
                
                ## entering the the aadhar no
                ele5 = driver.find_element(By.XPATH,"//input[@name='txtAadharNo']")
                ele5.click()
                ele5.send_keys('968117817804')
                ele5.send_keys(Keys.ENTER) 
                alert1 = driver.switch_to.alert
                alert1.accept()
                alert2 = driver.switch_to.alert
                alert2.accept()
                time.sleep(5)
                
                ## entering the applicant name
                ele6 = driver.find_element(By.XPATH,"//input[@name='txtApplicantName']")
                ele6.click()
                ele6 = driver.find_element(By.XPATH,"//input[@name='txtApplicantName']")
                ele6.clear()
                ele6.send_keys('CHINNA')
                ele6.send_keys(Keys.ENTER)
                alert1 = driver.switch_to.alert
                alert1.accept()
                alert2 = driver.switch_to.alert
                alert2.accept()
                time.sleep(3)
                
                ## Father/Husband name
                ele7 = driver.find_element(By.XPATH,"//input[@name='txtFatHusName']")
                ele7.click()
                ele7.send_keys('VASU DEV')
                ele7.send_keys(Keys.ENTER)
                alert1 = driver.switch_to.alert
                alert1.accept()
                alert2 = driver.switch_to.alert
                alert2.accept()
                time.sleep(3)
                
                ## Mother name 
                ele8 = driver.find_element(By.XPATH,"//input[@name='txtmother']")
                ele8.click()
                ele8.send_keys('ANJALI DEVI')
                # alert1 = driver.switch_to.alert
                # alert1.accept()
                # alert2 = driver.switch_to.alert
                # alert2.accept()
                time.sleep(3)
                
                ##Gender
                ele9 = driver.find_element(By.XPATH,"//select[@name='ddlGender']")
                ele9.click()
                ele9 = Select(ele9)
                ele9.select_by_visible_text("Male")
                time.sleep(5)
                
                ##Door number
                ele10 = driver.find_element(By.XPATH,"//input[@name='txtPerDoorNo']")
                ele10.click()
                ele10.send_keys('185/99/02/cK')
                ele10.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ##landmark
                ele11 = driver.find_element(By.XPATH,"//input[@name='txtPerLocality']")
                ele11.click()
                ele11.send_keys('SRIKALAHASTHI')
                ele11.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ## District
                ele12 = driver.find_element(By.XPATH,"//select[@name='ddlPerDistrict']")
                ele12.click()
                ele12 = Select(ele12)
                ele12.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ## mandal
                ele13 = driver.find_element(By.XPATH,"//select[@name='ddlPerMandal']")
                ele13.click()
                ele13 = Select(ele13)
                ele13.select_by_visible_text('Adilabad Rural')
                time.sleep(5)
                
                ##  village
                ele14 = driver.find_element(By.XPATH,"//select[@name='ddlPerVillage']")
                # driver.execute_script("arguments[0].scrollIntoView(true);", ele14)
                ele14.click()
                select = Select(ele14)
                desired_option = "Ankapur"
                driver.execute_script("arguments[0].scrollIntoView(true);", ele14)
                select.select_by_visible_text(desired_option)
                time.sleep(10)
                            
                
                ##mobile
                ele15 = driver.find_element(By.XPATH,"//input[@name='txtMobile']")
                ele15.click()
                ele15.send_keys('7386415182')
                ele15.send_keys(Keys.ENTER)
                alert1 = driver.switch_to.alert
                alert1.accept()
                alert2 = driver.switch_to.alert
                alert2.accept()
                time.sleep(5)
                
                ##delivery type
                ele16 = driver.find_element(By.XPATH,"//select[@name='ddlDelivery']")
                ele16.click()
                ele16 = Select(ele16)
                ele16.select_by_visible_text('Manual')
                alert1 = driver.switch_to.alert
                alert1.accept()
                time.sleep(5)
                
                ##income on other
                ele17 = driver.find_element(By.XPATH,"//input[@name='txtOtherIncome']")
                driver.execute_script("arguments[0].scrollIntoView(true);", ele17)
                ele17.click()
                ele17 = driver.find_element(By.XPATH,"//input[@name='txtOtherIncome']")
                ele17.clear()
                ele17.send_keys('14321')              
                ele17.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ## purpose
                ele18 = driver.find_element(By.XPATH,"//select[@name='ddlPurpose']")
                ele18.click()
                ele18 = Select(ele18)
                ele18.select_by_visible_text('General')
                time.sleep(5)
                
                ## files upload - 1,2,3
                ele19 = driver.find_element(By.XPATH,"//input[@name='chkApp$0']")
                ele19.click()
                time.sleep(3)
                ele20 = driver.find_element(By.XPATH,"//input[@name='fileApp']")
                ele20.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele21 = driver.find_element(By.XPATH,"//input[@name='chkRation$0']")
                ele21.click()
                time.sleep(3)
                ele22 = driver.find_element(By.XPATH,"//input[@name='fileRation']")
                ele22.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
               
                ele23 = driver.find_element(By.XPATH,"//input[@name='ChkPhoto$0']")
                ele23.click()
                time.sleep(3)
                ele24 = driver.find_element(By.XPATH,"//input[@name='filePhoto']")
                ele24.send_keys('C:/Users/USER/Desktop/ph.jpg')
                time.sleep(5)
                
                ## show payment option
                ele25= driver.find_element(By.XPATH,"//input[@name='btnShowPayment']")
                ele25.click()
                time.sleep(7)
                alert1 = driver.switch_to.alert
                alert1.accept()
                time.sleep(5)
                
                ## confirm payment option
                ele26 = driver.find_element(By.XPATH,"//input[@name='btnConfirmPayment']")
                driver.execute_script("arguments[0].scrollIntoView(true);", ele26)
                ele26.click()
                time.sleep(5)
                
                ## payment selection
                ele27 = driver.find_element(By.XPATH,"//span[normalize-space()='CASH']")
                ele27.click()
                time.sleep(5)
                
                ## making payment
                ele28 = driver.find_element(By.XPATH,"//input[@id='paymentsubmit']")
                driver.execute_script("arguments[0].scrollIntoView(true);", ele28)
                ele28.click()
                time.sleep(30)
             
                # alert1 = driver.switch_to.alert
                # alert.accept()
                # time.sleep(10)
                break
                
                driver.close()
                time.sleep(5)
                
            
            
multiwind =  multiple_windows()
multiwind.multi_window()