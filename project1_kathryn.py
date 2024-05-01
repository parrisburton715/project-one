#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
from census import Census
from tabulate import tabulate
import requests

# API key
api_key = "5ac8a932d7cbd9f6812d0e23d23f15c4b900ca27"

# Create Census object
c = Census(api_key, year=2013)

# Dictionary mapping state codes to state names
state_mapping = {
    '01': 'Alabama', '02': 'Alaska', '04': 'Arizona', '05': 'Arkansas',
    '06': 'California', '08': 'Colorado', '09': 'Connecticut', '10': 'Delaware',
    '11': 'District of Columbia', '12': 'Florida', '13': 'Georgia', '15': 'Hawaii',
    '16': 'Idaho', '17': 'Illinois', '18': 'Indiana', '19': 'Iowa', '20': 'Kansas',
    '21': 'Kentucky', '22': 'Louisiana', '23': 'Maine', '24': 'Maryland',
    '25': 'Massachusetts', '26': 'Michigan', '27': 'Minnesota', '28': 'Mississippi',
    '29': 'Missouri', '30': 'Montana', '31': 'Nebraska', '32': 'Nevada',
    '33': 'New Hampshire', '34': 'New Jersey', '35': 'New Mexico', '36': 'New York',
    '37': 'North Carolina', '38': 'North Dakota', '39': 'Ohio', '40': 'Oklahoma',
    '41': 'Oregon', '42': 'Pennsylvania', '44': 'Rhode Island', '45': 'South Carolina',
    '46': 'South Dakota', '47': 'Tennessee', '48': 'Texas', '49': 'Utah', '50': 'Vermont',
    '51': 'Washington', '54': 'West Virginia', '55': 'Wisconsin', '56': 'Wyoming',
    '72': 'Puerto Rico'
}

# Define Census API URL
census_api_url = "https://api.census.gov/data/2013/acs/acs5"

# Define variables for infant mortality data
infant_variables = {
    "get": "NAME,B01001_001E,B01001_011E",
    "for": "state:*"
}

# Fetch infant mortality data from Census API
infant_data = requests.get(census_api_url, params=infant_variables).json()

# Convert the API response to a pandas DataFrame
if infant_data:
    infant_mortality_df = pd.DataFrame(infant_data[1:], columns=infant_data[0])
    infant_mortality_df['State'] = infant_mortality_df['state'].map(state_mapping)
    infant_mortality_df["Mortality Rate"] = infant_mortality_df["B01001_011E"].astype(float) / infant_mortality_df["B01001_001E"].astype(float)
    selected_columns = ["State", "Mortality Rate"]
    print("\nInfant Mortality DataFrame:")
    print(tabulate(infant_mortality_df[selected_columns], headers='keys', tablefmt='pretty'))

    # Calculate highest and lowest infant mortality rates
    highest_infant_mortality = infant_mortality_df.nlargest(5, "Mortality Rate")
    lowest_infant_mortality = infant_mortality_df.nsmallest(5, "Mortality Rate")
    print("\nTop 5 states with highest infant mortality rates:")
    print(tabulate(highest_infant_mortality[selected_columns], headers='keys', tablefmt='pretty'))
    print("\nTop 5 states with lowest infant mortality rates:")
    print(tabulate(lowest_infant_mortality[selected_columns], headers='keys', tablefmt='pretty'))


# In[23]:


# Define variables for maternal mortality data
maternal_variables = {
    "get": "NAME,B01001_001E,B01001_012E",
    "for": "state:*"
}

# Fetch maternal mortality data from Census API
maternal_data = requests.get(census_api_url, params=maternal_variables).json()

# Convert the API response to a pandas DataFrame
if maternal_data:
    maternal_mortality_df = pd.DataFrame(maternal_data[1:], columns=maternal_data[0])
    maternal_mortality_df['State'] = maternal_mortality_df['state'].map(state_mapping)
    maternal_mortality_df["Mortality Rate"] = maternal_mortality_df["B01001_012E"].astype(float) / maternal_mortality_df["B01001_001E"].astype(float)
    print("\nMaternal Mortality DataFrame:")
    print(tabulate(maternal_mortality_df[selected_columns], headers='keys', tablefmt='pretty'))

    # Calculate highest and lowest maternal mortality rates
    highest_maternal_mortality = maternal_mortality_df.nlargest(5, "Mortality Rate")
    lowest_maternal_mortality = maternal_mortality_df.nsmallest(5, "Mortality Rate")
    print("\nTop 5 states with highest maternal mortality rates:")
    print(tabulate(highest_maternal_mortality[selected_columns], headers='keys', tablefmt='pretty'))
    print("\nTop 5 states with lowest maternal mortality rates:")
    print(tabulate(lowest_maternal_mortality[selected_columns], headers='keys', tablefmt='pretty'))


