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
        ele5.send_keys('income')
        time.sleep(5)
        
        parent_handle = driver.current_window_handle
        print(parent_handle)
        
        ele6 = driver.find_element(By.XPATH,"//div[@id='outputcontent1']//h1[@class='f_headline'][normalize-space()='AGRICULTURE INCOME CERTIFICATE']")
        ele6.click()
        time.sleep(10)
        
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                ele7 = driver.find_element(By.XPATH,"//input[@name='txtApplicantName']")
                ele7.click()
                ele7.send_keys('test applicant')
                ele7.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele8 = driver.find_element(By.XPATH,"//select[@name='ddlRelation']")
                ele8.click()
                ele8 = Select(ele8)
                ele8.select_by_visible_text('D/O')
                time.sleep(5)
                
                ele9 = driver.find_element(By.XPATH,"//input[@name='txtFatHusName']")
                ele9.click()
                ele9.send_keys('test relation')
                ele9.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele10 = driver.find_element(By.XPATH,"//select[@name='ddlGender']")
                ele10.click()
                ele10 = Select(ele10)
                ele10.select_by_visible_text('Female')
                time.sleep(5)
                
                ele11 = driver.find_element(By.XPATH,"//input[@name='txtMobile']")
                ele11.click()
                ele11.send_keys('7386415182')
                ele11.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele12= driver.find_element(By.XPATH,"//select[@name='ddlDelivery']")
                ele12.click()
                ele12 = Select(ele12)
                ele12.select_by_visible_text('Manual')
                time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele13 = driver.find_element(By.XPATH,"//select[@name='ddlPerDistrict']")
                ele13.click()
                ele13 = Select(ele13)
                ele13.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele14 = driver.find_element(By.XPATH,"//select[@name='ddlPerMandal']")
                ele14.click()
                ele14 = Select(ele14)
                ele14.select_by_visible_text('ADILABAD (URBAN)')
                time.sleep(5)
                
                ele15 = driver.find_element(By.XPATH,"//select[@name='ddlPerVillage']")
                ele15.click()
                ele15 = Select(ele15)
                ele15.select_by_visible_text('ADILABAD')
                time.sleep(5)
                
                ele16 = driver.find_element(By.XPATH,"//input[@name='chkSameAddress']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele16)
                ele16.click()
                time.sleep(5)
                
                ele17 = driver.find_element(By.XPATH,"//input[@name='txtPurpose']")
                ele17.click()
                ele17.send_keys('General')
                ele17.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele18 = driver.find_element(By.XPATH,"//input[@name='dgLandDetails$ctl02$chkSelect']")
                ele18.click()
                
                ele19 = driver.find_element(By.XPATH,"//input[@name='dgLandDetails$ctl02$txtPattadar']")
                ele19.click()
                ele19.send_keys('pattadhar')
                ele19.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele20 = driver.find_element(By.XPATH,"//input[@name='dgLandDetails$ctl02$txtSurveyNo']")
                ele20.click()
                ele20.send_keys('65845')
                ele20.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele21 = driver.find_element(By.XPATH,"//input[@name='dgLandDetails$ctl02$txtExtent']")
                ele21.click()
                ele21.send_keys('160')
                ele21.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele22 = driver.find_element(By.XPATH,"//input[@name='dgLandDetails$ctl02$txtPPBorDoc']")
                ele22.click()
                ele22.send_keys('784')
                ele22.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele23 =  driver.find_element(By.XPATH,"//input[@name='dgLandDetails$ctl02$txtIncome']")
                ele23.click()
                ele23.send_keys('10000')
                ele23.send_keys(Keys.ENTER)
                time.sleep(5)
                
                ele24 = driver.find_element(By.XPATH,"//input[@name='chkApp$0']")
                ele24.click()
                time.sleep(5)
                ele25 = driver.find_element(By.XPATH,"//input[@name='fileApp']")
                ele25.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele26 = driver.find_element(By.XPATH,"//input[@name='chkRation$0']")
                ele26.click()
                time.sleep(5)
                ele27= driver.find_element(By.XPATH,"//input[@name='fileRation']")
                ele27.send_keys('C:/Users/USER/Desktop/102132044.pdf')
                time.sleep(5)
                
                ele28= driver.find_element(By.XPATH,"//input[@name='btnShowPayment']")
                driver.execute_script('arguments[0].scrollIntoView(true);',ele28)
                ele28.click()
                time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele29 = driver.find_element(By.XPATH,"//input[@name='btnConfirmPayment']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele29)
                ele29.click()
                time.sleep(5)
                
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                
                ele30 = driver.find_element(By.XPATH,"//span[normalize-space()='CASH']")
                ele30.click()
                time.sleep(5)
                
                ele31 = driver.find_element(By.XPATH,"//input[@id='paymentsubmit']")
                driver.execute_script("arguments[0].scrollIntoView(true);",ele31)
                ele31.click()
                time.sleep(5)
                time.sleep(15)
                
                break 
        
                driver.close()
                time.sleep(5)

income = agricultuireincome()
income.agincomecert()