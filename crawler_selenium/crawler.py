from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

chrome_path = r"C:\Users\Mario\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.allmovie.com/advanced-search")
WebDriverWait(driver,5)
driver.find_element_by_xpath("""//*[@id="qcCmpButtons"]/button[2]""").click()
s1 = Select(driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[1]/section[2]/div/div/select[1]"""))
s1.select_by_visible_text('2010')
driver.save_screenshot('screenshot.png')
driver.quit()