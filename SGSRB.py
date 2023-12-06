from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time


driver=webdriver.Chrome()
browser = driver.get('https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm')
driver.maximize_window()
time.sleep(5)

driver.refresh()
ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
ele1.click()
ele1 = driver.find_element(By.XPATH,"//input[@name='staffCode']")
ele1.clear()
ele1.send_keys('TSGOPR0001')
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
ele1.send_keys('TSGOPR0001')
ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
ele2.click()
ele2 = driver.find_element(By.XPATH,"//input[@name='password']")
ele2.clear()
ele2.send_keys('123321')
ele2.send_keys(Keys.ENTER)
time.sleep(5)

alert = driver.find_element(By.XPATH,"//a[@class='close']")
alert.click()
time.sleep(3)
ele3 = driver.find_element(By.XPATH,"//input[@name='autocomplete']")
ele3.click()
ele3 = driver.find_element(By.XPATH,"//input[@name='autocomplete']")
ele3.send_keys('room')
time.sleep(3)

parent_handle = driver.current_window_handle
print(parent_handle)

# ele4 =driver.find_element(By.XPATH,"//div[@class='front s_front']//h1[@class='f_headline'][normalize-space()='SRI GNANA SARASWATI DEVASTHANAM ROOM BOOKING BASAR']")
ele4 = driver.find_element(By.XPATH,"//h1[contains(text(),'SRI LAKSHMI NARASIMHA SWAMY VARI DEVASTHANAM ROOM ')]")
ele4.click()
time.sleep(5)

all_handles = driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        ele5 = driver.find_element(By.XPATH,"//select[@name='ddlRoomType']")
        ele5.click()
        ele5 = Select(ele5)
        ele5.select_by_visible_text('ALL')
        time.sleep(5)
        
        ele6= driver.find_element(By.XPATH,"//input[@name='txtBookingDate']")
        ele6.click()
        time.sleep(3)
        ele7 = driver.find_element(By.XPATH,"//img[@src='../../../Images/Calendar/cal.gif']")
        ele7.click()
        time.sleep(5)
        ele8 = driver.find_element(By.XPATH,"//a[@title='December 29']")
        ele8.click()
        time.sleep(5)
        
        ele9 = driver.find_element(By.XPATH,"//select[@name='ddlDays']")
        ele9.click()
        ele9 = Select(ele9)
        ele9.select_by_visible_text('1')
        time.sleep(5)
        
        ele10 = driver.find_element(By.XPATH,"//input[@name='btnGetRoom']")
        ele10.click()
        time.sleep(10)
        
        ele11 = driver.find_element(By.XPATH,"//a[@id='dgRoomDetails_lnkAvailable_0']")
        ele11.click()
        time.sleep(5)
        
        ele12 = driver.find_element(By.XPATH,"//a[@id='grdDatesavailable_lnkBook1_0']")
        driver.execute_script('arguments[0].scrollIntoView(true);',ele12)
        ele12.click()
        time.sleep(5)
        
        ele13 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtDevotName']")
        driver.execute_script('arguments[0].scrollIntoView(true);',ele13)
        ele13.click()
        ele13.send_keys('KRISHNA')
        ele13.send_keys(Keys.ENTER)
        time.sleep(5)
        
        ele14 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlProofDocument']")
        ele14.click()
        ele14 = Select(ele14)
        ele14.select_by_visible_text('ANY GOVT ID')
        time.sleep(5)
        
        ele15 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtProofName']")
        driver.execute_script('arguments[0].scrollIntoView(true);',ele15)
        ele15.click()
        ele15.send_keys('proof name')
        ele15.send_keys(Keys.ENTER)
        time.sleep(5)
        
        ele16 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtProofNo']")
        ele16.click()
        ele16.send_keys('86454')
        ele16.send_keys(Keys.ENTER)
        time.sleep(5)
        
        ele17 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlGender']")
        ele17.click()
        ele17 = Select(ele17)
        ele17.select_by_visible_text('Female')
        time.sleep(5)
        
        ele18 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtMobile']")
        ele18.click()
        ele18 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtMobile']")
        ele18.clear()
        ele18.send_keys('7386415182')
        ele18.send_keys(Keys.ENTER)
        time.sleep(5)
        
        # ele25 = driver.find_element(By.XPATH,"//input[@name='chkIdentity']")
        # ele25.click()
        # time.sleep(3)
        # ele25 = driver.find_element(By.XPATH,"//input[@name='fupIDProof']")
        # ele25.send_keys('C:/Users/USER/Desktop/102132044.pdf')
        # time.sleep(5)
        
        # ele19 = driver.find_element(By.XPATH,"//input[@name='btnShowPayment']")
        # ele19.click()
        # time.sleep(10)
        
        # ele19 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtAge']")
        # ele19.click()
        # ele19 = driver.find_element(By.XPATH,"//input[@name='devoteedetails$txtAge']")
        # ele19.clear()
        # ele19.send_keys('25')
        # ele19 .send_keys(Keys.ENTER)
        # time.sleep(5)
        
        ele20 = driver.find_element(By.XPATH,"//select[name='devoteedetails$ddlDistrict']")
        # driver.execute_script('arguments[0].scrollIntoView(true);',ele20)
        ele20.click()
        ele20 = Select(ele20)
        ele20.select_by_visible_text('ADILABAD')
        time.sleep(5)
        
        # ele21 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlMandal']")
        # driver.execute_script('arguments[0].scrollIntoView(true);',ele21)
        # ele21.click()
        # ele21 = Select(ele21)
        # ele21.select_by_visible_text('ADILABAD RURAL')
        # time.sleep(5)
        
        # ele22 = driver.find_element(By.XPATH,"//select[@name='devoteedetails$ddlVillage']")
        # ele22.click()
        # ele22 = Select(ele22)
        # ele22.select_by_visible_text('ANKAPUR')
        # time.sleep(5)
        
        # ele23 = driver.find_element(By.XPATH,"//input[@name='txtAppName']")
        # ele23.click()
        # ele23 = driver.find_element(By.XPATH,"//input[@name='txtAppName']")
        # ele23.clear()
        # ele23.send_keys('test name')
        # ele23.send_keys(Keys.ENTER)
        # time.sleep(5)
        
        # ele24 = driver.find_element(By.XPATH,"//select[@name='ddlInfRelation']")
        # ele24.click()
        # ele24 = Select(ele24)
        # ele24.select_by_visible_text('Husband')
        # time.sleep(5)
        
        # ele25 = driver.find_element(By.XPATH,"//input[@name='chkApplication']")
        # ele25.click()
        # time.sleep(3)
        # ele25 = driver.find_element(By.XPATH,"//input[@name='fileApp']")
                
        # ele25.send_keys('C:/Users/USER/Desktop/102132044.pdf')
        # time.sleep(5)
        
        # ele26 = driver.find_element(By.XPATH,"//input[@name='chkProof']")
        # ele26.click()
        # time.sleep(3)
        # ele26 = driver.find_element(By.XPATH,"//input[@name='fupProof']")
        # ele26.send_keys('C:/Users/USER/Desktop/102132044.pdf')
        # time.sleep(5)
                
        
driver.close()