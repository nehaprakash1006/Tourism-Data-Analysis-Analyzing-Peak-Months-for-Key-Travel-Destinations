import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Tourist_Sites_Monthly_Data.csv")

# Monthly trend plot for a sample site, e.g., Taj Mahal
site_data = data[data["Site"] == "Taj Mahal"]
site_data_months = site_data.iloc[0, 1:]  # Select monthly data for the site

plt.figure(figsize=(10, 6))
sns.lineplot(data=site_data_months)
plt.title("Monthly Visitor Trend - Taj Mahal")
plt.xlabel("Month")
plt.ylabel("Visitor Count")
plt.xticks(rotation=45)  # Rotate month labels for better readability
plt.grid()
plt.show()