# In[26]:


# Define variables for infant mortality data
infant_variables = {
    "get": "NAME,B01001_001E,B01001_011E",
    "for": "state:*"
}

# Fetch infant mortality data from Census API
infant_data = requests.get(census_api_url, params=infant_variables).json()

# Convert the API response to a pandas DataFrame
if infant_data:
    infant_mortality_df = pd.DataFrame(infant_data[1:], columns=infant_data[0])
    infant_mortality_df['State'] = infant_mortality_df['state'].map(state_mapping)
    infant_mortality_df["Infant Mortality Rate"] = infant_mortality_df["B01001_011E"].astype(float) / infant_mortality_df["B01001_001E"].astype(float)

# Define variables for maternal mortality data
maternal_variables = {
    "get": "NAME,B01001_001E,B01001_012E",
    "for": "state:*"
}

# Fetch maternal mortality data from Census API
maternal_data = requests.get(census_api_url, params=maternal_variables).json()

# Convert the API response to a pandas DataFrame
if maternal_data:
    maternal_mortality_df = pd.DataFrame(maternal_data[1:], columns=maternal_data[0])
    maternal_mortality_df['State'] = maternal_mortality_df['state'].map(state_mapping)
    maternal_mortality_df["Maternal Mortality Rate"] = maternal_mortality_df["B01001_012E"].astype(float) / maternal_mortality_df["B01001_001E"].astype(float)

# Merge infant and maternal mortality DataFrames
merged_df = pd.merge(infant_mortality_df[['State', 'Infant Mortality Rate']], maternal_mortality_df[['State', 'Maternal Mortality Rate']], on='State')

# Display the merged DataFrame as a table
print("\nInfant and Maternal Mortality Rates:")
print(tabulate(merged_df, headers='keys', tablefmt='pretty'))


# In[4]:


# Fetch infant mortality data from Census API
infant_data = fetch_data_from_census_api(census_api_url, infant_variables)

# Convert the API response to a pandas DataFrame
if infant_data:
    infant_mortality_df = pd.DataFrame(infant_data[1:], columns=infant_data[0])

    # Calculate infant mortality rate
    infant_mortality_df["Mortality Rate"] = infant_mortality_df["B01001_011E"].astype(float) / infant_mortality_df["B01001_001E"].astype(float)

    # Plot infant mortality data
    plt.scatter(infant_mortality_df["Mortality Rate"], infant_mortality_df["Mortality Rate"], label="Infant Mortality", color="blue")

# Define variables for maternal mortality data
maternal_variables = {
    "get": "NAME,B01001_001E,B01001_012E",
    "for": "state:*"
}

# Fetch maternal mortality data from Census API
maternal_data = fetch_data_from_census_api(census_api_url, maternal_variables)

# Convert the API response to a pandas DataFrame
if maternal_data:
    maternal_mortality_df = pd.DataFrame(maternal_data[1:], columns=maternal_data[0])

    # Calculate maternal mortality rate
    maternal_mortality_df["Mortality Rate"] = maternal_mortality_df["B01001_012E"].astype(float) / maternal_mortality_df["B01001_001E"].astype(float)

    # Plot maternal mortality data
    plt.scatter(maternal_mortality_df["Mortality Rate"], maternal_mortality_df["Mortality Rate"], label="Maternal Mortality", color="red")

# Plot formatting
plt.xlabel("Rate")
plt.ylabel("Rate")
plt.title("Maternal and Infant Mortality Rates")
plt.legend()
plt.grid(True)

# Show plot
plt.show()


# ###### 

# In[13]:


# Combine the highest infant and maternal mortality data into a single DataFrame
combined_df = pd.merge(highest_infant_mortality, highest_maternal_mortality, on='NAME', suffixes=('_infant', '_maternal'))

# Plot bar graph for highest infant and maternal mortality rates
plt.figure(figsize=(12, 6))

# Set the width of the bars
bar_width = 0.35

# Set position of bar on X axis
r1 = np.arange(len(combined_df))
r2 = [x + bar_width for x in r1]

# Plot bars
plt.bar(r1, combined_df['Mortality Rate_infant'], color='skyblue', width=bar_width, edgecolor='grey', label='Infant Mortality Rate')
plt.bar(r2, combined_df['Mortality Rate_maternal'], color='salmon', width=bar_width, edgecolor='grey', label='Maternal Mortality Rate')

