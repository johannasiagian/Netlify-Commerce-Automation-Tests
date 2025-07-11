import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

driver = webdriver.Chrome()
driver.get("https://qa-practice.netlify.app/register")
driver.maximize_window()

driver.find_element(By.ID, "firstName").send_keys("Budi")
driver.find_element(By.ID, "lastName").send_keys("Putra")
driver.find_element(By.ID, "phone").send_keys("08121212121")
dropdown = Select()