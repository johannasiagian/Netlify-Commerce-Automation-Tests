import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helpers.login_helper import do_login


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://qa-practice.netlify.app/auth_ecommerce")

do_login(driver, "admin@admin.com", "admin123")

time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#prooood > section:nth-child(2) > div > div:nth-child(2) > div > button").click()
driver.find_element(By.CSS_SELECTOR, "#prooood > section:nth-child(1) > button").click()

print("Berhasil masuk ke halaman checkout!")

driver.quit()  