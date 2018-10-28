from selenium import webdriver

def getColleges(url):
    global c
    driver.get(url)
    elems = driver.find_elements_by_xpath("//a[@href][@class='tuple-institute-name']")
    for elem in elems:
        colleges.append(elem.get_attribute("href"))
        c = c + 1

driver = webdriver.Edge()
driver.implicitly_wait(15)
startWith = "https://www.shiksha.com/b-tech/colleges/b-tech-colleges-india"
colleges = []
c = 0
driver.get(startWith)
getColleges(startWith)

numberOfPages = 2

# for i in range (2,numberOfPages):
#     url = driver.find_element_by_xpath("//a[@href][@data-page='"+str(i)+"']").get_attribute("href")
#     getColleges(url)

driver.close()