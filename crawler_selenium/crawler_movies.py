from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time

with open("movies.csv", "w") as movies: 
    chrome_path = r"C:\Users\Mario\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://www.allmovie.com/movie/the-house-with-a-clock-in-its-walls-v693799")
    time.sleep(3)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, """//*[@id="cmn_wrap"]/div[1]/div[2]/section/div""")))
    text = driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[2]/section/div""").get_attribute('innerHTML')
    print(text)
    driver.close()