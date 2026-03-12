import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r"C:\Generation Data Analyst Bootcamp\interim project\question 1 & 3\regional_revenue.csv")
#print(sales_data.info())

# Ensure we have the grouped data
country_totals = sales_data.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

# Visualization (Pie Chart)
plt.figure(figsize=(10, 8))

# We use the index (Country names) and the values (Total Revenue)
plt.pie(
    country_totals, 
    labels=country_totals.index, 
    autopct='%1.1f%%',   # This adds the percentage text inside the slices
    startangle=140, 
    colors=sns.color_palette('pastel')
)

plt.title('Question 3: Global Revenue Distribution by Country', fontsize=14)

# Save this for your report
plt.savefig('question3_global_revenue.png')
plt.show()