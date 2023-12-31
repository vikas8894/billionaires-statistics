# -*- coding: utf-8 -*-
"""Untitled31.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1en_A8GRtSP7c5Gi6BT2DPpWTB0mq05Pg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df=pd.read_csv('/content/Billionaires Statistics Dataset.csv')
df

"""Data Cleaning
and Understanding Data
"""

df.drop_duplicates()

df.info()

df.isnull().sum()

"""Data Visualization

1.To find the industries from where billionaires generate the money.
"""

new_df=df.sort_values('finalWorth',ascending=False)
plt.barh(new_df['industries'],new_df['finalWorth'],color='teal')
plt.xlabel('net worth in billion')
plt.ylabel('Industries of billionaires')
plt.title('Industries as per net worth',color='green',size='20')
plt.gca().invert_yaxis()
plt.show()

"""It is Found that most of the income of billionaires is genrated through Fashiom and retail sector or they are associated to this industry.

2. to Know which country has maximum net worth in total genrated by top billionaires in world
"""

df.plot(x='country',y='finalWorth',kind='line')
plt.xlabel('List of countries',color='yellow',loc='right')
plt.xticks(rotation=45)
plt.ylabel('Net worth in billion',color='yellow')
plt.title('total worth as per country',size=16,color='pink')
plt.show()

"""It is found that United Kingdom has maximum net worth genrated from billionaires.

3. Rank the billionaires in terms of net worth.
"""

df_new=df.sort_values('rank',ascending=True).head(15)
plt.barh(df_new['personName'],df_new['rank'])
plt.gca().invert_yaxis()
plt.show()

"""It is found Bernard Arnault & Family is the most richest in world.
Mukesh Ambani from India ranks 9th.

4. Which state has maximum net worth in respect to billionaires?
"""

df.dropna(inplace=True)
df['state']
df=df.sort_values('finalWorth',ascending=False).head(20)
df.plot(x='state',y='finalWorth',kind='bar')
plt.xlabel('state')
plt.ylabel('net worth in billion')
plt.title('worth as per state in terms of money')

"""It is found Texas has maximum net worth.

5. What is the percentage contribution to billionaires list in terms of gender?
"""

gender_counts=df['gender'].value_counts()
plt.pie(gender_counts,labels=gender_counts.index,autopct='%.1f%%')
plt.legend(title='percentage of male and female in the list of billionaires',shadow=True)
shadow=True

"""It is found that 12.8% in the list are female and remaining 87.2% are male

6. To know the age groups of billionaires and what is the median age?
"""

plt.figure(figsize=(20,8))
sns.displot(df['age'].dropna(),bins=20,kde=True)
median_age=df['age'].median()
plt.axvline(median_age,linestyle='--',color='red',label=f'Median Age: {median_age:.2f}')
plt.xlabel('age groups of billionaires')
plt.ylabel('count of billionaires as per age group')
plt.title('Displot as per age group')
print(f"Median Age: {median_age:.2f}")

"""It is found that maximum billionaires lis in the age group between 55-75"""

df['status'].unique()

"""7. How many billionaires are self made and how many are in herited?"""

sns.countplot(data=df,x='selfMade')

"""The bar with False title are inherited billionaires and the one with True title are self made billionaires"""

df['gdp_country']=pd.to_numeric(df['gdp_country'],errors='coerce')
df['cpi_country']=pd.to_numeric(df['cpi_country'],errors='coerce')
df['total_tax_rate_country']=pd.to_numeric(df['total_tax_rate_country'],errors='coerce')
economic_columns=['gdp_country','cpi_country','total_tax_rate_country']
df[economic_columns].isnull().sum()

import plotly.express as px

"""8. To find the correlation between economic factors such as gdp, tax rate in respect to final worth."""

correlation=px.scatter_matrix(df,dimensions=['finalWorth','gdp_country','cpi_country','total_tax_rate_country'],color='status')
correlation.show()

"""9. To show the Total of net worth is maximum in which part of world on the image that relate to globe"""

import plotly.graph_objects as go

a=go.Figure(data=go.Scattergeo(
    lon=df["longitude_country"],
    lat=df["latitude_country"],
    text=df["personName"],
    mode="markers",
    marker=dict(
        size=8,
        opacity=0.6,
        color=df["finalWorth"],
        colorscale="Rainbow",
        colorbar=dict(title="Final Worth"))))
a.update_layout(title='geogrpahical distribution as per worth')
a.update_geos(projection_type="natural earth")
a.show()

"""It is found that maximum net worth genrated by billionaires is from Europe.

Thank You
"""