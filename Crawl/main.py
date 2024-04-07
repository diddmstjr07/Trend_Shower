
#* instagram Account automatic creater

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import os

class IPAnalyze:
    def __init__(self) -> None:
        import requests
        self.check_ip = "https://httpbin.org/ip"
        self.requests = requests
    
    def Outer_IP_Get(self):
        outer_ip = self.requests.get("http://ip.jsontest.com").json()['ip']
        self.IP = outer_ip
        return outer_ip

    def Check_IP(self):
        API_KEY = "cy7f9CctmoBzvYFCdHXlYNijczkjGPNg"
        url = f"https://ipqualityscore.com/api/json/ip/{API_KEY}/{self.IP}"
        score_json = self.requests.get(url).json()
        self.score_json = score_json

    def IPQS(self):
        self.Check_IP()
        score_json = self.score_json
        print("\033[1;32m" + "Fraud Score Point: " + "\033[0m" + str(score_json["fraud_score"]))
        print("\033[1;32m" + "Region: " + "\033[0m" + str(score_json["region"]))
        print("\033[1;32m" + "City: " + "\033[0m" + str(score_json["city"]))
        print("\033[1;32m" + "Poxy: " + "\033[0m" + str(score_json["proxy"]))
        print("\033[1;32m" + "VPN: " + "\033[0m" + str(score_json["vpn"]))
        print("\033[1;32m" + "TOR: " + "\033[0m" + str(score_json["tor"]))
        print("\033[1;32m" + "Active VPN: " + "\033[0m" + str(score_json["active_vpn"]))
        print("\033[1;32m" + "Active TOR: " + "\033[0m" + str(score_json["active_tor"]))

        if score_json["proxy"] == True or score_json["vpn"] == True or score_json["tor"] == True or score_json["active_vpn"] == True or score_json["active_tor"] == True:
            print("\033[1;31m" + f"\nGoogle or Meta will be also detect as IPQS System\n" + "\033[0m")
            answer = input("Ignore warning and continue run program? (y/n): ")
            if answer == 'y' or answer == 'Y':
                print("\033[1;33m" + "\nRunning..." + "\033[0m")
            elif answer == 'n' or answer == 'N':
                print("\033[1;33m" + "\nStoping..." + "\033[0m")
                os._exit(0)
        else:
            answer = input("\nMake sure check not using your Real IP Address. Are you minding set IP as your real IP? (y/n): ")
            if answer == 'y' or answer == 'Y':
                print("\033[1;33m" + "\nStoping..." + "\033[0m")
                os._exit(0)
            elif answer == 'n' or answer == 'N':
                print("\033[1;33m" + "\nRunning..." + "\033[0m")


