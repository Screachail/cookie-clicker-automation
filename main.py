from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
s=Service('/home/screachail/Downloads/chromedriver')
browser = webdriver.Chrome(service=s, options=options)
url='http://orteil.dashnet.org/experiments/cookie/'
browser.get(url)

time.sleep(2)
cookies = browser.find_element(By.LINK_TEXT, "Got it!")
cookies.click()
cookie = browser.find_element(By.ID, "cookie")
money = browser.find_element(By.ID, "money")


timeout = time.time() + 5
ending_time = time.time() + 60 * 5

while time.time() < ending_time:
    cookie.click()

    if time.time() > timeout:
        items = browser.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")

        if len(items) > 0:
            items[-1].click()

        timeout = time.time() + 5

print("Your final score:", browser.find_element(By.ID, "cps").text)
browser.save_screenshot("result.png")
browser.quit()