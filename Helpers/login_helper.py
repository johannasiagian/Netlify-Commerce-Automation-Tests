import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qa-practice.netlify.app/auth_ecommerce")

def do_login(driver,email,password):
    driver.find_element(By.ID, "email").send_keys("admin@admin.com")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "#submitLoginBtn").click()
    time.sleep(5)
    print("Login berhasil yes!")