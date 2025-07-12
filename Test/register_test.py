from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://qa-practice.netlify.app/register")

driver.find_element(By.ID, "firstName").send_keys("Budi")
driver.find_element(By.ID, "lastName").send_keys("Santoso")
driver.find_element(By.ID, "phone").send_keys("081234567890")
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#countries_dropdown_menu"))
dropdown.select_by_visible_text("Indonesia")
driver.find_element(By.ID, "emailAddress").send_keys("budi@gmail.com")
driver.find_element(By.ID, "password").send_keys("budi12345")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#registerBtn").click()

time.sleep(3)

print("Berhasil melakukan registrasi!")

driver.quit()