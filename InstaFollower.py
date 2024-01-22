from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.follower_count = 0

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/cristiano/")
        time.sleep(5)
        follower_count = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div['
                                                            '2]/section/main/div/header/section/ul/li[2]/button/span')
        count_result = follower_count.get_attribute("title")
        count_list = [i for i in count_result if i != ","]
        final_count = int("".join(count_list))
        self.follower_count += final_count
        time.sleep(3)

        login_click = self.driver.find_element(By.XPATH, value='//a[text()="Log in"]')
        login_click.click()
        time.sleep(4)
        login_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_field.send_keys(username)
        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(password)
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, '// *[ @ id = "loginForm"] / div / div[3] / button / div')

        time.sleep(3)
        login_button.click()

        time.sleep(6)
        not_now_button = self.driver.find_element(By.XPATH, value='//div[text()="Not now"]')
        not_now_button.click()

    # #     time.sleep(2)
    # #     not_now_button_2 = self.driver.find_element(By.XPATH, value='//button[text()="Not Now"]')
    # #     not_now_button_2.click()
    # #     time.sleep(4)
    # #
    def find_followers(self):
        followers_button = self.driver.find_element(By.XPATH, '//a[contains(@href,"followers")]')
        followers_button.click()
        time.sleep(3)

        time.sleep(4)

        followers_frame = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div['
                                                   '2]/div/div/div[2]')
        time.sleep(3)

        for i in range(3):
            # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_frame)
            # time.sleep(random.randint(500, 1000) / 1000)

            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       followers_frame)
            time.sleep(2)

        #
        # def follow(self):
        #     pass
