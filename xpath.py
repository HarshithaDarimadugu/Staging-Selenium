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

# service = Service(r"C:\Py\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_obj)

# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=chrome_options)

# https://demo.nopcommerce.com/register?returnUrl=%2Flogin --- another link of practing the automation
# driver = webdriver.Chrome()
# driver.get('https://demo.nopcommerce.com/register?returnUrl=%2Flogin')
# https://seleniumbase.io/demo_page
# driver.get('https://seleniumbase.io/demo_page')
# driver.maximize_window()
# time.sleep(5)

# tit = driver.title
# print(tit)
# print(driver.current_url)
# print(driver.page_source)

# ele= driver.find_element(By.XPATH,"//input[@name='fname']")

# print(ele.is_displayed())
# time.sleep(5)

# print(ele.is_enabled())
# time.sleep(5)

# button = driver.find_element(By.XPATH,"//input[@value='female']")
# print('before selecting the button....')
# print(button.is_selected())

# button.click()
# print('after selecting the button...')
# time.sleep(5)
# print(button.is_selected())

# time.sleep(5)

# driver.get('https://www.facebook.com/')
# driver.get('https://www.amazon.in/')
# time.sleep(5)

# driver.back()
# time.sleep(5)
# driver.forward()
# time.sleep(5)
# driver.refresh()
# driver.close()   

########### find_element -- returning only single web element
###################locator matching with single web element
# ele = driver.find_element(By.XPATH,"//input[@name='FirstName']")
# ele.send_keys('Harshitha')
# time.sleep(5)

###################### locator matching with multiple web elements
# ele = driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(len(ele))
# print(ele.text)
# time.sleep(5)

#######################locator matching with no element
# ele = driver.find_element(By.XPATH,"//strong[normalize-space()='News']")
# print(ele.text)

#########find_elements --- returns the multiple web elements
#############################locator matching with single web element

# elements = driver.find_elements(By.XPATH,"//input[@name='FirstName']")
# elements.send_keys('anjali')
# print(len(elements))
# time.sleep(5)
# elements[0].send_keys('anjali')
# time.sleep(5)

###############locator matching with multiple web elements
# elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))
# time.sleep(3)
# print(elements[21].text)
# time.sleep(5)

#################locator matching with no element
# elements = driver.find_elements(By.XPATH,"//*[@id='small-search']")
# print(len(elements))
# time.sleep(5)

######### clear(), text, get_attribute()

# ele = driver.find_element(By.XPATH,"//input[@id='myTextInput2']")
# ele.clear()
# ele.send_keys('testing')
# time.sleep(5)

# ele = driver.find_element(By.XPATH,"//button[@id='myButton']")
# print('text is:',ele.text)
# print('get attribute is:',ele.get_attribute('type'))


############ implicit wait

# driver = webdriver.Chrome()
# driver.get('https://www.nopcommerce.com/en')
# driver.implicitly_wait(10)
# driver.maximize_window()
# time.sleep(5)
# ele1 = driver.find_element(By.XPATH,"//span[@class='user-actions-ico']//*[name()='svg']")
# ele1.click()
# time.sleep(5)
# ele2 = driver.find_element(By.XPATH,"//span[normalize-space()='Log in']")
# ele2.click()
# time.sleep(5)
# ele3=driver.find_element(By.XPATH,"//*[@id='challenge-stage']/div/label/input")
# ele3.click()
# time.sleep(5)

# driver = webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.implicitly_wait(10)

# ele1 = driver.find_element(By.XPATH,"//*[@id='name']")
# ele1.click()
# ele1.send_keys('Harshitha')
# time.sleep(5)

#########################explicitly wait

# driver = webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
# mywait = WebDriverWait(driver,10) ######## base equation
# mywait = WebDriverWait(driver, 10, poll_frequency = 2, ignored_exceptions = [NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException])
######### advanced equation

# obj = mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='name']")))
# ele1 = driver.find_element(By.XPATH,"//*[@id='name']")
# obj.click()
# obj.send_keys('Harshitha')
# time.sleep(5)




####### checking the check boxes
# ele1 = driver.find_element(By.ID,'sunday')
# driver.execute_script('arguments[0].scrollIntoView(true);',ele1)
# ele1.click()
# time.sleep(5)


############ selecting all checkboxes 
# ele1 = driver.find_elements(By.XPATH,"//*[contains(@id, 'day')]")
# print(len(ele1))
# for i in range(len(ele1)):
    # ele1[i].click()
# time.sleep(15)

###### selectting particular checkboxes using the condition
# ele1 = driver.find_elements(By.XPATH,"//*[contains(@id,'day')]")
# print(len(ele1))
# for ele in ele1:
    # if len(ele1)<2:
        # print(len(i))
        # ele1[i].click()
# time.sleep(10)
 
driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(5)

ele=driver.find_element(By.XPATH,"//input[@id='male']")
print("text is:",ele.text)
print("get_attribute value is:", ele.get_attribute('value'))
time.sleep(2)

ele2 =driver.find_elements(By.XPATH,"//*[contains(@id,'day')]")
print(len(ele2))
for i in range(len(ele2)):
    ele2[0].text
time.sleep(5)



















driver.quit()