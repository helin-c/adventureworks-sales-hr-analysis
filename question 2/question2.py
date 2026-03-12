import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

vacation_data = pd.read_csv(r"C:\Generation Data Analyst Bootcamp\interim project\question2\vacation_bonus.csv")
#print(vacation_data.info())
#print(vacation_data.describe())

correlation = vacation_data['VacationHours'].corr(vacation_data['Bonus'])
print(f"Correlation: {correlation:.2f}")

plt.figure(figsize=(10,6))
sns.regplot(data=vacation_data, x='VacationHours', y='Bonus', color='teal', marker='o')

plt.title('Relationship: Annual Leave vs. Bonus (Corr: 0.38)', fontsize=14)
plt.xlabel('Vacation Hours')
plt.ylabel('Bonus ($)')
plt.grid(True, alpha=0.3)

plt.savefig('vacation_bonus_relationship.png')
plt.show()