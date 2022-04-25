import numpy as np
import pandas as pd
from datetime import datetime


############################################################
# Choose an interesting dataset 
############################################################

city_csv = [
    "Banning.csv",
    "Central_Los_Angeles.csv",
    "Compton.csv",
    "Glendora.csv",
    "Lake_Elsinore.csv",
    "Mira_Loma.csv",
    "North_Hollywood.csv",
    "Reseda.csv",
    "SanBernardino.csv",
    "Santa_Clarita.csv",
    "Temecula.csv",
    "Upland.csv"
]

# find the city with the most days with values > 50
# (aka more pollution)
for city in city_csv:
    df1 = pd.read_csv("data/2021Q1Q2/" + city)
    df2 = pd.read_csv("data/2021Q3Q4/" + city)
    df = pd.concat([df1, df2])

    df = df[df['Value'] > 50]
    num_rows = df.shape[0]
    print(f"{city}:  num_rows is {num_rows}")

# Mira Loma has the most days with values > 50, so
# make a plot of pm2.5 levels in Mira Loma, CA during 2021.


############################################################
# Read data and make dataframe
############################################################

df1 = pd.read_csv("data/2021Q1Q2/Mira_Loma.csv")
df2 = pd.read_csv("data/2021Q3Q4/Mira_Loma.csv")
df = pd.concat([df1, df2])


############################################################
# Explore data
############################################################

#print(df.head(2))

#Date Time,Site Name,Value,Averaging Period,Units,
#California State Standard,
#National Ambient Air Quality Standard by U.S. EPA,
#1/1/2021 12:00:00 AM,Central San Bernardino Mountains,3,1-hr,µg/m3,
#N/A,N/A,

print(df.info())
num_rows = df.shape[0]
print(f"\nWe have {num_rows} rows, but expected {365 * 24} rows.\n")

# There are definitely some missing entries, since if you multiply 
# 365 x 24, then that is more than the number of rows we have.


############################################################
# Clean data
############################################################

# You can't have a negative number of Particulate Matter (PM 2.5).
# < 0 values don't make sense, so remove them.
df = df[df['Value']>=0]
print(f"{num_rows - df.shape[0]} rows were deleted.\n")

# updated number of rows
num_rows = df.shape[0]

max_value = max(df['Value'])
print(f"max value is {max_value}.\n")


# IN: date_str: "1/1/2021 12:00:00 AM"
# OUT: x,y: which coordinates that date is located on the image
def get_im_loc( date_str):
    dt = datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p")

    # convert from datetime to day of year (1..366)
    x = dt.timetuple().tm_yday - 1   # (0..365) 

    y = dt.hour
    #print(f"get_im_loc():   x is {x}   y is {y}")
    return x,y


# OUT: 24 rows, 365 col.  Each cell gets the PM2.5 value for the hour. 
def get_data():
    X = np.zeros([24,365])  # setup the structure and default values

    for i in range(num_rows):
        row = df.iloc[i]
        value = row['Value']
        date_str = row['Date Time']
        x, y = get_im_loc( date_str)
        X[y][x] = value

    return X


#IN: s: string: in "Jan 1, 2021" format
#OUT: the day of the year, that the string represents (1-366)
def convert_from_date_str_to_day_of_year( s):
    try:
        # convert from string to datetime object
        dt = datetime.strptime(s, '%b %d, %Y')

        # %j  is the day number of the year (1-366)
        day_of_year = int(dt.strftime('%j'))
        return day_of_year
    except ValueError as err:
        print(err)
        print("ValueError")
        print(f"convert_from_date_str_to_day_of_year( {s})")


