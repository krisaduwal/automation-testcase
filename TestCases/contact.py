import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")

home_element = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[1]/a")
assert home_element.text == "Home"
print("Success!")

driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[8]/a").click()

getIn = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/h2").text
assert "get in touch" in getIn.lower()
print("get in touch")

driver.find_element(By.NAME, "name").send_keys("kris")
time.sleep(1)
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
time.sleep(1)
driver.find_element(By.NAME, "subject").send_keys("report")
time.sleep(1)
driver.find_element(By.ID, "message").send_keys("there is a problem")
time.sleep(1)

# driver.find_element(By.NAME, "upload_file").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[6]/input").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(10)
