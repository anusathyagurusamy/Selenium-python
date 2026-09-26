import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#Launch Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# 1. IMPLICIT WAIT


driver.implicitly_wait(10)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Selenium Python")

print("Implicit Wait - Search box found successfully")

# 2. EXPLICIT WAIT


wait = WebDriverWait(driver, 10)

search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

print("Explicit Wait - Search box is visible")


search_box.clear()
search_box.send_keys("Python Selenium Automation")


# 3. TIME.SLEEP()

time.sleep(3)

print("time.sleep() - Browser paused for 3 seconds")

print("Page title:", driver.title)

# Close browser
driver.quit()



