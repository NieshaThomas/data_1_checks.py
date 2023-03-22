import pandas as pd
import csv

import matplotlib.pyplot as plt

import csv

import numpy as np

data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\Louisville_Metro_KY_-_LMPD_Hate_Crimes.csv')
df = pd.DataFrame(data, columns=['CRIME_TYPE','BIAS_MOTIVATION_GROUP', 'ZIP_CODE', 'PREMISE_TYPE'])

print(df)

labels = 'ANTI-BLACK', 'ANTI-WHITE', 'ANTI-MALE HOMOSEXUAL (GAY)', 'ANTI-FEMALE HOMOSEXUAL (LESBIAN)'
sizes = [15, 30, 45, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct= '%1.1f%%')

plt.show()









