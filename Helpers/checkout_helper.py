from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def do_checkout(driver):
    driver.find_element(By.CSS_SELECTOR, "#prooood > section:nth-child(2) > div > div:nth-child(2) > div > button").click()
    driver.find_element(By.CSS_SELECTOR, "#prooood > section:nth-child(1) > button").click()
    print("Berhasil masuk ke halaman checkout!")    
    time.sleep(3)
    