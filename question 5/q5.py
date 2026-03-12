import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
store_data = pd.read_csv(r'C:\Generation Data Analyst Bootcamp\interim project\question5\store_duration.csv')

# Calculate Duration
store_data['TradingDuration'] = 2014 - store_data['YearOpened']

# Group by Duration (Get the Averages)
duration_trends = store_data.groupby('TradingDuration')['TotalRevenue'].mean().reset_index()

# Calculate the Correlation Coefficient
# This checks the relationship on the RAW data (every single store)
correlation = store_data['TradingDuration'].corr(store_data['TotalRevenue'])

print(f"Statistical Analysis")
print(f"Correlation Coefficient: {correlation:.4f}")

# Interpretation logic for your terminal
if correlation > 0.5:
    print("Result: Strong Positive Relationship")
elif correlation > 0.3:
    print("Result: Moderate Positive Relationship")
elif correlation > 0.1:
    print("Result: Weak Positive Relationship")
else:
    print("Result: No significant relationship")

# VISUALIZATION 
plt.figure(figsize=(10, 6))

# Plot the AVERAGES with a trend line (Regression on the averages)
sns.regplot(data=duration_trends, x='TradingDuration', y='TotalRevenue', 
            color='green', marker='o')

plt.title('Question 5: Average Revenue Trend by Store Age', fontsize=14)
plt.xlabel('Years in Business (Trading Duration)')
plt.ylabel('Average Revenue ($)')
plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig('question5_final_trend.png')
plt.show()


