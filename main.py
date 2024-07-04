from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from random import randint
import os
import time

# ----------------------------------------- Function and Variable Declarations --------------------------------------- #

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
CREDENTIALS = [USERNAME, PASSWORD]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


def wait(minim=300, maxim=600) -> None:
    time.sleep(randint(minim, maxim) / 100)


# --------------------------------------------- Tinder Login --------------------------------------------------------- #
driver.get("https://tinder.com/")
wait()
log_in = driver.find_element(By.XPATH, value="//*[@id='u-684883901']/div/div[1]/div/main/div["
                                             "1]/div/div/div/div/header/div/div[2]/div[2]/a")
log_in.click()
wait()
log_in_fb = driver.find_element(By.XPATH, value="//*[@id='u1881702319']/div/div/div/div[1]/div/div/div[2]/div["
                                                "2]/span/div[2]/button")
log_in_fb.click()
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

# -------------------------------------------- Facebook Login -------------------------------------------------------- #

wait()
for char in USERNAME:
    wait(minim=5, maxim=10)
    driver.find_element(By.CSS_SELECTOR, value="#email_container input").send_keys(char)
wait()
for char in PASSWORD:
    wait(minim=5, maxim=10)
    driver.find_element(By.ID, value="pass").send_keys(char)
wait()
fb_login_btn = driver.find_element(By.ID, value="loginbutton")
fb_login_btn.click()

# ------------------------------------------- Tinder Dismiss Boxes --------------------------------------------------- #
driver.switch_to.window(tinder_window)
wait()
accept_cookies = driver.find_element(By.XPATH, value="//*[@id='u1881702319']/div/div[2]/div/div/div[1]/div[1]/button")
accept_cookies.click()
wait()
allow_location = driver.find_element(By.XPATH, value="//*[@id='u1881702319']/div/div/div/div/div[3]/button[1]")
allow_location.click()
wait()
reject_notifications = driver.find_element(By.XPATH, value="//*[@id='u1881702319']/div/div/div/div/div[3]/button[2]")
reject_notifications.click()
wait()
# ---------------------------------------- Tinder Swipe Right Behavior ----------------------------------------------- #
swipe = driver.find_element(By.XPATH, value="//*[@id='u-684883901']/div/div[1]/div/main/div[1]/div/div/div["
                                            "1]/div[1]/div/div[3]/div/div[4]/button")
while True:
    try:
        wait()
        swipe.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            try:
                wait()
                no_thanks = driver.find_element(By.XPATH, value='//*[@id="q840495415"]/div/div/button[2]/span')
                no_thanks.click()
            except NoSuchElementException:
                wait()
                reject_HS = driver.find_element(By.XPATH, value="//*[@id='u1881702319'']/div/div/div[2]/button[2]/span")
                reject_HS.click()
