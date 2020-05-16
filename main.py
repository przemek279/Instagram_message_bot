from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import secret

class InstaBot:
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0")
        self.driver = webdriver.Firefox(profile)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(1)
        fb_login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button')
        fb_login_btn.click()
        sleep(1)

        fb_nick_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_nick_input.send_keys(secret.fb_nick)
        fb_pass_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_pass_input.send_keys(secret.fb_pass)
        fb_log_in_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_log_in_btn.click()
        sleep(6)
        
        ntf_popup = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        ntf_popup.click()
        sleep(1)
    
    def choose_user(self, insta_user):
        self.driver.get('https://instagram.com/{}'.format(insta_user))
        sleep(5)

    def start_following(self):
        try:
            flw_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
            flw_btn.click()
        except:
            print("Allready following!")

    def send_msg(self, msg):
        self.start_following()
        sleep(5)
        msg_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button')
        msg_btn.click()
        sleep(5)
        msg_to_input = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        msg_to_input.send_keys(msg)
        msg_to_input.send_keys(Keys.RETURN)
        sleep(1)

    def __del__(self):
        self.driver.close()


if __name__ == '__main__':
    x = InstaBot()
    x.login()
    x.choose_user('message_to_user_name')
    x.send_msg('Your text message content')