# Add xticks on the middle of the group bars
plt.xlabel('State', fontweight='bold')
plt.xticks([r + bar_width/2 for r in range(len(combined_df))], combined_df['NAME'], rotation=45, ha='right')

# Add ylabel
plt.ylabel('Mortality Rate', fontweight='bold')

# Add title
plt.title('Highest Infant and Maternal Mortality Rates by State')

# Add legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()


# In[14]:


# Combine the lowest infant and maternal mortality data into a single DataFrame
combined_df_lowest = pd.merge(lowest_infant_mortality, lowest_maternal_mortality, on='NAME', suffixes=('_infant', '_maternal'))

# Plot bar graph for lowest infant and maternal mortality rates
plt.figure(figsize=(12, 6))

# Set the width of the bars
bar_width = 0.35

# Set position of bar on X axis
r1 = np.arange(len(combined_df_lowest))
r2 = [x + bar_width for x in r1]

# Plot bars
plt.bar(r1, combined_df_lowest['Mortality Rate_infant'], color='skyblue', width=bar_width, edgecolor='grey', label='Infant Mortality Rate')
plt.bar(r2, combined_df_lowest['Mortality Rate_maternal'], color='salmon', width=bar_width, edgecolor='grey', label='Maternal Mortality Rate')

# Add xticks on the middle of the group bars
plt.xlabel('State', fontweight='bold')
plt.xticks([r + bar_width/2 for r in range(len(combined_df_lowest))], combined_df_lowest['NAME'], rotation=45, ha='right')

# Add ylabel
plt.ylabel('Mortality Rate', fontweight='bold')

# Add title
plt.title('Lowest Infant and Maternal Mortality Rates by State')

# Add legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()


# In[30]:


# Define Census API URL
census_api_url = "https://api.census.gov/data/2013/acs/acs5"

# Define variables for infant mortality data by race
infant_variables = {
    "get": "NAME,B01001_001E,B01001_002E,B01001_003E,B01001_004E,B01001_005E,B01001_006E",
    "for": "state:*"
}

# Fetch infant mortality data by race from Census API
infant_data_by_race = requests.get(census_api_url, params=infant_variables).json()

# Convert the API response to a pandas DataFrame
if infant_data_by_race:
    infant_mortality_race_df = pd.DataFrame(infant_data_by_race[1:], columns=infant_data_by_race[0])
    infant_mortality_race_df['State'] = infant_mortality_race_df['state'].map(state_mapping)
    infant_mortality_race_df['Total Population'] = infant_mortality_race_df['B01001_001E'].astype(int)
    infant_mortality_race_df['White'] = infant_mortality_race_df['B01001_002E'].astype(int)
    infant_mortality_race_df['Black or African American'] = infant_mortality_race_df['B01001_003E'].astype(int)
    infant_mortality_race_df['American Indian and Alaska Native'] = infant_mortality_race_df['B01001_004E'].astype(int)
    infant_mortality_race_df['Asian'] = infant_mortality_race_df['B01001_005E'].astype(int)
    infant_mortality_race_df['Native Hawaiian and Other Pacific Islander'] = infant_mortality_race_df['B01001_006E'].astype(int)

# Calculate infant mortality rates by race
infant_mortality_race_df['Infant Mortality Rate (White)'] = (infant_mortality_race_df['White'] / infant_mortality_race_df['Total Population']) * 1000
infant_mortality_race_df['Infant Mortality Rate (Black or African American)'] = (infant_mortality_race_df['Black or African American'] / infant_mortality_race_df['Total Population']) * 1000
infant_mortality_race_df['Infant Mortality Rate (American Indian and Alaska Native)'] = (infant_mortality_race_df['American Indian and Alaska Native'] / infant_mortality_race_df['Total Population']) * 1000
infant_mortality_race_df['Infant Mortality Rate (Asian)'] = (infant_mortality_race_df['Asian'] / infant_mortality_race_df['Total Population']) * 1000
infant_mortality_race_df['Infant Mortality Rate (Native Hawaiian and Other Pacific Islander)'] = (infant_mortality_race_df['Native Hawaiian and Other Pacific Islander'] / infant_mortality_race_df['Total Population']) * 1000

# Define variables for maternal mortality data by race
maternal_variables = {
    "get": "NAME,B01001_001E,B01001_007E,B01001_008E,B01001_009E,B01001_010E,B01001_011E",
    "for": "state:*"
}

