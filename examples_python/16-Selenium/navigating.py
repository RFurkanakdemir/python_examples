from selenium import webdriver
from selenium.webdriver.common.by import By    #find element methodu için eklenen kütüphane
from selenium.webdriver.common.keys import Keys      #entera bas gibi emir verir
import time

driver_path="C:\\Users\\rfrkn\\Desktop\\visual Studio\\16-Selenium\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])              #ayarlar ve driver yolu
driver = webdriver.Chrome(options=options,executable_path=driver_path)

url="http://github.com"
driver.get(url)

searchInput=driver.find_element(By.NAME, "q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result=driver.page_source   #sayfa kaynak kodunu almak için kulllanılırız
# print(result)

result=driver.find_elements(By.CLASS_NAME,'v-align-middle') 
for element in result:
    print(element.text)    #hex veri text e çevirilir

time.sleep(2)
driver.close()