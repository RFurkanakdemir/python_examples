from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By    #find element methodu için eklenen kütüphane
from selenium.webdriver.common.keys import Keys      #entera bas gibi emir verir
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])              #ayarlar ve driver yolu

class Twitter:
    def __init__(self,username,password):
        driver_path="C:\\Users\\rfrkn\\Desktop\\visual_studio\python\\16-Selenium\\chromedriver.exe"    #ayarlar
        browserProfile = webdriver.ChromeOptions()
        options=browserProfile.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromeopt=browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser=webdriver.Chrome(options=options,executable_path=driver_path,chrome_options=chromeopt)
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get('https://twitter.com/i/flow/login')
        time.sleep(10)

        usernameInput=self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(3)                    
        passwordInput=self.browser.find_element(By.NAME,'password')
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

    def search(self,hashtag):
        searchInput=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(7)
        results=[]

        # zaman_Akisi=self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div")
        # elements=zaman_Akisi.find_elements(By.XPATH,'div>div>div>div>article>div>div>div>div[1]>div[1]>div')
        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            for i in self.browser.find_elements(By.XPATH,"//div[@data-testid='tweetText']"):
                results.append(i.text)
            
            if loopCounter > 2:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(3)

            
            
            self.browser.implicitly_wait(5)

            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1
        
            
        
        count = 1
        
        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n***********\n")
                count+=1
        
    
           
            
            
    # def search(self, hashtag):
    #     searchInput = self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
    #     searchInput.send_keys(hashtag)
    #     time.sleep(3)
    #     searchInput.send_keys(Keys.ENTER)
    #     time.sleep(3)

    #     results = []

    #     self.browser.implicitly_wait(5)
        
    #     for i in self.browser.find_elements(By.XPATH,"//div[@data-testid='tweet']/div[2]/div[2]"):
    #         results.append(i.text)
    #         self.like(i)
        
    #     time.sleep(3)

    #     loopCounter = 0
    #     last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
    #     while True:
    #         if loopCounter > 5:
    #             break
    #         self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    #         time.sleep(3)

    #         for i in self.browser.find_elements(By.XPATH,"//div[@data-testid='tweet']/div[2]/div[2]"):
    #             results.append(i.text)
    #             self.like(i)
            
    #         self.browser.implicitly_wait(5)

    #         new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
    #         if last_height == new_height:
    #             break
    #         last_height = new_height
    #         loopCounter+=1            

    #     count = 1
    #     with open("tweets.txt","w",encoding="UTF-8") as file:
    #         for item in results:
    #             file.write(f"{count}-{item}\n")
    #             count+=1
        



twitter=Twitter(username,password)
twitter.signIn()
# hashtag=input("giriniz")
hashtag="python"
twitter.search(hashtag)
