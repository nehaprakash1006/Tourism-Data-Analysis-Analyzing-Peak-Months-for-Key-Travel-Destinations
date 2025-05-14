import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_file = 'D:/Projects/DAV/Tourist_Sites_Monthly_Data.csv'  # Update as necessary
df = pd.read_csv(data_file)

# Rename columns
df.rename(columns={df.columns[0]: 'Site'}, inplace=True)

# Melt the DataFrame for analysis
df_melted = df.melt(id_vars='Site', var_name='Month', value_name='Visitor_Count')

# Convert 'Month' to categorical type with appropriate order
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=month_order, ordered=True)

# Seasonal classification
def classify_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Autumn'

df_melted['Season'] = df_melted['Month'].apply(classify_season)

# Group by season and site type
seasonal_summary = df_melted.groupby(['Site', 'Season'])['Visitor_Count'].sum().reset_index()

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x='Season', y='Visitor_Count', hue='Site', data=seasonal_summary)
plt.title('Total Visitor Counts by Season and Tourist Site', fontsize=18)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Total Visitor Count', fontsize=14)
plt.legend(title='Tourist Site')
plt.tight_layout()

# Save the plot
plt.savefig('seasonal_visitor_counts.pdf')
plt.show()
