
#* Instargram Account automatic creater

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
import string
from selenium.webdriver.support.ui import Select
from names_generator import generate_name
import os
from requests import get

def generate_random_name(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

check_ip = "https://httpbin.org/ip"
url = "https://www.moakt.com/ok/inbox"
instargram_account = "https://www.instagram.com/accounts/signup/email/?next=https%3A%2F%2Fwww.instagram.com%2Faccounts%2F"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; Pixel 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15",
    "Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)",
    "Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",
    "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
    "AppleTV6,2/11.1",
]

def Outer_IP_Get():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip

def virtual_mail():
    options = Options()
    options.add_argument("--headless")
    random_user_agent = random.choice(user_agents)
    options.add_argument(f"--user-agent={random_user_agent}")
    mail = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    mail.get(url)
    time.sleep(3)
    mail.find_element(By.CSS_SELECTOR, "#mailForm > form > input.mail_butt").click()
    time.sleep(3)
    mail_address = mail.find_element(By.CSS_SELECTOR, "#email-address").text
    print("\033[1;32m" + f"Mail Cracked: " + "\033[0m" + mail_address)
    instargram = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    instargram.get(instargram_account)
    time.sleep(5)
    try:
        instargram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[3]/div[2]/a[2]/img")
        result = Instargram_Verify_Newest(instargram, mail_address, mail)
        if result == None:
            raise ConnectionRefusedError
    except:
        Instargram_Verify(instargram, mail_address, mail)

def Instargram_Verify_Newest(instargram, mail_address, mail):    
    form = instargram.find_elements(By.TAG_NAME, "input")
    if len(form) == 4:
        random_name = generate_name(style='capital')
        random_id = generate_random_name(13)
        random_password = generate_random_password(12)
        print("\033[1;32m" + f"Cracked Instargram Name: " + "\033[0m" + random_name)
        print("\033[1;32m" + f"Cracked Instargram uid: " + "\033[0m" + random_id)
        print("\033[1;32m" + f"Cracked Instargram Password: " + "\033[0m" + random_password)
        form[0].send_keys(mail_address)
        form[1].send_keys(random_name)
        form[2].send_keys(random_id)
        form[3].send_keys(random_password)
        id_submit = instargram.find_elements(By.TAG_NAME, "button")
        id_submit[2].click()
        time.sleep(10)
        birth = instargram.find_elements(By.TAG_NAME, "select")
        birth_obj = Select(birth[2])
        birth_obj.select_by_index("20")
        id_submit = instargram.find_elements(By.TAG_NAME, "button")
        id_submit[1].click()
        time.sleep(30)
        try:
            instargram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[1]/div[2]/span").text
            return None
        except:
            pass
            mail.refresh()
            Verified_Code = mail.find_element(By.CSS_SELECTOR, '#email_message_list > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text[0:6]
            time.sleep(1)
            print("\033[1;32m" + f"Cracked Instargram Verified Code: {Verified_Code}" + "\033[0m")
            time.sleep(10)
            submit = instargram.find_elements(By.TAG_NAME, "button")
            print(len(submit))
            submit[1].click()
            instargram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/div/button").click()
            birth = instargram.find_elements(By.TAG_NAME, "select")
            birth_obj = Select(birth[0])
            birth_obj.select_by_index("10")
            time.sleep(10)

def Instargram_Verify(instargram, mail_address, mail):
    email = instargram.find_element(By.XPATH, "//*[contains(@id, 'f')]")
    email.send_keys(mail_address)
    time.sleep(3)
    instargram.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div[3]/button").click()
    time.sleep(3)
    time.sleep(30)
    mail.refresh()
    Verified_Code = mail.find_element(By.CSS_SELECTOR, '#email_message_list > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text[0:6]
    time.sleep(1)
    print("\033[1;32m" + f"Cracked Instargram Verified Code: " + "\033[0m" + Verified_Code)
    time.sleep(10)
    instargram.find_element(By.XPATH, "//*[contains(@id, 'f')]").send_keys(Verified_Code)
    time.sleep(10)
    button_el = instargram.find_elements(By.CSS_SELECTOR, "button")
    if len(button_el) > 1:
        button_el[1].click()
    time.sleep(10)
    name_pass = instargram.find_elements(By.CSS_SELECTOR, "input")
    random_id = generate_random_name(13)
    random_password = generate_random_password(12)
    random_name = generate_name(style='capital')
    if len(name_pass) > 1:
        name_pass[0].send_keys(random_name)
        name_pass[1].send_keys(random_password)
        print("\033[1;32m" + f"Cracked Instargram Name: " + "\033[0m" + random_name)
        print("\033[1;32m" + f"Cracked Instargram Password: " + "\033[0m" + random_password)
        form = instargram.find_elements(By.TAG_NAME, "button")
        if len(form) > 1:
            form[0].click()
        birth = instargram.find_elements(By.TAG_NAME, "select")
        birth_obj = Select(birth[2])
        birth_obj.select_by_index("20")
        submit = instargram.find_elements(By.TAG_NAME, "button")
        submit[1].click()
        time.sleep(10)
    try:
        checkbox = instargram.find_elements(By.XPATH, "//input[@type='checkbox']")
        checkbox[0].click()
        submit = instargram.find_elements(By.TAG_NAME, "button")
        submit[0].click()
        time.sleep(5)
    except:
        pass
    uid = instargram.find_elements(By.TAG_NAME, "input")
    uid[0].send_keys(random_id)
    submit = instargram.find_elements(By.TAG_NAME, "button")
    submit[0].click()
    Account = {
        "Email": mail_address,
        "Uid": random_id,
        "Name": random_name,
        "Password": random_password
    }
    time.sleep(60)
    with open('Instargram_Cracked.txt', 'w') as w:
        w.write(str(Account))
    instargram.quit()
    mail.quit()
    print("\033[1;31m" + f"Instargram Account Crack Completed ---> " + "\033[0m" + "./Crawl/Instargram_Cracked.txt")
    os._exit(0)
    # account_initialize(random_id, random_password)

def account_initialize(uid, password):
    options = Options()
    random_user_agent = random.choice(user_agents)
    options.add_argument(f"--user-agent={random_user_agent}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    login = driver.find_elements(By.TAG_NAME, "button")
    login[2].click()
    time.sleep(3)
    text = driver.find_elements(By.TAG_NAME, "input")
    text = driver.find_elements(By.TAG_NAME, "input")
    time.sleep(3)
    text[0].send_keys(uid)
    time.sleep(3)
    text[1].send_keys(password)
    time.sleep(3)
    submit = driver.find_elements(By.TAG_NAME, "button")
    submit[0].click()


if __name__ == "__main__":
    err_coun = 0
    while True:
        try:
            virtual_mail()
        except:
            print("\033[1;31m" + f"Instargram Account Crack Failed ---> " + "\033[0m")
            print("\033[1;33m" + "Reloading..." + "\033[0m")
            err_coun += 1
            if err_coun > 5:
                print("\033[1;31m" + f"Please Change VPN Server ---> " + "\033[0m")
                os._exit(0)

# //*[@id="mount_0_0_xV"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input
# //*[@id="mount_0_0_oe"]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/label/div/input
# #mount_0_0_h3 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > section > main > div > div > div.x78zum5.xdt5ytf > div._aa4v > a:nth-child(2) > img
# //*[@id="mount_0_0_h3"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[3]/div[2]/a[2]/img
# //*[@id="mount_0_0_h3"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[3]/div[2]/a[2]/img
# //*[@id="mount_0_0_dX"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[1]/div[2]/span