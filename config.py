# Config for the project [import in all files]

# Input filename
filename = 'Motor_Vehicle_Collisions_-_Crashes.csv'
# Cleaned filename
clean_filename = 'Motor_Vehicle_Collisions_-_Crashes_Cleaned.csv'

# Index column
index_col = 'COLLISION_ID'

# Data types for the columns in the data
dtypes = {
    'CRASH DATE' : 'str',
    'CRASH TIME' : 'str',
    'BOROUGH' : 'str',
    'ZIP CODE' : 'str',
    'LATITUDE' : 'float64',
    'LONGITUDE' : 'float64',
    'LOCATION' : 'object',
    'ON STREET NAME' : 'str',
    'CROSS STREET NAME' : 'str',
    'OFF STREET NAME' : 'str',
    'NUMBER OF PERSONS INJURED' : 'float64',
    'NUMBER OF PERSONS KILLED' : 'float64',
    'NUMBER OF PEDESTRIANS INJURED' : 'float64',
    'NUMBER OF PEDESTRIANS KILLED' : 'float64',
    'NUMBER OF CYCLIST INJURED' : 'float64',
    'NUMBER OF CYCLIST KILLED' : 'float64',
    'NUMBER OF MOTORIST INJURED' : 'float64',
    'NUMBER OF MOTORIST KILLED' : 'float64',
    'CONTRIBUTING FACTOR VEHICLE 1' : 'str',
    'CONTRIBUTING FACTOR VEHICLE 2' : 'str',
    'CONTRIBUTING FACTOR VEHICLE 3' : 'str',
    'CONTRIBUTING FACTOR VEHICLE 4' : 'str',
    'CONTRIBUTING FACTOR VEHICLE 5' : 'str',
    'COLLISION_ID' : 'int64',
    'VEHICLE TYPE CODE 1' : 'category',
    'VEHICLE TYPE CODE 2' : 'category',
    'VEHICLE TYPE CODE 3' : 'category',
    'VEHICLE TYPE CODE 4' : 'category',
    'VEHICLE TYPE CODE 5' : 'category'
}

# Column-wise replacement values for NA
na_replace = {
    'BOROUGH' : 'UNKNOWN',
    'ZIP CODE' : 'UNKNOWN',
    'LATITUDE' : 0,
    'LONGITUDE' : 0,
    'LOCATION' : '(0.0, 0.0)',
    'ON STREET NAME' : '',
    'CROSS STREET NAME' : '',
    'OFF STREET NAME' : '',
    'NUMBER OF PERSONS INJURED' : 0,
    'NUMBER OF PERSONS KILLED' : 0,
    'NUMBER OF PEDESTRIANS INJURED' : 0,
    'NUMBER OF PEDESTRIANS KILLED' : 0,
    'NUMBER OF CYCLIST INJURED' : 0,
    'NUMBER OF CYCLIST KILLED' : 0,
    'NUMBER OF MOTORIST INJURED' : 0,
    'NUMBER OF MOTORIST KILLED' : 0,
    'CONTRIBUTING FACTOR VEHICLE 1' : '',
    'CONTRIBUTING FACTOR VEHICLE 2' : '',
    'CONTRIBUTING FACTOR VEHICLE 3' : '',
    'CONTRIBUTING FACTOR VEHICLE 4' : '',
    'CONTRIBUTING FACTOR VEHICLE 5' : '',
    'VEHICLE TYPE CODE 1' : '',
    'VEHICLE TYPE CODE 2' : '',
    'VEHICLE TYPE CODE 3' : '',
    'VEHICLE TYPE CODE 4' : '',
    'VEHICLE TYPE CODE 5' : ''
}