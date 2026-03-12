import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

store_data = pd.read_csv(r'C:\Generation Data Analyst Bootcamp\interim project\question6\store_size_employees.csv')


# To see which factor matters more: Size or Staff?
corr_size = store_data['SquareFeet'].corr(store_data['TotalRevenue'])
corr_staff = store_data['NumberEmployees'].corr(store_data['TotalRevenue'])

print(f"Correlation (Size vs Revenue): {corr_size:.4f}")
print(f"Correlation (Staff vs Revenue): {corr_staff:.4f}")


# VISUALIZATION: BUBBLE CHART 
plt.figure(figsize=(12, 8))

# We use a Scatterplot where 'hue' (color) and 'size' both represent the Number of Employees
sns.scatterplot(
    data=store_data, 
    x='SquareFeet', 
    y='TotalRevenue', 
    size='NumberEmployees',  # The dots get bigger with more staff
    hue='NumberEmployees',   # The dots get darker with more staff
    sizes=(20, 200),         # Range of dot sizes
    palette='viridis',       # Color scheme
    alpha=0.7                # Transparency so you can see overlapping dots
)

plt.title('Question 6: Impact of Store Size & Staff on Revenue', fontsize=15)
plt.xlabel('Store Size (Square Feet)', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend(title='Employees', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.savefig('question6_bubble_chart.png')
plt.show()
