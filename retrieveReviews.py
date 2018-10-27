from retriveColleges import colleges
from selenium import webdriver

def getReviews(url):
    driver.get(url)
    elem = driver.find_elements_by_class_name("rvwv1Heading")
    reviews = driver.find_elements_by_xpath("//p[strong = 'Placements :']")
    if(len(elem)>0):
        for i in range(0, len(elem)):
            user = str(elem[i].find_element_by_css_selector("p").text)
            p = user.find(',')
            name = user[3:p]
            strings = user.split()
            month = strings[3]

            if month == "Jan" or month == "Feb" or month == "Mar" or month == "Apr" or month == "May" or month == "Jun" or month == "Jul" or month == "Aug" or month == "Sep" or month == "Oct" or month == "Nov" or month == "Dec":
                if user:
                    if reviews[i]:
                        review = reviews[i].text[13:]
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

