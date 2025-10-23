#Highlight a section and hit 'Ctrl' + '/' to focus on sections you want to run


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir(r'<replace with the path for the folder where you have the csv files downloaded')

cr= pd.read_csv('mainCountryRev.csv')
print(cr.head())
cust= pd.read_csv('CountryCustomers.csv')
print(cust.head()) 
units= pd.read_csv('CountryUnits.csv')
print(units.head()) 
why= pd.read_csv('FormingTargets.csv')
print(why.head()) 

## FIGURE 1: BAR CHART OF REVENUE PER COUNTRY
plt.figure()
plt.bar(cr['Country'], cr['TotalRevenueUSD'], color='blue', zorder=2)
plt.xlabel('Country', size= 14,  weight= 'semibold')
plt.ylabel('Revenue ($)', size=14, weight= 'semibold') 
plt.ylim(0, 65000000)
plt.yticks(range(0,65000001,5000000),[f'{round(x/1000000)}M' for x in range(0, 65000001, 5000000)])
plt.grid(axis='y', alpha= 0.5, zorder=0) 
plt.title('Total Revenue by Country', size= 18, weight= 'bold')
# plt.text(0.5, 10000001, 'Australian and German\noperations only began in May 2013', size= 8, horizontalalignment='center')
# plt.text(4.5, 50000001, 'Revenue in the US stores is more than x2\nthe revenue of all other countries combined', size= 8, horizontalalignment='right')
plt.tight_layout()
plt.show() 

## FIGURE 1.5: BAR CHART OF REVENUE PER COUNTRY WITHOUT CURRENCY EXCHANGE
we= pd.read_csv('withoutExch.csv')
print(we.head())
plt.figure()
plt.bar(we['Country'], we['TotalRevenueUSD'], color='blue', zorder=2)
plt.xlabel('Country', size= 14,  weight= 'semibold')
plt.ylabel('Revenue ($)', size=14, weight= 'semibold') 
plt.ylim(0, 65000000)
plt.yticks(range(0,65000001,5000000),[f'{round(x/1000000)}M' for x in range(0, 65000001, 5000000)])
plt.grid(axis='y', alpha= 0.5, zorder=0) 
plt.title('Total Revenue by Country', size= 18, weight= 'bold')
plt.text(0.5, 10000001, 'Australian and German\noperations only began in May 2013', size= 8, horizontalalignment='center')
plt.text(4.5, 50000001, 'Revenue in the US stores is more than x2\nthe revenue of all other countries combined', size= 8, horizontalalignment='right')
plt.tight_layout()
plt.show() 

# Filter out USA before creating the plot
cr_filtered = cr[cr['Country'] != 'United States']

## FIGURE 1: BAR CHART OF REVENUE PER COUNTRY (EXCLUDING USA)
plt.figure()
plt.bar(cr_filtered['Country'], cr_filtered['TotalRevenueUSD'], color='blue', zorder=2)
plt.xlabel('Country', size=14, weight='semibold')
plt.ylabel('Revenue ($)', size=14, weight='semibold') 
plt.ylim(0, 12000000)
plt.yticks(range(0,12000001,2000000),[f'{round(x/1000000)}M' for x in range(0, 12000001, 2000000)])
plt.text(0.5, 8000001, 'Australian and German\noperations only began in May 2013', size= 12, horizontalalignment='center')
plt.grid(axis='y', alpha=0.5, zorder=0) 
plt.title('Total Revenue by Country (Excluding USA)', size=18, weight='bold')
plt.tight_layout()
plt.show()

## FIGURE 2: INVESTIGATING REVENUE BY COUNTRY
fig, ax = plt.subplots()
revenue_pct = cr['TotalRevenueUSD'] / (cr['TotalRevenueUSD'].sum()) * 100
stores_pct = cust['NumStores'] / (cust['NumStores'].sum()) * 100
customers_pct = cust['NumCustomers'] / (cust['NumCustomers'].sum()) * 100
units_pct = units['NumUnitsSold'] / (units['NumUnitsSold'].sum()) * 100
width, x = 0.2, np.arange(len(cust['Country'])) 
ax.bar(x - width, stores_pct, width=width, label='Stores', color='aquamarine', zorder=2)
ax.bar(x, customers_pct, width=width, label='Customers', color='darkturquoise', zorder=2)
ax.bar(x + width, units_pct, width=width, label='Units', color='skyblue', zorder=2)
ax2 = ax.twinx()  
ax2.plot(x, revenue_pct, label='Revenue', color='blue', marker='o')
ax.set_xlabel('Country', weight='bold')
ax.set_ylabel('Percentage', weight='bold')
ax.set_xticks(x, labels= cust['Country'])
ax2.set_yticklabels([]) 
ax2.set_yticks([])
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.set_title('Distribution of Factors Influencing Country Revenue', weight='bold', size=15)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
plt.tight_layout()
plt.show()

## FIGURE 2: INVESTIGATING REVENUE BY COUNTRY WITHOUT CURRENCY EXCHANGE
fig, ax = plt.subplots()
revenue_pct = we['TotalRevenueUSD'] / (we['TotalRevenueUSD'].sum()) * 100
stores_pct = cust['NumStores'] / (cust['NumStores'].sum()) * 100
customers_pct = cust['NumCustomers'] / (cust['NumCustomers'].sum()) * 100
units_pct = units['NumUnitsSold'] / (units['NumUnitsSold'].sum()) * 100
width, x = 0.2, np.arange(len(cust['Country'])) 
ax.bar(x - width, stores_pct, width=width, label='Stores', color='aquamarine', zorder=2)
ax.bar(x, customers_pct, width=width, label='Customers', color='darkturquoise', zorder=2)
ax.bar(x + width, units_pct, width=width, label='Units', color='skyblue', zorder=2)
ax2 = ax.twinx()  
ax2.plot(x, revenue_pct, label='Revenue', color='blue', marker='o')
ax.set_xlabel('Country', weight='bold')
ax.set_ylabel('Percentage', weight='bold')
ax.set_xticks(x, labels= cust['Country'])
ax2.set_yticklabels([]) 
ax2.set_yticks([])
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.set_title('Distribution of Factors Influencing Country Revenue', weight='bold', size=15)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
plt.tight_layout()
plt.show()

## FIGURE 3: DISTRIBUTION OF PRICE BRACKETS OF PURCHASES BY UNITED KINGDOM AND CANADA
why2 = why[why['Country'].isin(['GB', 'CA'])]
PriceCategory = ['$10<','$10-49','$50-99','$100-499','$500-999','$1000>=']
bins = [0,10,50,100,500,1000,float('inf')]
why2['PricePt'] = pd.cut(why2['UnitPrice'], bins=bins, labels=PriceCategory)
print(why2.head())
why2.groupby('Country')['PricePt'].value_counts(normalize=True).unstack('PricePt').plot.barh(stacked=True, cmap='viridis')
plt.ylabel('Country', size= 14,  weight= 'semibold')
plt.xlabel('Distributions', size=14) 
plt.title('Country Comparison Distribution of Purchases by Price', size= 18, weight= 'bold')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()