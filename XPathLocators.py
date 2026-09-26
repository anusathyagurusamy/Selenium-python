import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)

search=driver.find_element(By.ID,'name')
search.send_keys('Anusathya G')
time.sleep(3)

search=driver.find_element(By.XPATH,"//input[@id='email']")
search.send_keys('anusathyagurusamy@gmail.com')
time.sleep(3)

search=driver.find_element(By.XPATH,'//input[@maxlength="10"]')
search.send_keys('4330489202')
time.sleep(3)

search=driver.find_element(By.XPATH,"//textarea[@id='textarea']")
search.send_keys('Madurai, India')
time.sleep(3)


gender=driver.find_element(By.XPATH,"//input[@value='female']")
gender.click()
time.sleep(3)

search=driver.find_element(By.XPATH,'//input[@value="sunday"]')
search.click()
time.sleep(3)

search=driver.find_element(By.CSS_SELECTOR,"#datepicker")
search.send_keys('05/23/2005')
time.sleep(3)


