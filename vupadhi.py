# from selenium import webdriver
# import time

# driver = webdriver.Edge()
# driver.maximize_window()
# driver.get("http://www.bing.com")

# time.sleep(3)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Edge()

# driver.get('https://bing.com')

# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()

# time.sleep(10)
# driver.quit()


# from selenium import webdriver
# import time

# driver = webdriver.Edge()
# driver.get("https://www.python.org")
# print(driver.title)
# time.sleep(5)
# driver.close()

# from selenium import webdriver  
# import time  
# from selenium.webdriver.common.keys import Keys 
# from selenium.webdriver.common.by import By 
# print("sample test case started")  
# driver = webdriver.Edge()  
# driver=webdriver.firefox()  
# driver=webdriver.ie()  
# maximize the window size  
# driver.maximize_window()  
# navigate to the url  
# driver.get("https://www.google.com/")  
# identify the Google search text box and enter the value  
# element = driver.find_element_by_id("input")
# element.send_keys("javatpoint")  
# time.sleep(5)  
# click on the Google search button  
# ele = driver.find_element_by_id("addShortcutIcon")
# ele.send_keys(Keys.ENTER)  
# time.sleep(5)  
# close the browser  
# driver.close()  
# print("sample test case successfully completed")  

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Edge()
# driver.get("https://google.com")
# driver.maximize_window()
# time.sleep(5)
# searchElement = driver.find_element("id","APjFqb")
# searchElement.send_keys("BTS")
# time.sleep(5)
# ele = driver.find_element("id", "APjFqb")
# ele.send_keys(Keys.ENTER)  
# time.sleep(5) 
# searchElement.submit()
# searchElement.click()
# print(searchElement)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Edge()
# driver.get("https://google.com")
# driver.maximize_window()
# element = driver.find_element("name","q")
# element.send_keys("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# time.sleep(5)
# element.send_keys(Keys.ENTER)

# element = driver.find_element("name","alert")
# first_link = element.find_element("partial_linktext","Practice handling Alerts in selenium webdriver - CherCherTech")
# first_link = element.find_element("xpath", "//*[@id='rso']")
# first_link = driver.find_element(By.XPATH, "//a[@href='/docs/configuration']")
# first_link.click()
# time.sleep(5)
# driver.switch_to.alert.accept()
# driver.back()
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm")
# wait = WebDriverWait(driver, 10)
# ele1 = wait.until(EC.presence_of_element_located((By.NAME, "staffCode"))).click()
ele1 = driver.find_element(By.NAME,("staffCode"))
ele1.click()
ele1 = driver.find_element(By.NAME,("staffCode"))
ele1.clear()
ele1.send_keys("CRAMESH")
# ele1.send_keys(Keys.ENTER)
ele2 = driver.find_element("id", "password")
# alert = driver.switch_to.alert
# alert.accept()
ele2.click()
ele2 = driver.find_element("id", "password")
ele2.clear()
ele2.send_keys("123321")
ele2.send_keys(Keys.ENTER)
time.sleep(5)
# ele3 = driver.find_element(By.XPATH,"//*[@id='contentBox']")
# ele3 = driver.find_element(By.LINK_TEXT,'Login')
# ele3 = driver.find_element(By.CLASS_NAME, "button.btn.btn-primary.btn-block")
# ele3 = driver.find_element(By.CLASS_NAME,'col-md-12').submit()
# wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
# ele3 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'col-md-12')))



# ele3.click()
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(5)
# ele4 = driver.find_element(By.XPATH,("//span[normalize-space()='Signout']")).click()
time.sleep(15)
driver.close()




# ele2 = driver.find_element("id", "userfront-input-password")
# ele3 = driver.find_element(By.XPATH,"//*[@id='contentBox']").submit()
# ele3 = driver.find_element(By.CLASS_NAME,"btn btn-primary btn-block").click()
# ele3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div[1]/div[3]/div/div[2]/div/div[2]/div[5]/div[1]/button").click()
# ele3 = driver.find_element("By.LINK_TEXT","Login").click()
# ele3 = driver.find_element("css_selector", "#prompt-textarea").click()
# ele3 = driver.find_element("id", "userfront-button-submit")
# ele3 = driver.find_element(By.XPATH ,"//*[@id='contentBox").click()
# ele3 = driver.find_element(By.CSS_SELECTOR, "#contentBox > div.container-fluid > div > div.col-md-4 > div > div.login-box-body > div.row.mtb20 > div.col-md-12 > button").click()
# ele3 = driver.find_element(By.CLASS_NAME,"login-box-body").click()
# ele3 = driver.find_element(By.TAG_NAME,"button").click()
# ele3 = driver.find_element(By.CLASS_NAME,"col-md-12").click()
# ele3.send_keys(Keys.ENTER)
# time.sleep(10)
# driver.close()
# contentBox > div.container-fluid > div > div.col-md-4 > div > div.login-box-body > div.row.mtb20 > div.col-md-12 > button





# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
# import time

# driver = webdriver.Chrome()
# driver.get("https://tsstaging.meeseva.telangana.gov.in/meesevastaging/login.htm")
# time.sleep(3)
# ele1 = driver.find_element("name","staffCode")
# ele1.send_keys("TSGOPR0002")
# ele1.send_keys(Keys.ENTER)
# time.sleep(3)
# ele2 = driver.find_element("id", "password")
# ele2.send_keys("123321")
# ele2.send_keys(Keys.ENTER)
# time.sleep(3)
# ele = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/form/div[1]/div[3]/div/div[2]/div/div[2]/div[5]/div[1]/button').click()
# time.sleep(3)
# alert = driver.switch_to.alert
# alert.accept()
# driver.close()