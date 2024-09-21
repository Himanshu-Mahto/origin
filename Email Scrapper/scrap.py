from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("https://google.com")

WebDriverWait(driver, 3).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "truncate"))
)

input_element=driver.find_element(By.CLASS_NAME, "truncate")
input_element.clear()
input_element.send_keys("robot"+Keys.ENTER)
time.sleep(50)
driver.quit()
