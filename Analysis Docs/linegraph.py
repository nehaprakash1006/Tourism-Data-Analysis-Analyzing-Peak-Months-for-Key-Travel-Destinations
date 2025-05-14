import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data_file = "Tourist_Sites_Monthly_Data.csv"  # Change this to your CSV file path
df = pd.read_csv(data_file)

# Rename the first column to 'Site'
df.rename(columns={df.columns[0]: 'Site'}, inplace=True)

# Set the index to the site names and transpose the DataFrame for plotting
df.set_index('Site', inplace=True)
df_transposed = df.transpose()

# Plotting
plt.figure(figsize=(12, 6))
for site in df_transposed.columns:
    plt.plot(df_transposed.index, df_transposed[site], marker='o', label=site)

plt.title('Monthly Visitor Count by Site')
plt.xlabel('Month')
plt.ylabel('Visitor Count')
plt.xticks(rotation=45)
plt.legend(title='Sites')
plt.grid()
plt.tight_layout()
plt.savefig('monthly_visitor_count_line_graph.png')
plt.show()
