import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



SIMILAR_ACCOUNT = "youtube"
USERNAME = "username"
PASSWORD = "passwprd"
#no copy

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username= self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        time.sleep(1)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        search = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)#first result
        seach_especifict = self.driver.find_element(By.CLASS_NAME, "fuqBx").find_elements(By.TAG_NAME, "div")[0]
        seach_especifict.click()
        time.sleep(3)


    def find_followers(self):
        time.sleep(2)
        title = self.driver.title
        title_enterprice = title.split(" ")[0].lower()
        self.driver.get(f"https://www.instagram.com/{title_enterprice}/followers/")
        time.sleep(4)
        followers = self.driver.find_elements(By.CSS_SELECTOR, "._aaey ._aae- li")
        time.sleep(1)
        self.follow(followers)



    def follow(self, followers):
        for follow_person in followers:
            follow= follow_person.find_element(By.CSS_SELECTOR, "._aaes button")
            follow.click()
            time.sleep(5)

if __name__ =="__main__":
    bot = InstaFollower(Service(ChromeDriverManager().install()))
    bot.login()
    bot.find_followers()
