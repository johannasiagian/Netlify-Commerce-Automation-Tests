import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helpers.checkout_helper import do_checkout
from Helpers.login_helper import do_login
from selenium.webdriver.support.ui import Select  

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://qa-practice.netlify.app/auth_ecommerce")

do_login(driver, "admin@admin.com", "admin123")

time.sleep (3)

do_checkout(driver)
print("Berhasil masuk ke halaman checkout!")

driver.find_element(By.ID, "phone").send_keys("0812345689")
driver.find_element(By.CSS_SELECTOR, "#shippingForm > div:nth-child(2) > input").send_keys("Bandung")
driver.find_element(By.CSS_SELECTOR, "#shippingForm > div:nth-child(3) > input").send_keys("Jalan Praga no 11")

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#countries_dropdown_menu"))
dropdown.select_by_visible_text("Indonesia")

driver.find_element(By.CSS_SELECTOR, "#submitOrderBtn").click()

time.sleep(3)
print("Berhasil melakukan checkout!")

