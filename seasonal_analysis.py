import pandas as pd
import matplotlib.pyplot as plt

# Sample data (assuming your data is structured similarly)
# You would replace this with your actual data import
data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'Site_A': [1200, 1100, 1500, 1700, 2300, 2400, 2000, 1900, 1800, 1600, 1300, 1400],
    'Site_B': [900, 850, 1200, 1500, 1800, 1900, 1700, 1600, 1400, 1300, 1100, 1150],
    'Site_C': [600, 650, 800, 1000, 1200, 1400, 1300, 1500, 1450, 1300, 900, 950]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define seasons
seasons = {
    'Winter': ['December', 'January', 'February'],
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August'],
    'Monsoon': ['September', 'October', 'November']
}

# Initialize a DataFrame for seasonal data
seasonal_counts = {season: [] for season in seasons}

# Aggregate monthly counts into seasonal totals
for season, months in seasons.items():
    seasonal_totals = df[df['Month'].isin(months)].sum(numeric_only=True)
    seasonal_counts[season] = seasonal_totals

# Create a new DataFrame for seasonal data
seasonal_df = pd.DataFrame(seasonal_counts)

# Plotting
plt.figure(figsize=(14, 8))  # Increased figure size
seasonal_df.plot(kind='bar', figsize=(14, 8))  # Ensure bar plot matches figure size
plt.title('Seasonal Visitor Counts to Tourist Sites', fontsize=16)
plt.xlabel('Tourist Sites', fontsize=14)
plt.ylabel('Total Visitors', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.grid(axis='y')

# Use subplots_adjust to fine-tune layout
plt.subplots_adjust(bottom=0.15, top=0.9, left=0.1, right=0.95)

# Show the plot
plt.show()

# Box Plot Visualization
plt.figure(figsize=(14, 8))  # Increased figure size for the box plot
seasonal_df_melted = seasonal_df.melt(var_name='Season', value_name='Visitors')
seasonal_df_melted.boxplot(by='Season', figsize=(14, 8))
plt.title('Box Plot of Seasonal Visitor Counts to Tourist Sites', fontsize=16)
plt.suptitle('')  # Suppress the default title to clean up the plot
plt.xlabel('Season', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)
plt.grid(axis='y')

# Use subplots_adjust for the box plot
plt.subplots_adjust(bottom=0.15, top=0.9, left=0.1, right=0.95)

# Show the box plot
plt.show()
