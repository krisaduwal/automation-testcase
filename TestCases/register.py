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

Title = driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/h2").text
assert "New User Signup!" in Title
print("sign up page")

name = driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[2]")
name.send_keys("kris")

email = driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[3]")
email.send_keys("hello@g.com")

driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/button").click()
time.sleep(2)
info = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/h2/b").text
assert "enter account information" in info.lower()
print("enter info")

driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[1]/div[2]/label/div/span/input").click()
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[4]/input").send_keys("123456789")
Select(driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[5]/div/div[1]/div/select")).select_by_value("8")
Select(driver.find_element(By.ID, "months")).select_by_value("12")
Select(driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[5]/div/div[3]/div/select")).select_by_value("2001")

time.sleep(1)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[6]/div/span/input").click()
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[7]/div/span/input").click()

time.sleep(1)

driver.find_element(By.ID, "first_name").send_keys("kris")
driver.find_element(By.ID, "last_name").send_keys("duwal")
time.sleep(1)
driver.find_element(By.ID, "company").send_keys("minnie")
time.sleep(1)
driver.find_element(By.ID, "address1").send_keys("bhaktapur")
driver.find_element(By.ID, "address2").send_keys("ktm")
time.sleep(1)
Select(driver.find_element(By.ID, "country")).select_by_value("United States")
driver.find_element(By.ID, "state").send_keys("bagmati")
driver.find_element(By.ID, "city").send_keys("bkt")
time.sleep(1)
driver.find_element(By.ID, "zipcode").send_keys("1234")
time.sleep(1)
driver.find_element(By.ID, "mobile_number").send_keys("9876543210")
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/button").click()
created = driver.find_element(By.XPATH, "/html/body/section/div/div/div/h2/b").text
assert "account created" in created.lower()
print("account created")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/a").click()
loggedIn = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a").text
assert "Logged in as" in loggedIn
print("logged in as usrname")
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a").click()
# deleted = driver.find_element(By.XPATH, "/html/body/section/div/div/div/h2/b").text
# assert "account deleted" in deleted.lower()
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/a").click()
time.sleep(30)

