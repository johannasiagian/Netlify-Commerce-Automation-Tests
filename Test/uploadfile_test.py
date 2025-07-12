import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qa-practice.netlify.app/file-upload")
driver.maximize_window()

driver.find_element(By.ID, "file_upload").send_keys("C:/Users/Dian Pramesti/Downloads/putih.png")
driver.find_element(By.CSS_SELECTOR, "#content > div.input-group > div > button").click()

time.sleep(5)

print("Berhasil upload file ea!")

driver.quit()