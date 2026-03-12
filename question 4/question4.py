import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
sick_data = pd.read_csv(r"C:\Generation Data Analyst Bootcamp\interim project\question4\sick_leave_data.csv")

# Group by PersonType and get the descriptive statistics for SickLeaveHours
stats_summary = sick_data.groupby('PersonType')['SickLeaveHours'].describe()

# Print the results to your terminal
print("Detailed Statistics for Sick Leave:")
print(stats_summary)

# You can also specifically print just the medians
medians = sick_data.groupby('PersonType')['SickLeaveHours'].median()
print("\nMedians per group:")
print(medians)


# Initialize the plot
plt.figure(figsize=(12, 6))

# Use a Box Plot to show the relationship between Category (PersonType) and Number (SickLeaveHours)
sns.boxplot(data=sick_data, x='PersonType', y='SickLeaveHours', palette='Set2')

# Add titles and labels
plt.title('Relationship: Sick Leave Hours by Person Type', fontsize=14)
plt.xlabel('Person Type (Category)')
plt.ylabel('Sick Leave Hours')

plt.savefig('sick_leave_boxplot.png')
plt.show()