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

def trimDetail(detailText):
    return str(detailText.replace("|","").replace(",","").replace("\n"," ").strip())

def processElement(cssSelector):
    try:
        element = driver.find_element(By.CSS_SELECTOR,cssSelector).text
        return str(element.replace(",","").replace("\n"," ").strip())
    except Exception:
        return ""

def processLink(link):
    with open("errorlog.txt", "a+") as errorlog:
        link = link[:-1]
        print("Processing link " + link)
        driver.get(link)
        time.sleep(1)
        try:
            title = trimDetail(driver.find_element(By.CSS_SELECTOR, "#cmn_wrap > div.content-container > div.content > header > hgroup.movie-info > h2").text[:-7])
            synopsis = trimDetail(driver.find_element(By.CSS_SELECTOR, "#cmn_wrap > div.content-container > div.content > section.review.read-more.synopsis > div").text)
            allmovieRating = trimDetail(driver.find_element(By.CSS_SELECTOR,"#microdata-rating > div").text)

            genres = ""
            subGenres = ""
            releaseDate = ""
            duration = ""
            countries = ""
            mpaaRating = ""

            movieDetails = driver.find_element(By.CSS_SELECTOR, "#cmn_wrap > div.content-container > div.content > header > hgroup.details")
            movieDetails = movieDetails.find_elements(By.XPATH, "*")
            for detail in movieDetails:
                if "Sub-Genres" in detail.text:
                    subGenres = trimDetail(detail.text[13:])
                elif "Genres" in detail.text:
                    genres = trimDetail(detail.text[9:])
                elif "Release Date" in detail.text:
                    releaseDate = trimDetail(detail.text[15:])[:12].replace("(","").strip()
                elif "Run Time" in detail.text:
                    duration = trimDetail(detail.text[11:])[:-5]
                elif "Countries" in detail.text:
                    countries = trimDetail(detail.text[12:])
                elif "MPAA Rating" in detail.text:
                    mpaaRating = trimDetail(detail.text[14:])

            directedBy = processElement("#movie-director-link")[12:]
            producedBy = processElement("#cmn_wrap > div.content-container > div.sidebar > section.basic-info > div.produced-by")[12:]
            releasedBy = processElement("#cmn_wrap > div.content-container > div.sidebar > section.basic-info > div.released-by")[12:]
            flags = processElement("#cmn_wrap > div.content-container > div.sidebar > section.basic-info > div.flags")[5:]

            moods = processElement("#cmn_wrap > div.content-container > div.content > section.characteristics > div.moods")[6:]
            themes = processElement("#cmn_wrap > div.content-container > div.content > section.characteristics > div.themes")[7:]
            keywords = processElement("#cmn_wrap > div.content-container > div.content > section.characteristics > div.keywords")[9:]
            attributes = processElement("#cmn_wrap > div.content-container > div.content > section.characteristics > div.attributes")[11:]

            relatedMovies = ""
            try:
                relatedMoviesElements = driver.find_element(By.CSS_SELECTOR, "#cmn_wrap > div.content-container > div.content > section.related-highlights > div.related-movies.clearfix")
                relatedMoviesElements = relatedMoviesElements.find_elements(By.XPATH, "*")
                for relatedMovie in relatedMoviesElements:
                    relatedMovies = relatedMovies + str(relatedMovie.find_element(By.CSS_SELECTOR, "div > img").get_attribute("alt")).replace(",","").replace("\n"," ").strip() + " | "
            except Exception as e:
                print("Error: {0}".format(e) + " --- NO RELATED MOVIES DETECTED, SKIPPING PARAMETER (no problem...)")
                errorlog.write(link + "\n" + "Error: {0}".format(e) + " --- NO RELATED MOVIES DETECTED, SKIPPING PARAMETER (no problem...)\n\n\n\n")

            relatedMovies = relatedMovies[:-3]

            driver.get(link + "/cast-crew")
            time.sleep(1)

            actors = ""
            try:
                castFirstContainer = driver.find_element(By.CSS_SELECTOR, "#cmn_wrap > div.content-container > div.content > section > div:nth-child(1)")
                castFirstContainerH2 = castFirstContainer.find_element(By.TAG_NAME, "h2")
                if "Cast" in castFirstContainerH2.text:
                    castContainers = castFirstContainer
                else:
                    castSecondContainer = driver.find_element(By.CSS_SELECTOR, "#cmn_wrap > div.content-container > div.content > section > div:nth-child(2)")
                    castSecondContainerH2 = castSecondContainer.find_element(By.TAG_NAME, "h2")
                    if "Cast" in castSecondContainerH2.text:
                        castContainers = castSecondContainer

                castContainers = castContainers.find_elements(By.CSS_SELECTOR, ".cast_container")
                for castContainer in castContainers:
                    try:
                        actors = actors + str(castContainer.find_element(By.CSS_SELECTOR, ".artist-name").text).replace(",","").replace("\n"," ").strip() + " | "
                    except Exception as e:
                        print("Error: {0}".format(e))
                        errorlog.write(link + "\n" + "Error: {0}".format(e) + "\n\n\n\n")

            except Exception as e:
                print("Error: {0}".format(e))
                errorlog.write(link + "\n" + "Error: {0}".format(e) + " ---- NO ACTORS DETECTED, SKIPPING PARAMETERS (no problem...)\n\n\n\n")

            actors = actors[:-3]
            return link + ", " + title + ", " + genres + ", " + subGenres + ", " + releaseDate + ", " + duration + ", " + countries + ", " + mpaaRating + ", " + allmovieRating + ", " + flags + ", " + directedBy + ", " + producedBy + ", " + releasedBy + ", " + moods + ", " + themes + ", " + keywords + ", " + attributes + ", " +  synopsis + ", " + actors + ", " + relatedMovies + "\n"
        except Exception as e:
            print("Error: {0}".format(e))
            errorlog.write(link + "\n" + "Error: {0}".format(e) + "\n\n\n\n")
            return link + "\n"

year = "2005"
filePath = "../data/links_"+year+".csv"
chromePath = r"C:\Users\Mario\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromePath)

setupBrowser(driver)

with open(filePath, "r", encoding="utf-8") as linksFile:
    links = linksFile.readlines()
    linksFile.close()

for index, link in enumerate(links):
    if "," not in link:
        links[index] = processLink(link)
        updateFile(filePath, links)
    else:
        print("Link " + link + " already processed, skipping...")

print("all done! :D")