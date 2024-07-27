import pandas as pd
import json

# Load the scraped data from 'output.json'
with open('output.json', 'r') as f:
    data = json.load(f)

# Prepare the data for DataFrame
amenities_set = set()
listings_dict = {}

# Populate the listings dictionary and the set of all amenities
for entry in data:
    listing_name = entry['title']
    amenities = entry.get('amenities', [])
    
    # Initialize the dictionary for each listing if not already present
    if listing_name not in listings_dict:
        listings_dict[listing_name] = {}
    
    # Update the set of all possible amenities
    for amenity in amenities:
        amenities_set.add(amenity)
        # Mark the amenity as present for this listing
        listings_dict[listing_name][amenity] = 1

# Create a DataFrame with amenities as rows and listings as columns
df = pd.DataFrame(columns=sorted(listings_dict.keys()), index=sorted(amenities_set))

# Fill the DataFrame with the presence data (1 for present)
for listing, amenities in listings_dict.items():
    for amenity in amenities:
        df.at[amenity, listing] = 1

# Fill NaN values with 0 (indicating absence of an amenity)
df.fillna(0, inplace=True)

# Export the DataFrame to a CSV file
df.to_csv('dormy_amenities_matrix.csv')

print("Data has been exported to 'dormy_amenities_matrix.csv'")
