from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

with open("links.csv", "w") as links: 
    chrome_path = r"C:\Users\Mario\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://www.allmovie.com/advanced-search")
    time.sleep(5)
    #WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, """//*[@id="qcCmpButtons"]/button[2]""")))
    driver.find_element_by_xpath("""//*[@id="qcCmpButtons"]/button[2]""").click()
    s1 = Select(driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[1]/section[2]/div/div/select[1]"""))
    s1.select_by_visible_text('2018')
    s2 = Select(driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[1]/section[2]/div/div/select[2]"""))
    s2.select_by_visible_text('2018')
    counter = 1
    while True:
        try:
            time.sleep(5)
            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, """#cmn_wrap > div.content-container > div.content > section.results > div.desktop-results > table > tbody""")))
            table = driver.find_element_by_css_selector("""#cmn_wrap > div.content-container > div.content > section.results > div.desktop-results > table > tbody""")
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                links.write((row.find_element(By.CSS_SELECTOR, "td.title > a").get_attribute('href') + "\n"))
            elem = driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[2]/section[2]/div[3]/div""")
            elem_childs = elem.find_elements_by_css_selector("*")
            if "Next" in str(elem_childs[len(elem_childs) - 1].get_attribute('innerHTML')):
                counter = counter + 1
                print("next page " + str(counter))
                elem = elem_childs[len(elem_childs) - 1].click()
            else:
                print("all done!")
                break
        except Exception as e:
            print("Error: {0}".format(e))
            break