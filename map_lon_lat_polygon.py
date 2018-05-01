# python 3 

import numpy as np
import pandas as pd 
import datetime as dt
import time
import json
from shapely.geometry import shape, Point


# help function

def combine_lng_lat(lng,lat):
    return str([float(lng),float(lat)])
    

def fetch_hz_name(geojson,lng_lat):
    """
    --- argument  ---
    
    geojson : a json file with geojson form  (e.g. : test.geo.json)
    x       : a set of geo-coordinates [lng, lat]
    
    --- argument  ---
    """
    # open hz geojson file and retrun as dict (python json object)
    with open('ldn_hz.geo.json') as f:
        js = json.load(f)
    # get point lon & lat 
    point = Point(float(lng_lat[0]), float(lng_lat[1]))
    # loop over all hz in the dict
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            print ('Found containing polygon:', feature['properties'])
        else:
            print ('none')

            
            
def fetch_hz_name_(geojson,lat,lon):
    """
    --- argument  ---
    
    geojson : a json file with geojson form  (e.g. : test.geo.json)
    x       : a set of geo-coordinates [lng, lat]
    
    --- argument  ---
    """
    # open hz geojson file and retrun as dict (python json object)
    with open(geojson) as f:
        js = json.load(f)
    # get point lon & lat 
    point = Point(float(lat), float(lon))
    print (point)
    # loop over all hz in the dict
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            print ('Found containing polygon:', feature['properties'])
            return str(feature['properties']['Name'])
        else:
            print ('none')
            pass
        
        

"""

# example 

# ----- run alltogether ------


df_trip = pd.read_csv('lon_lat_sample.csv')
df_trip_=df_trip.head(50)
df_trip_['lng_lat_']=df_trip_.apply(lambda row : pd.Series(combine_lng_lat(row['ride_start_long'],row['ride_start_lat']))  ,axis=1)
geojson='postcodes.geo.json'
df_trip_['hz'] = df_trip_.apply(lambda row : pd.Series(fetch_hz_name_(geojson,row['ride_start_long'],row['ride_start_lat']))  ,axis=1)


"""