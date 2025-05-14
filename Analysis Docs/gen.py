import pandas as pd
import numpy as np

# List of tourist sites
tourist_sites = [
    "Taj Mahal", "Red Fort", "Qutub Minar", "Gateway of India", "India Gate", "Hawa Mahal", "Amer Fort", 
    "Charminar", "Lotus Temple", "Meenakshi Temple", "Golden Temple", "Mysore Palace", "Jaisalmer Fort",
    "Jagannath Temple", "Konark Sun Temple", "Rani Ki Vav", "Fatehpur Sikri", "Sanchi Stupa", "Khajuraho Temples",
    "Chittorgarh Fort", "Ajanta Caves", "Ellora Caves", "Brihadeeswarar Temple", "Harmandir Sahib", "Somnath Temple",
    "Ranthambore National Park", "Kaziranga National Park", "Bandipur National Park", "Valley of Flowers", 
    "Sundarbans", "Jim Corbett National Park", "Rishikesh", "Varanasi Ghats", "Lonavala", "Munnar", "Coorg",
    "Mahabalipuram", "Mount Abu", "Udaipur City Palace", "Lake Palace", "Ranakpur Jain Temple", "Neemrana Fort",
    "Bandhavgarh National Park", "Bhimbetka", "Ramoji Film City", "Cellular Jail", "Hemis Monastery", "Pangong Lake",
    "Nubra Valley", "Rohtang Pass", "Spiti Valley", "Leh Palace", "Shanti Stupa", "Dal Lake", "Magnetic Hill",
    "Gulmarg", "Srinagar Houseboats", "Manali", "Kullu", "Ziro Valley", "Loktak Lake", "Nanda Devi", "Kedarnath",
    "Badrinath", "Yamunotri", "Gangotri", "Rameswaram", "Kanyakumari", "Vivekananda Rock Memorial", "Dhanushkodi",
    "Ooty", "Andaman and Nicobar Islands", "Lakshadweep", "Auroville", "Jantar Mantar", "Mehrangarh Fort",
    "Umaid Bhawan Palace", "Thar Desert", "Great Rann of Kutch", "Elephanta Caves", "Gwalior Fort", "Kanha National Park",
    "Pench National Park", "Rajaji National Park", "Chambal Wildlife Sanctuary", "Bishnupur Temples", "Nagarhole National Park",
    "Shivanasamudra Falls", "Hampi", "Badami Caves", "Pattadakal", "Chikmagalur", "Nandi Hills", "Dharamshala", 
    "McLeod Ganj", "Khardung La", "Tawang", "Itanagar", "Majuli Island", "Sula Vineyards"
]

# Set seed for reproducibility
np.random.seed(42)

# Create an empty DataFrame
data = pd.DataFrame({
    "Site": tourist_sites,
})

# Generate random tourist numbers for each month, with some seasonal variation
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for month in months:
    # Randomly generate tourists with higher numbers for peak months like Dec, Jan, and Nov
    if month in ["Dec", "Jan", "Nov"]:
        data[month] = np.random.randint(15000, 50000, size=len(tourist_sites))
    elif month in ["Apr", "May", "Jun", "Jul"]:
        data[month] = np.random.randint(10000, 30000, size=len(tourist_sites))
    else:
        data[month] = np.random.randint(5000, 25000, size=len(tourist_sites))

# Save to CSV
data.to_csv("Tourist_Sites_Monthly_Data.csv", index=False)
print("Dataset created and saved as 'Tourist_Sites_Monthly_Data.csv'")
