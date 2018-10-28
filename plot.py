from opinionAnalysis import upload
from opinionAnalysis import subjectivity
from opinionAnalysis import polarity
import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {}

data['Month'] = upload
data['Subjectivity'] = subjectivity
data['Polarity'] = polarity

df = pd.DataFrame(data)

grouped = df.groupby('Month')

print("Subjectivity")
print()
print(grouped['Subjectivity'].agg([np.mean, np.std]))
print()
print("Polarity")
print()
print(grouped['Polarity'].agg([np.mean, np.std]))

plt.figure(1)
plot_data = df.groupby('Month')['Subjectivity'].sum()
plot_data.sort_values().plot(kind='bar')
plt.title("Months")
plt.ylabel("Subjectivity")

plt.figure(2)
plot_data = df.groupby('Month')['Polarity'].sum()
plot_data.sort_values().plot(kind='bar')
plt.title("Months")
plt.ylabel("Polarity")

plt.figure(3)
freq = nltk.FreqDist(upload)
freq.plot(cumulative=False)
