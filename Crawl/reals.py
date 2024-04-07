
#* Reals Analyzing System Programing

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

class InstagramLogin:
    def __init__(self, Driver, Uid, Password) -> str:
        self.login = Driver
        self.Uid = Uid
        self.Password = Password
        self.instargram_url = "https://www.instagram.com/"
    
    def form_old(self):
        self.login.get(self.instargram_url)
        time.sleep(3)
        Login = self.login.find_elements(By.TAG_NAME, "button")
        Login[1].click()
        time.sleep(5)
        login_area = self.login.find_elements(By.TAG_NAME, "input")
        login_area[0].send_keys(self.Uid)
        login_area[1].send_keys(self.Password)
        time.sleep(2)
        Login = self.login.find_elements(By.TAG_NAME, "button")
        Login[2].click()
        time.sleep(10)
        self.login.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div").click()
        self.login.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div/div/div[3]/button[2]").click()
    
    def form_new(self):
        self.login.get(self.instargram_url)
        login_area = self.login.find_elements(By.TAG_NAME, "input")
        login_area[0].send_keys(self.Uid)
        login_area[1].send_keys(self.Password)
        time.sleep(2)
        self.login.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button").click()
        time.sleep(5)
        self.login.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
        self.login.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()

    def Login(self):
        hashtag = "#릴스"
        actions = ActionChains(self.login)                                          
        self.login.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/span/div/a/div/div/div/div").click()
        self.login.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input").send_keys(hashtag)        
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(3)
        # self.login.delete_all_cookies()
        self.login.refresh()
        time.sleep(2)
        # while True:
        # self.login.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/span[2]").click()
        # Title = self.login.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/span[1]").text
        # print(Title)
        # actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1000)

def process():
    try:
        from Driver import WebdriverManager
        Driver = WebdriverManager(display=True, user_oper=True)
        Driver.display_option()
        Driver.user_oper_option()
        Driver = Driver.Webdriver()
        Login = InstagramLogin(Driver, Uid="____eunseok", Password="7788Lucas08130128")
        Login.form_new()
        Login.Login()
        Driver.quit()
    except:
        Login.form_old()
        Login.Login()
        Driver.quit()

if __name__ == "__main__":
    process()


# //*[@id="mount_0_0_wO"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div
# //*[@id="mount_0_0_+e"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div
# //*[@id="mount_0_0_4I"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/span/div/a
# //*[@id="mount_0_0_0a"]
# //*[@id="mount_0_0_vG"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/span[2]
# //*[@id="mount_0_0_s4"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[3]/span/div/a/div/div[1]/div/div
# //*[@id="mount_0_0_Iz"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/span/div/a/div/div/div/div
# //*[@id="mount_0_0_cp"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input
# //*[@id="mount_0_0_M6"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div
# /html/body/div[6]/div[1]/div/div/div/div[3]/button[2]