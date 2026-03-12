import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r"C:\Generation Data Analyst Bootcamp\interim project\question 1 & 3\regional_revenue.csv")
#print(sales_data.info())


# Finding the best performing country automatically
country_totals = sales_data.groupby('Country')['Revenue'].sum().sort_values(ascending=False)
best_country = country_totals.index[0]
print(country_totals)
print(f"The best performing country is {best_country} with ${country_totals.iloc[0]:,.2f} in revenue.")

# Extracting ONLY the regions for that best country
best_country_data = sales_data[sales_data['Country'] == best_country]

# VISUALIZATION
plt.figure(figsize=(10,6))
sns.barplot(data=best_country_data, 
            x='Region', y='Revenue',hue='Region',legend=False, palette='flare')

plt.title(f'Question 1: Regional Sales in {best_country}', fontsize=14)
plt.xlabel('Region')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45) 
plt.savefig('question1.png')
plt.show()