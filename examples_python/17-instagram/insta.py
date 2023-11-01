from instaUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By    #find element methodu için eklenen kütüphane
from selenium.webdriver.common.keys import Keys      #entera bas gibi emir verir
import time
driver_path="C:\\Users\\rfrkn\\Desktop\\visual Studio\\16-Selenium\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])              #ayarlar ve driver yolu


class Instagram:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome(options=options,executable_path=driver_path)
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(3)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(2)
        
    def getFollowers(self):
        time.sleep(3)
        
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(10)
        self.browser.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(10)
        
        
        



instagm=Instagram(username,password)
instagm.signIn()
instagm.getFollowers()