# Fetch maternal mortality data by race from Census API
maternal_data_by_race = requests.get(census_api_url, params=maternal_variables).json()

# Convert the API response to a pandas DataFrame
if maternal_data_by_race:
    maternal_mortality_race_df = pd.DataFrame(maternal_data_by_race[1:], columns=maternal_data_by_race[0])
    maternal_mortality_race_df['State'] = maternal_mortality_race_df['state'].map(state_mapping)
    maternal_mortality_race_df['Total Population'] = maternal_mortality_race_df['B01001_001E'].astype(int)
    maternal_mortality_race_df['White'] = maternal_mortality_race_df['B01001_007E'].astype(int)
    maternal_mortality_race_df['Black or African American'] = maternal_mortality_race_df['B01001_008E'].astype(int)
    maternal_mortality_race_df['American Indian and Alaska Native'] = maternal_mortality_race_df['B01001_009E'].astype(int)
    maternal_mortality_race_df['Asian'] = maternal_mortality_race_df['B01001_010E'].astype(int)
    maternal_mortality_race_df['Native Hawaiian and Other Pacific Islander'] = maternal_mortality_race_df['B01001_011E'].astype(int)

# Calculate maternal mortality rates by race
maternal_mortality_race_df['Maternal Mortality Rate (White)'] = (maternal_mortality_race_df['White'] / maternal_mortality_race_df['Total Population']) * 1000
maternal_mortality_race_df['Maternal Mortality Rate (Black or African American)'] = (maternal_mortality_race_df['Black or African American'] / maternal_mortality_race_df['Total Population']) * 1000
maternal_mortality_race_df['Maternal Mortality Rate (American Indian and Alaska Native)'] = (maternal_mortality_race_df['American Indian and Alaska Native'] / maternal_mortality_race_df['Total Population']) * 1000
maternal_mortality_race_df['Maternal Mortality Rate (Asian)'] = (maternal_mortality_race_df['Asian'] / maternal_mortality_race_df['Total Population']) * 1000
maternal_mortality_race_df['Maternal Mortality Rate (Native Hawaiian and Other Pacific Islander)'] = (maternal_mortality_race_df['Native Hawaiian and Other Pacific Islander'] / maternal_mortality_race_df['Total Population']) * 1000

# Create a scatter plot for infant mortality rates by race
plt.figure(figsize=(10, 6))
plt.scatter(infant_mortality_race_df['Infant Mortality Rate (White)'], infant_mortality_race_df['Infant Mortality Rate (Black or African American)'], color='blue', label='Black or African American')
plt.scatter(infant_mortality_race_df['Infant Mortality Rate (White)'], infant_mortality_race_df['Infant Mortality Rate (American Indian and Alaska Native)'], color='red', label='American Indian and Alaska Native')
plt.scatter(infant_mortality_race_df['Infant Mortality Rate (White)'], infant_mortality_race_df['Infant Mortality Rate (Asian)'], color='green', label='Asian')
plt.scatter(infant_mortality_race_df['Infant Mortality Rate (White)'], infant_mortality_race_df['Infant Mortality Rate (Native Hawaiian and Other Pacific Islander)'], color='orange', label='Native Hawaiian and Other Pacific Islander')
plt.xlabel('Infant Mortality Rate (White)')
plt.ylabel('Infant Mortality Rate by Race')
plt.title('Infant Mortality Rates by Race')
plt.legend()
plt.grid(True)
plt.show()

# Create a scatter plot for maternal mortality rates by race
plt.figure(figsize=(10, 6))
plt.scatter(maternal_mortality_race_df['Maternal Mortality Rate (White)'], maternal_mortality_race_df['Maternal Mortality Rate (Black or African American)'], color='blue', label='Black or African American')
plt.scatter(maternal_mortality_race_df['Maternal Mortality Rate (White)'], maternal_mortality_race_df['Maternal Mortality Rate (American Indian and Alaska Native)'], color='red', label='American Indian and Alaska Native')
plt.scatter(maternal_mortality_race_df['Maternal Mortality Rate (White)'], maternal_mortality_race_df['Maternal Mortality Rate (Asian)'], color='green', label='Asian')
plt.scatter(maternal_mortality_race_df['Maternal Mortality Rate (White)'], maternal_mortality_race_df['Maternal Mortality Rate (Native Hawaiian and Other Pacific Islander)'], color='orange', label='Native Hawaiian and Other Pacific Islander')
plt.xlabel('Maternal Mortality Rate (White)')
plt.ylabel('Maternal Mortality Rate by Race')
plt.title('Maternal Mortality Rates by Race')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




