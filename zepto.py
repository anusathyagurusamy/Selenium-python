from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.zepto.com/")

driver.maximize_window()

time.sleep(10)

print(driver.title)
print(driver.current_url)
sweet = driver.find_element(By.XPATH, "//img[@alt='Sweet Cravings']")

sweet.click()
time.sleep(3)
product = driver.find_element(By.XPATH,"//img[@alt='Kinder Joy Blue | Chocolate | Assorted']")
product.click()
time.sleep(3)

add_cart = driver.find_element(By.XPATH,"(//button[text()='Add to Cart'])[2]")
add_cart.click()
time.sleep(3)

cart=driver.find_element(By.XPATH,"/html/body/div[4]/div/div/header/div/div[4]/div/div[1]/button")
cart.click()
time.sleep(3)

checkout=driver.find_element(By.XPATH,"//button[text()='Login to Proceed']")
checkout.click()
time.sleep(3)