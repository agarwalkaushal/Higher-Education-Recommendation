from retriveColleges import colleges
from selenium import webdriver
from pprint import pprint

def getReviews(url):
    print()

driver = webdriver.Edge()
driver.implicitly_wait(15)

for i in range(0, len(colleges)):
    colleges[i]=colleges[i]+"/reviews"
    print(colleges[i])
    #getReviews(colleges[i])
