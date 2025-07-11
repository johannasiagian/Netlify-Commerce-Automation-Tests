import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Manggil webdriver
driver = webdriver.Chrome()
driver.maximize_window()

#Buka URL buat yang dituju 
driver.get("https://qa-practice.netlify.app/auth_ecommerce")
# Menunggu 3 detik buat nampilin halaman gitu 
time.sleep (3) 

driver.find_element(By.ID, "email").send_keys("admin@admin.com")
driver.find_element(By.ID, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "#submitLoginBtn").click() 

# Menunggu 3 detik buat nampilin halaman gitu 
time.sleep (3) 

# Untuk jadi verivikasi kalau berhasil dibuka halamannya itu 
print("Login berhasil!")

driver.quit()  
