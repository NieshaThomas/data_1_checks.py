
import csv
import pandas as pd
import matplotlib as plt

data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')
print(data.head())

# total amount spent over all
import pandas as pd
data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')
data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)
total = sum(data['AMOUNTS PAID'])
print(total)

# food city total and first five line
import pandas as pd

data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')

data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)


FOODCITY_data = data.loc[(data['STORE NAME'] == 'FOOD CITY')]
FOODCITY_total = sum(FOODCITY_data['AMOUNTS PAID'])
print(data.head)
print(FOODCITY_total)

# dollar general total and first five lines
import pandas as pd

data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')

data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)


DOLLARGeneral_data = data.loc[(data['STORE NAME'] == 'DOLLAR General')]
DOLLARGeneral_total = sum(DOLLARGeneral_data['AMOUNTS PAID'])
print(data.head()) 
print(DOLLARGeneral_total)



# Hibbets total and first 5 lines
import pandas as pd

data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')

data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)


HIBBETTS_data = data.loc[(data['STORE NAME'] == 'HIBBETTS')]
HIBBETTS_total = sum(HIBBETTS_data['AMOUNTS PAID'])
print(data.head()) 
print(HIBBETTS_total)

# money gram total and first 5 lines

import pandas as pd

data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')

data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)


MONEY_GRAM_data = data.loc[(data['STORE NAME'] == 'MONEY GRAM')]
MONEYGRAM_total = sum(MONEY_GRAM_data['AMOUNTS PAID'])
print(data.head()) 
print(MONEYGRAM_total)



# dollar general total and first five lines
import pandas as pd

data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')

data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)



DOLLARGeneral_data = data.loc[(data['STORE NAME'] == 'DOLLAR General')]
DOLLARGeneral_total = sum(DOLLARGeneral_data['AMOUNTS PAID'])
print(data.head()) 
print(DOLLARGeneral_total)




import matplotlib.pyplot as plt
labels = 'WALMART', 'DOLLAR GENERAL', 'HIBBETTS', 'FOOD CITY', 'MONEY GRAM'
sizes = [1345.72, 467.00, 167.42, 117.26, 99.00]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.show()

# ebt payment method total and first five lines
import pandas as pd


data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')


data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)


EBT_Pay = data[(data['PAYMENT METHOD'] == 'EBT')]

EBT_total = sum(EBT_Pay['AMOUNTS PAID'])

print(EBT_Pay.head())

print(EBT_total)

#cash payment method total and first five lines

import pandas as pd


data = pd.read_csv(r'C:\Users\shede\OneDrive\Desktop\git\data_1_checks.py\ASSETS\FAMILY FINANCES SINCE 0801222.csv')


data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)


CASH_Pay = data[(data['PAYMENT METHOD'] == 'CASH')]

CASH_total = sum(CASH_Pay['AMOUNTS PAID'])

print(CASH_Pay.head())

print(CASH_total)


import matplotlib.pyplot as plt
labels = 'CASH', 'EBT'
sizes = [1371.65, 1327.71]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.show()


# wal total
data[data.columns[3]] = data[data.columns[3]].replace('[\$,]', '', regex=True).astype(float)
walmart_data = data.loc[(data['STORE NAME'] == 'WALMART')]
Wal_total = sum(walmart_data['AMOUNTS PAID'])
print(Wal_total)



Item_names = ['FOOD', 'HOUSE HOLD', 'Apperal']
Items_counts = [1345.71, 343.49, 277.00]

fig, ax = plt.subplots()
bar_container = ax.bar(Item_names, Items_counts)
ax.set(ylabel='Money Spent', title='Walmart Sales', ylim=(0, 2000))
ax.bar_label(bar_container, fmt='{:,.0f}')

plt.show()








