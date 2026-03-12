# AdventureWorks Global Sales & Operations Analysis

## 🌍 Project Overview
This project presents a comprehensive exploratory data analysis of AdventureWorks’ global sales, human resources, and retail operations data.The objective was to uncover actionable business insights using the AdventureWorks 2019 SQL database and provide strategic recommendations for workforce and retail expansion.

## 🛠️ Tools & Methodology
* **SQL Server Management Studio (SSMS):** Used for database exploration, schema verification, and executing core data extraction queries. 
* **Advanced SQL (XML Parsing):** Employed the `WITH XMLNAMESPACES` clause and XQuery (`.value`) to parse complex XML data stored in the `Demographics` column of the `Sales.Store` table, extracting specific variables like store size, employee count, and year opened.
* **Python (Pandas, Matplotlib, Seaborn):** Used for data cleaning, calculating Pearson correlation coefficients, and generating high-level statistical graphics (regression plots, bubble charts, and box plots).

![Database Schema](https://github.com/helin-c/adventureworks-sales-hr-analysis/blob/main/Database%20Schema.png?raw=true)

## 📊 Key Business Insights & Visualizations

### 1. Regional Sales Dominance
**Question:** What are the regional sales in the best-performing country?
* **Insight:** The United States is the top-performing country globally, generating $70.8 million in revenue.Within the US, the Southwest region is the strongest performer at $27.1 million, followed by the Northwest ($18 million).

![Question 1](https://github.com/helin-c/adventureworks-sales-hr-analysis/blob/main/question%201/question1.png?raw=true) 

### 2. Annual Leave vs. Bonus Correlation
**Question:** What is the relationship between annual leave taken and bonus?
* **Insight:** A moderate positive correlation (r = 0.38) exists between accrued annual leave and financial bonuses. However, this relationship is driven by employee tenure rather than leave usage. Senior staff members accrue more vacation time and, due to their experience, consistently perform higher in sales, earning larger bonuses.

![question 2](https://github.com/helin-c/adventureworks-sales-hr-analysis/blob/main/question%202/vacation_bonus_relationship.png?raw=true)

### 3. Global Market Distribution
**Question:** What is the relationship between Country and Revenue?
* **Insight:** AdventureWorks is heavily reliant on the US market, which accounts for 57.5% of total global revenue. Canada follows at 14.9%, while European markets (France, Germany, UK) combined contribute a very small fraction of total sales. This reveals a massive untapped opportunity for European expansion.

![question 3](https://github.com/helin-c/adventureworks-sales-hr-analysis/blob/main/question%203/question3_global_revenue.png?raw=true)

### 4. Sick Leave by Job Title
**Question:** What is the relationship between sick leave and Job Title?
* **Insight:** General Employees (EM) accrue significantly more sick leave than Sales Personnel (SP). Physically intensive roles, such as Stockers and Janitors, average around 60 hours of sick leave, whereas Sales roles average 30-35 hours. This suggests that taking sick leave in commission-driven sales roles is likely discouraged by the employees themselves.

![question 4](https://github.com/helin-c/adventureworks-sales-hr-analysis/blob/main/question%204/sick_leave_boxplot.png?raw=true)


### 5. Store Age and Performance
**Question:** What is the relationship between store trading duration and revenue?
* **Insight:** There is no significant statistical relationship (r = 0.0136) between the age of a store and its financial performance. Stores open for 30+ years do not consistently outperform newer stores, indicating that age and established brand loyalty alone do not guarantee high revenue.

![question 5](https://github.com/helin-c/adventureworks-sales-hr-analysis/blob/main/question%205/question5_final_trend.png?raw=true)

### 6. Store Size & Staffing Impact
**Question:** What is the relationship between the size of the stores, number of employees, and revenue?
* **Insight:** A complex bubble chart was generated to evaluate size, staff, and revenue simultaneously. The correlation is incredibly weak for both size (0.10) and staffing (0.09). Large stores (75k+ sq ft) exhibit extreme revenue volatility—some generate nearly $1 million, while identically sized stores generate near zero. A well-managed small store is often just as profitable as a massive retail space.

![question 6](https://github.com/helin-c/adventureworks-sales-hr-analysis/blob/main/question%206/question6.png?raw=true)

## 🚀 Strategic Recommendations
1. **European Market Expansion:** Launch targeted marketing campaigns in France and Germany to diversify revenue streams away from heavy US reliance.
2. **Workforce Optimization:** Pivot capital away from expanding massive physical retail spaces and invest in staff coverage and sales training programs.
3. **Logistical Contingency Planning:** Cross-train staff to cover high-absence roles (like Stockers and Clerks) to prevent supply chain disruptions.

## 📂 Repository Contents
* **`question 1/` - `question 6/`**: Dedicated folders for each business question, containing the specific SQL data extraction queries, Python analysis scripts, and resulting visual charts.
* **`Database Schema.png`**: The Entity-Relationship Diagram (ERD) utilized to navigate the AdventureWorks database and map out SQL joins.
