from retrieveReviews import matrix
from textblob import TextBlob
import csv

for i in range(0, len(matrix)):
    if(len(matrix[i])>0):
        if (matrix[i][2]):
            review = matrix[i][2]
            analysis = TextBlob(review)
            opinion = analysis.sentiment
            matrix[i].append(opinion)

with open("opinions.csv","w+") as csvfile:
    csvWriter = csv.writer(csvfile,delimiter=',')
    csvWriter.writerows(matrix)