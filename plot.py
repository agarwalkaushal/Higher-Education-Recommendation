from opinionAnalysis import upload
from opinionAnalysis import subjectivity
from opinionAnalysis import polarity
import nltk
import pandas as pd
import numpy as np

data = {}

data['Month'] = upload
data['Subjectivity'] = subjectivity
data['Polarity'] = polarity

df = pd.DataFrame(data)

grouped = df.groupby('Month')

print("Subjectivity")
print()

print(grouped['Subjectivity'].agg([np.sum, np.mean, np.std]))
print()
print("Polarity")
print()

print(grouped['Polarity'].agg([np.sum, np.mean, np.std]))

freq = nltk.FreqDist(upload)
freq.plot(cumulative=False)
