from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_drive_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get('https://tinder.com/app/recs')

# Setup wait for later
wait = WebDriverWait(driver, 10)
# Store the ID of the original window
original_window = driver.current_window_handle

language_button = driver.find_element(By.CLASS_NAME, 'focus-button-style')
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(language_button).click(language_button).perform()
time.sleep(3)

login_button = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button/span[2]')
login_button.click()

wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

time.sleep(5)
email = driver.find_element(By.ID, 'identifierId')
email.send_keys("YOUR_PERSONAL@EMAIL.COM")
email.send_keys(Keys.ENTER)

next_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
next_btn.click()
email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
driver.implicitly_wait(10)
email.send_keys('YOURPASSWORD')
time.sleep(1)
next_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
next_btn.click()
time.sleep(1)

driver.switch_to.window(original_window)

allow_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_btn.click()
time.sleep(1)
activate_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
activate_btn.click()
time.sleep(15)

while True:
    like_btn = driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
    like_btn.click()
    time.sleep(2)
