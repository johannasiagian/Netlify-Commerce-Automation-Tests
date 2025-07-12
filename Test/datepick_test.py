import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()    

driver.get("https://qa-practice.netlify.app/calendar")

driver.find_element(By.ID, "range-date-calendar").click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[3]').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[4]').click()
