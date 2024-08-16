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

driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a").click()
time.sleep(2)
products = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2").text
assert "all products" in products.lower()
print("all products page")

clickable = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]")
ActionChains(driver)\
    .click(clickable)\
    .perform()

# time.sleep(2)
driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[1]/div/div/div[3]/button").click()
time.sleep(2)

clickable1 = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]")
ActionChains(driver)\
    .click(clickable1)\
    .perform()
driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/a").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[1]/div/div/div[2]/p[2]/a/u").click()

time.sleep(10)