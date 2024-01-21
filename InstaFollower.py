from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/englandcricket/")
        time.sleep(5)
        login_click = self.driver.find_element(By.XPATH,  value='//a[text()="Log In"]')
        login_click.click()
        time.sleep(4)
        login_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_field.send_keys(username)
        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(password)
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, '// *[ @ id = "loginForm"] / div / div[3] / button / div')

        time.sleep(2)
        login_button.click()

        time.sleep(3)
        not_now_button = self.driver.find_element(By.XPATH, value='//div[text()="Not now"]')
        not_now_button.click()

    #     time.sleep(2)
    #     not_now_button_2 = self.driver.find_element(By.XPATH, value='//button[text()="Not Now"]')
    #     not_now_button_2.click()
    #     time.sleep(4)
    #
    # def find_followers(self):
    #     search_button = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_5+"]/div/div/div[2]/div/div/div['
    #                                                        '1]/div[1]/div[1]/div/div/div/div/div[2]/div['
    #                                                        '2]/span/div/a/div')
    #     print("found element")
    #     search_button.click()
    #
    # def follow(self):
    #     pass
