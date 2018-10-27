from opinionAnalysis import upload
import nltk

freq = nltk.FreqDist(upload)
freq.plot(cumulative=False)
