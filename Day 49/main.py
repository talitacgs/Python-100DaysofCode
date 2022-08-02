from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


chrome_drive_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get("https://www.linkedin.com/jobs/view/3201404965/?alternateChannel=search&refId=kj3y5RBcD12G3szwobx7MA%3D%3D&trackingId=T%2B8sS9bp%2FcDdv0rNIgPLTw%3D%3D&trk=d_flagship3_search_srp_jobs")

apply_button = driver.find_element(By.CLASS_NAME, "apply-button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(apply_button).click(apply_button).perform()

username = driver.find_element(By.ID, "username")
username.send_keys("YOUR_LINKEDIN_EMAIL")

password = driver.find_element(By.ID, "password")
password.send_keys("YOUR_LINKEDIN_PASSWORD")
password.send_keys(Keys.ENTER)

time.sleep(3)

easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
easy_apply.click()

next_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button.click()

next_button_2 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
next_button_2.click()

input_year = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
input_year.send_keys("0")

review_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
review_button.click()

follow_enterprise = driver.find_element(By.CLASS_NAME, "t-14")
follow_enterprise.click()

review_button_2 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
review_button_2.click()
