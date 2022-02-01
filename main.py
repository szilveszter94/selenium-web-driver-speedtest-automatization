from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#selenium importálása
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "D:\Development\chromedriver.exe"

service_path = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_path)
# főoldal megnyitása

speedtest_url = "https://www.speedtest.net/"
twitter_url = "https://twitter.com/i/flow/login"

driver.get(speedtest_url)

# elfogadás gomb
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="_evidon-banner-acceptbutton"]').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()

time.sleep(50)
try:
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                  '8]/div/div/div[2]/a').click()
except NoSuchElementException:
    pass
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                              '3]/div/div/div[1]/div/div/div[2]/div[2]/a').click()
time.sleep(1)
download_speed = driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div['
                                     '1]/div[2]/div/div[2]/div/div[2]/span').text
upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/span').text

driver.get(twitter_url)
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                              '1]/div/div[5]/label/div/div[2]/div/input').send_keys("+36307099284")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                              '1]/div/div[6]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                              '1]/div/div[2]/div/label/div/div[2]/div[1]/input').send_keys("Pannika2006")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                              '2]/div/div').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                              '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div['
                              '1]/div/div/div/div/div[2]/div/div/div/div').send_keys(
    f"A letöltési sebesség {download_speed} Mbps, a feltöltési sebesség: {upload_speed} Mbps.")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                              '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()