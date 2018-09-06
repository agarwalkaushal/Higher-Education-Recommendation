from retriveColleges import colleges
from selenium import webdriver
from pprint import pprint

def getReviews():
    print()

driver = webdriver.Edge()
driver.implicitly_wait(15)

for i in range(0, len(a)):
    driver.get(a[i])
