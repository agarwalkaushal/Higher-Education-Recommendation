from retriveColleges import colleges
from selenium import webdriver

def getReviews(url):

    driver.get(url)
    elem = driver.find_elements_by_class_name("rvwv1Heading")
    reviews = driver.find_elements_by_xpath("//p[strong = 'Placements :']")

    if reviews:
        for i in range(0, len(reviews)):
            user = str(elem[i].find_element_by_css_selector("p").text)
            strings = user.split()
            if user:
                p = user.find(',')
                name = user[3:p]
                months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                for k in range(0, len(strings)):
                    if strings[k] in months:
                        month = strings[k]
                        break
            review = reviews[i].text
            row = []
            row.append(name)
            row.append(month)
            row.append(review)
            matrix.append(row)

matrix = [[]]

driver = webdriver.Edge()
driver.implicitly_wait(15)

numberOfColleges = len(colleges)

for i in range(0, numberOfColleges):
    colleges[i]=colleges[i]+"/reviews"
    getReviews(colleges[i])

driver.close()

