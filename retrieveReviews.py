from retriveColleges import colleges
from selenium import webdriver
from pprint import pprint

def getReviews(url):
    driver.get(url)
    elem = driver.find_elements_by_class_name("rvwv1Heading")
    review = driver.find_elements_by_xpath("//p[strong = 'Placements :']")
    if(len(elem)>0):
        for i in range(0, len(elem)):
            user = elem[i].find_element_by_css_selector("p")

            #print(user.text)
            if review[i]:
                #TODO extract user name from user.text and review.text without placement and make a matrix
                #print(review[i].text)
            print()

reviews = [[]]

driver = webdriver.Edge()
driver.implicitly_wait(15)

for i in range(0, len(colleges)):
    colleges[i]=colleges[i]+"/reviews"
    getReviews(colleges[i])

driver.close()
