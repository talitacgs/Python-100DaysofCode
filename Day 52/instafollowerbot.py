from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)

        email = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label')
        email.send_keys(username)
        psw = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label')
        psw.send_keys(password)

        log_in = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
        log_in.click()

        time.sleep(5)


    def find_followers(self,account):

        search = self.driver.find_element(By.CLASS_NAME, '_aauy')
        search.send_keys(account)

        time.sleep(3)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        search.send_keys(Keys.ENTER)

        time.sleep(6)
        followers = self.driver.find_element(By.CLASS_NAME, '_aacx')
        followers.click()





    def follow(self):
        pass