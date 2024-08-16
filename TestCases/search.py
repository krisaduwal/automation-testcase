import time

from selenium import webdriver
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


driver.find_element(By.XPATH, "/html/body/section[1]/div/input").send_keys("Blue Top")
driver.find_element(By.ID, "submit_search").click()
time.sleep(2)

searched = driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2").text
assert "searched products" in searched.lower()
print("searched products verify")
time.sleep(3)