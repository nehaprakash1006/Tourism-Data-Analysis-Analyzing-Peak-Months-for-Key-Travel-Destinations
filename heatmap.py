import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file
data_file = 'D:/Projects/DAV/Tourist_Sites_Monthly_Data.csv'  # Update this path if necessary
try:
    df = pd.read_csv(data_file)

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty. Please check the CSV file.")

    # Print the DataFrame to inspect the structure and values
    print("DataFrame Contents:")
    print(df)

    # Rename the first column to 'Site'
    df.rename(columns={df.columns[0]: 'Site'}, inplace=True)

    # Prepare data for heatmap
    heatmap_data = df.set_index('Site').transpose()  # Transpose to have months on y-axis

    # Print transposed data to verify structure
    print("Transposed Data for Heatmap:")
    print(heatmap_data)

    # Plotting the heatmap
    plt.figure(figsize=(16, 10))  # Increased figure size for better readability
    sns.heatmap(
        heatmap_data,
        annot=False,  # Set to False to remove annotations
        cmap='YlGnBu',
        cbar_kws={'label': 'Visitor Count'},
        linewidths=.5,  # Add grid lines between cells
        linecolor='gray',  # Color of grid lines
    )
    plt.title('Heatmap of Tourist Sites by Month', fontsize=18)
    plt.xlabel('Site', fontsize=14)
    plt.ylabel('Month', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)  # Rotate x labels
    plt.yticks(fontsize=12)  # Adjust y labels
    plt.tight_layout()
    plt.savefig('heatmap_tourist_sites.png')  # Save the figure as PNG
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{data_file}' was not found. Please check the path.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
