
import csv
import pandas as pd
import matplotlib as plt

data = pd.read_csv('FAMILY FINANCES SINCE 0801222.csv')
data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)
total = sum(data['AMOUNTS PAID'])

print(total)

df = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')
print(df)

data = pd.read_csv('FAMILY FINANCES SINCE 0801222.csv')
data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)
total = sum(data['AMOUNTS PAID'])

import matplotlib.pyplot as plt
labels = 'WALMART', 'DOLLAR GENERAL', 'HIBBETTS', 'FOOD CITY', 'MONEY GRAM'
sizes = [1345.72, 467.00, 167.42, 117.26, 99.00]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.show()

import csv
import pandas as pd
df = pd.read_csv('pay_CASH.csv')
print(df)



import matplotlib.pyplot as plt
labels = 'CASH', 'EBT'
sizes = [1371.65, 1327.71]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.show()

df = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')

data = pd.read_csv('FAMILY FINANCES SINCE 0801222.csv')
data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)
total = sum(data['AMOUNTS PAID'])
# wal total
walmart_data = data.loc[(data['STORE NAME'] == 'WALMART')]
Wal_total = sum(walmart_data['AMOUNTS PAID'])
print(Wal_total)

Item_names = ['FOOD', 'HOUSE HOLD', 'Apperal']
Items_counts = [1460.20
, 343.49, 277.00]

fig, ax = plt.subplots()
bar_container = ax.bar(Item_names, Items_counts)
ax.set(ylabel='Money Spent', title='Walmart Sales', ylim=(0, 2000))
ax.bar_label(bar_container, fmt='{:,.0f}')

plt.show()








