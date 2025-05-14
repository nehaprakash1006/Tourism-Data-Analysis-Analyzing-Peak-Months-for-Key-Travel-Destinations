import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
data_file = 'D:/Projects/DAV/Tourist_Sites_Monthly_Data.csv'  # Update this path if necessary
try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(data_file)

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty. Please check the CSV file.")

    # Print the DataFrame to inspect the structure and values
    print("DataFrame Contents:")
    print(df)

    # Rename the first column to 'Site'
    df.rename(columns={df.columns[0]: 'Site'}, inplace=True)

    # Melt the DataFrame for easier plotting
    df_melted = df.melt(id_vars='Site', var_name='Month', value_name='Visitor_Count')

    # Print melted DataFrame to verify structure
    print("Melted DataFrame:")
    print(df_melted)

    # Set the figure size
    plt.figure(figsize=(12, 8))

    # Create a bar plot
    sns.barplot(x='Month', y='Visitor_Count', hue='Site', data=df_melted)

    # Add title and labels
    plt.title('Visitor Counts by Month for Tourist Sites', fontsize=18)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Visitor Count', fontsize=14)
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    plt.legend(title='Tourist Site')
    plt.tight_layout()

    # Save the plot as a PDF
    plt.savefig('barchart_tourist_sites.pdf')  # Save the figure as PDF
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{data_file}' was not found. Please check the path.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
