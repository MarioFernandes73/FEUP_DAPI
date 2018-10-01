from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time

def updateFile(path, linesArray):
    print("Updating file don't close the program...")
    with open(path, 'w', encoding='utf-8') as fileToOverwrite:
        fileToOverwrite.writelines(linesArray)
        fileToOverwrite.close()
    print("File successfully updated.")

def setupBrowser(driver):
    driver.get("https://www.allmovie.com/advanced-search")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, """//*[@id="qcCmpButtons"]/button[1]""")))
    time.sleep(1)
    driver.find_element_by_xpath("""//*[@id="qcCmpButtons"]/button[1]""").click()
    time.sleep(1)

def processElement(element):
    return str(element.text).strip().replace(",","")

def processLink(link):
    link = link[:-1]
    print("Processing link " + link)
    driver.get(link)
    time.sleep(1)
    try:
        title = processElement(driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[2]/header/hgroup[1]/h2"""))[:-7]
        synopsis = processElement(driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[2]/section[1]/div"""))
        genres = processElement(driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[2]/header/hgroup[2]/span[1]"""))[9:][:-3]
        subGenres = processElement(driver.find_element_by_xpath("""//*[@id="cmn_wrap"]/div[1]/div[2]/header/hgroup[2]/span[2]"""))[13:][:-3]
        return link + "," + synopsis + "\n"
    except Exception as e:
        print("Error: {0}".format(e))
        return link

year = "2018"
filePath = "../data/links_"+year+".csv"
chromePath = r"C:\Users\Mario\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromePath)
driver2 = webdriver.Chrome(chromePath)

setupBrowser(driver)

with open(filePath, "r") as linksFile:
    links = linksFile.readlines()
    linksFile.close()

for index, link in enumerate(links):
    if "," not in link:
        links[index] = processLink("https://www.allmovie.com/movie/the-gospel-according-to-andr%C3%A9-v691868\n")
        #updateFile(filePath, links)
        break
    else:
        print("Link " + link + " already processed, skipping...")