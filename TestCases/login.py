import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")

home_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[1]/a")
assert home_element.text == "Home"
print("Success!")

signUp = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")
signUp.click()

Title = driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/h2").text
assert "Login to your account" in Title
print("login page")

# login with correct email and password
# time.sleep(2)
# driver.find_element(By.NAME, "email").send_keys("hello@g.com")
# time.sleep(1)
# driver.find_element(By.NAME, "password").send_keys("123456789")
# time.sleep(1)
# driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/button").click()
# time.sleep(2)
# loggedIn = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a").text
# assert "Logged in as" in loggedIn
# print("logged in as username")


# login with incorrect email and password
driver.find_element(By.NAME, "email").send_keys("helo@g.com")
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys("1234589")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/button").click()
time.sleep(2)
loggedIn = driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/p").text
assert "Your email or password is incorrect" in loggedIn
print("incorrect email or password")

time.sleep(5)