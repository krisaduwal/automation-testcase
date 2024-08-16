import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")

home_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[1]/a")
assert home_element.text == "Home"
print("Success!")

footer = driver.find_element(By.XPATH, "/html/body/footer")
ActionChains(driver) \
    .scroll_to_element(footer) \
    .perform()
time.sleep(2)

subscription = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[2]/div/h2").text
assert "subscription" in subscription.lower()
print("subscription")

# driver.find_element(By.ID, "subscribe_email").click()
driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[2]/div/form/input[2]").send_keys("du@h.com")
time.sleep(3)
driver.find_element(By.ID, "subscribe").click()

time.sleep(10)

