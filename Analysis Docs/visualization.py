import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('Tourist_Sites_Monthly_Data.csv')

# Set the 'Site' column as the index
data.set_index('Site', inplace=True)

# Transpose the data to have months as rows and sites as columns
data_t = data.T

# Plotting
plt.figure(figsize=(14, 8))
for site in data_t.columns:
    plt.plot(data_t.index, data_t[site], marker='', label=site)

# Adding labels and title
plt.title('Monthly Tourist Visits to Various Sites')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')
plt.xticks(rotation=45)
plt.grid()
plt.legend(title='Tourist Sites', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()