class InstagramAccount:
    def __init__(self, name_length, pass_length) -> int:
        from names_generator import generate_name
        from Driver import WebdriverManager
        import random
        import string
        import check
        self.Driver = WebdriverManager(display=False, user_oper=True)
        self.name = name_length
        self.password = pass_length
        self.generate_name = generate_name
        self.random = random
        self.string = string
        self.Login = check
        self.mail_url = "https://www.moakt.com/ok/inbox"
        self.instagram_account = "https://www.instagram.com/accounts/signup/email/?next=https%3A%2F%2Fwww.instagram.com%2Faccounts%2F"

    def generate_random_name(self):
        letters = self.string.ascii_letters
        return ''.join(self.random.choice(letters) for i in range(self.name))

    def generate_random_password(self):
        characters = self.string.ascii_letters + self.string.digits + self.string.punctuation
        return ''.join(self.random.choice(characters) for i in range(self.password))
    
    def virtual_mail(self):
        self.Driver.display_option()
        self.Driver.user_oper_option()
        mail = self.Driver.Webdriver()
        mail.get(self.mail_url)
        time.sleep(3)
        mail.find_element(By.CSS_SELECTOR, "#mailForm > form > input.mail_butt").click()
        time.sleep(3)
        mail_address = mail.find_element(By.CSS_SELECTOR, "#email-address").text
        print("\033[1;32m" + f"Mail Cracked: " + "\033[0m" + mail_address)
        self.Driver.display_option()
        self.Driver.user_oper_option()
        instagram = self.Driver.Webdriver()
        instagram.get(self.instagram_account)
        time.sleep(5)
        try:
            instagram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[3]/div[2]/a[2]/img")
            result = self.instagram_Verify_Newest(instagram, mail_address, mail)
            if result == None:
                raise ConnectionRefusedError
        except:
            self.instagram_Verify(instagram, mail_address, mail)
    
    def instagram_Verify_Newest(self, instagram, mail_address, mail):    
        form = instagram.find_elements(By.TAG_NAME, "input")
        if len(form) == 4:
            random_name = self.generate_name(style='capital')
            random_id = self.generate_random_name()
            random_password = self.generate_random_password()
            print("\033[1;32m" + f"Cracked instagram Name: " + "\033[0m" + random_name)
            print("\033[1;32m" + f"Cracked instagram uid: " + "\033[0m" + random_id)
            print("\033[1;32m" + f"Cracked instagram Password: " + "\033[0m" + random_password)
            form[0].send_keys(mail_address)
            form[1].send_keys(random_name)
            form[2].send_keys(random_id)
            form[3].send_keys(random_password)
            id_submit = instagram.find_elements(By.TAG_NAME, "button")
            id_submit[2].click()
            time.sleep(10)
            birth = instagram.find_elements(By.TAG_NAME, "select")
            birth_obj = Select(birth[2])
            birth_obj.select_by_index("20")
            id_submit = instagram.find_elements(By.TAG_NAME, "button")
            id_submit[1].click()
            time.sleep(30)
            try:
                instagram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[1]/div[2]/span").text
                return None
            except:
                mail.refresh()
                Verified_Code = mail.find_element(By.CSS_SELECTOR, '#email_message_list > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text[0:6]
                time.sleep(1)
                print("\033[1;32m" + f"Cracked instagram Verified Code: {Verified_Code}" + "\033[0m")
                time.sleep(10)
                submit = instagram.find_elements(By.TAG_NAME, "button")
                print(len(submit))
                submit[1].click()
                instagram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/div/button").click()
                birth = instagram.find_elements(By.TAG_NAME, "select")
                birth_obj = Select(birth[0])
                birth_obj.select_by_index("10")
                time.sleep(10)
    
    def instagram_Verify(self, instagram, mail_address, mail):
        email = instagram.find_element(By.XPATH, "//*[contains(@id, 'f')]")
        email.send_keys(mail_address)
        time.sleep(3)
        instagram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div[3]/button").click()
        time.sleep(3)
        time.sleep(30)
        mail.refresh()
        Verified_Code = mail.find_element(By.CSS_SELECTOR, '#email_message_list > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text[0:6]
        time.sleep(1)
        print("\033[1;32m" + f"Cracked instagram Verified Code: " + "\033[0m" + Verified_Code)
        time.sleep(10)
        instagram.find_element(By.XPATH, "//*[contains(@id, 'f')]").send_keys(Verified_Code)
        time.sleep(10)
        button_el = instagram.find_elements(By.CSS_SELECTOR, "button")
        if len(button_el) > 1:
            button_el[1].click()
        time.sleep(10)
        name_pass = instagram.find_elements(By.CSS_SELECTOR, "input")
        random_id = self.generate_random_name()
        random_password = self.generate_random_password()
        random_name = self.generate_name(style='capital')
        if len(name_pass) > 1:
            name_pass[0].send_keys(random_name)
            name_pass[1].send_keys(random_password)
            print("\033[1;32m" + f"Cracked instagram Name: " + "\033[0m" + random_name)
            print("\033[1;32m" + f"Cracked instagram Password: " + "\033[0m" + random_password)
            form = instagram.find_elements(By.TAG_NAME, "button")
            if len(form) > 1:
                form[0].click()
                time.sleep(5)
            birth = instagram.find_elements(By.TAG_NAME, "select")
            birth_obj = Select(birth[2])
            birth_obj.select_by_index("20")
            submit = instagram.find_elements(By.TAG_NAME, "button")
            submit[1].click()
            time.sleep(10)
        try:
            checkbox = instagram.find_elements(By.XPATH, "//input[@type='checkbox']")
            checkbox[0].click()
            submit = instagram.find_elements(By.TAG_NAME, "button")
            submit[0].click()
            time.sleep(5)
        except:
            pass
        uid = instagram.find_elements(By.TAG_NAME, "input")
        uid[0].send_keys(random_id)
        submit = instagram.find_elements(By.TAG_NAME, "button")
        submit[0].click()
        Account = {
            "Email": mail_address,
            "Uid": random_id,
            "Name": random_name,
            "Password": random_password
        }
        time.sleep(60)
        with open('instagram_Cracked.txt', 'w') as w:
            w.write(str(Account))
        instagram.quit()
        mail.quit()
        print("\033[1;31m" + f"instagram Account Crack Completed ---> " + "\033[0m" + "./Crawl/instagram_Cracked.txt")
        while True:
            try:
                infor = self.Login.Striping_account_info()
                self.Login.login(infor)
                (lambda x: time.sleep(x))(100)
                os._exit(0)
            except:
                pass

def process():
    err_coun = 0
    IP = IPAnalyze()
    IPA = IP.Outer_IP_Get()
    print("\033[1;32m" + "Connection IP Address: " + "\033[0m" + IPA)
    IP.IPQS()
    while True:
        try:
            Instar = InstagramAccount(13, 12)
            Instar.virtual_mail()
            try:
                from Driver import WebdriverManager
                import reals
                Driver = WebdriverManager(display=True, user_oper=True)
                Driver.display_option()
                Driver.user_oper_option()
                Driver = Driver.Webdriver()
                Login = reals.InstagramLogin(Driver, Uid="____eunseok", Password="7788Lucas08130128")
                Login.form_new()
                Login.Login()
                Driver.quit()
                break
            except:
                Login.form_old()
                Login.Login()
                Driver.quit()
        except Exception as e:
            print(e)
            print("\033[1;31m" + f"instagram Account Crack Failed ---> " + "\033[0m")
            print("\033[1;33m" + "Reloading..." + "\033[0m")
            err_coun += 1
            if err_coun > 5:
                print("\033[1;31m" + f"Please Change VPN Server ---> " + "\033[0m")
                os._exit(0)

if __name__ == "__main__":
    process()

# //*[@id="mount_0_0_xV"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input
# //*[@id="mount_0_0_oe"]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/label/div/input
# *#mount_0_0_h3 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > section > main > div > div > div.x78zum5.xdt5ytf > div._aa4v > a:nth-child(2) > img
# //*[@id="mount_0_0_h3"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[3]/div[2]/a[2]/img
# //*[@id="mount_0_0_h3"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[3]/div[2]/a[2]/img
# //*[@id="mount_0_0_dX"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[1]/div[2]/span