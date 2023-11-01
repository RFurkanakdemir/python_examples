from Userinfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Github:
    def __init__(self,username,password):
        driver_path="C:\\Users\\rfrkn\\Desktop\\visual Studio\\16-Selenium\\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])   
        self.browser=webdriver.Chrome(options=options,executable_path=driver_path)
        self.username=username
        self.password=password
        self.followers=[]

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)

        username=self.browser.find_element(By.XPATH,'//*[@id="login_field"]').send_keys(self.username)
        password=self.browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[12]').click()

    def loadFollowers(self):
        items=self.browser.find_elements(By.XPATH,'//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div')
        for i in items:
            self.followers.append(i.find_element(By.XPATH,'//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/a/span[2]').text)
    
    def getFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(5)
        self.loadFollowers()
            
        while len(self.followers)>50:
            links=self.browser.find_element(By.CLASS_NAME,"BtnGroup").find_elements(By.TAG_NAME,"a")
            if len(links)==1:
                if links[0].text=="Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()

                else:
                    break
            else:
                for link in links:
                    if link.text=="Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                        
                    else:
                        continue





github=Github(username,password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)
