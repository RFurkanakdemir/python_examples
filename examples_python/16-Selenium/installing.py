from selenium import webdriver
import time

driver=webdriver.Chrome()

url="http://sadikturan.com"

driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("xxxx")

print(driver.title)


time.sleep(2)
driver.close()
