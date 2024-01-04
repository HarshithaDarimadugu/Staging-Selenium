from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import time

# obj = Service('https://testautomationpractice.blogspot.com/')
# driver = webdriver.Chrome(service = obj)
driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
parent_handle = driver.current_window_handle
driver.maximize_window()
time.sleep(5)

####################### entering the input in the fields
# ele1 = driver.find_element(By.XPATH,"//input[@id='name']")
# ele1.click()
# ele1.send_keys('Harshitha Darimadugu')
# ele1.send_keys(Keys.ENTER)

# ele2 = driver.find_element(By.XPATH,"//input[@id='email']")
# ele2.click()
# ele2.send_keys('harshi4@gmail.com')
# ele2.submit

# ele3 = driver.find_element(By.XPATH,"//input[@id='phone']")
# ele3.click()
# ele3.send_keys('789748646')
# ele3.submit

# ele4 = driver.find_element(By.XPATH,"//textarea[@id='textarea']")
# ele4.click()
# ele4.send_keys('XYTGYGDJYAGJ')
# ele4.submit

############# clicking the radio button
# ele5 = driver.find_element(By.XPATH,"//label[@for='female']")
# ele5.click()

###############selecting all the checkboxes 
# ele6 =driver.find_elements(By.XPATH,"// label[contains(text(), 'day')]")
# for ele in ele6:
    # ele.click()
    
############# selecting only particular checkboxes by choice
# ele7 =driver.find_elements(By.XPATH,"//input[@type= 'checkbox']")
# driver.execute_script('arguments[0].scrollIntoView(true);', ele7)
# for ele in ele7:
    # var = ele.get_attribute('value')
    # if var == "monday" or var == "saturday":
        # ele.click()
        
##########selecting checkboxes by range
# ele6 =driver.find_elements(By.XPATH,"// label[contains(text(), 'day')]")
# for ele in range((len(ele6)-4),(len(ele6)-1)):
    # ele6[ele].click()

############# selecting checkboxes at first 2 and last 2
# ele6 =driver.find_elements(By.XPATH,"// label[contains(text(), 'day')]")
# for i in range(len(ele6)):
    # if i < 2 or i >4:
        # ele6[i].click()
        
# for i in range(len(ele6)):
    # if i > 4:
        # ele6[i].click()

########## unchecking al checkboxes
# ele6 =driver.find_elements(By.XPATH,"// label[contains(text(), 'day')]")
# for ele in ele6:
    # ele.click() ######## checking
    # ele.click()

##########selecting the dropdown option
# ele7 = driver.find_element(By.XPATH, "//select[@id='country']")
# ele7.click()
# ele7 = Select(ele7)
# ele7.select_by_visible_text('Australia')
# time.sleep(5)

# ele8 = driver.find_element(By.XPATH,"//option[@value='yellow']")
# ele8.click()

# ele7 = driver.find_element(By.XPATH, "//select[@id='country']")
# ele7.click()
# ele7 = Select(ele7)
# ele7.select_by_value("uk")

# ele7 = driver.find_element(By.XPATH, "//select[@id='country']")
# ele7.click()
# clk = Select(ele7)
# clk.select_by_index(9)

###################selecting the alerts
# ele9 = driver.find_element(By.XPATH,"//button[text()='Alert']")
# ele9.click()
# alert_window = driver.switch_to.alert
# alert_window.accept()


# ele9 = driver.find_element(By.XPATH,"//button[text() = 'Confirm Box']")
# ele9.click()
# alert_window = driver.switch_to.alert
# time.sleep(5)
# alert_window.accept()
# time.sleep(10)

# ele9 = driver.find_element(By.XPATH,"//button[text() = 'Confirm Box']")
# ele9.click()
# alert_window = driver.switch_to.alert
# time.sleep(5)
# alert_window.dismiss()
# time.sleep(10)

############alert has input, reading the text, ok and cancel button
# ele9 = driver.find_element(By.XPATH,"//button[text() = 'Prompt']")
# ele9.click()
# alert_window = driver.switch_to.alert
# time.sleep(5)
############# driver.execute_script("arguments[0].value = '';", alert_window)
# print('alert box text is: ',alert_window.text) ### reading the text
# alert_window.send_keys('Hi i am Krishna') ### entering the input
# alert_window.accept() ### accepting the alert
# time.sleep(10)

# ele9 = driver.find_element(By.XPATH,"//button[text() = 'Prompt']")
# ele9.click()
# alert_window = driver.switch_to.alert
# time.sleep(5)
# print('alert box text is: ',alert_window.text) ### reading the text
# alert_window.send_keys('Hi hello i am Janu') ### entering the input
# alert_window.dismiss() ### cancel the alert
# time.sleep(10)


###########wait commands --- implicit, explicit
# ele10 =  driver.find_element(By.XPATH,"//button[text() = 'New Browser Window']")
# ele10.click()
# all_handles = driver.window_handles
# for handle in all_handles:
    # if handle != parent_handle:
        # driver.switch_to.window(handle)
        # driver.implicitly_wait(10)
        # ele11 =driver.find_element(By.XPATH,"//a[normalize-space()='MP3 Players']")
        # ele11.click()
        # ele12 = driver.find_element(By.XPATH,"//*[text()='test 22 (0)']")
        # ele12.click()
        # ele13 = driver.find_element(By.XPATH,"//*[text()='Cameras (2)']")
        # ele13.click()
        # time.sleep(5)
        
############## explicit wait
ele10 =  driver.find_element(By.XPATH,"//button[text() = 'New Browser Window']")
ele10.click()
all_handles = driver.window_handles
for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        wait = WebDriverWait(driver, 10, poll_frequency = 2, ignored_exceptions =[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        ele11 =driver.find_element(By.XPATH,"//a[normalize-space()='MP3 Players']")
        ele11.click()
        ele12 = driver.find_element(By.XPATH,"//*[text()='test 22 (0)']")
        ele12.click()
        mywait = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Cameras (2)']")))
        # ele13 = driver.find_element(By.XPATH,"//*[text()='Cameras (2)']")
        mywait.click()
        time.sleep(5)        
        
        
        
        

driver.quit()
