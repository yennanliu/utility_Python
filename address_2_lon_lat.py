# -*- coding: utf-8 -*-
# python 3 

"""
# ref 
# https://pypi.python.org/pypi/geopy
# https://github.com/yennanliu/web_scraping/blob/master/google_geodata/geopy_address_lon_lat.py

# todo : deal with geopy request limit 
# https://stackoverflow.com/questions/30108786/how-to-deal-with-geopys-query-limit
# install Nominatim on server 
# https://wiki.openstreetmap.org/wiki/Nominatim/Installation

# work around 
# https://www.shanelynn.ie/batch-geocoding-in-python-with-google-geocoding-api/


""" 
import numpy as np 
import time
import requests
import os 
from geopy.geocoders import Nominatim

# -------------------------------------------- 
# help function 




def split_lat(x):
    try:
        return x[0]
    except:
        return None 
    
def split_lon(x):
    try:
        return x[1]
    except:
        return None 


# work function 
# ------------- 


def run_hack(df):
    """
    df :
    id, address zipcode , lat lon 
    """
    pass 



# ref
# https://github.com/shanealynn/python_batch_geocode/blob/master/python_batch_geocoding.py
# https://www.shanelynn.ie/batch-geocoding-in-python-with-google-geocoding-api/
def get_google_results(address, api_key=None, return_full_response=False):
    """
    Get geocode results from Google Maps Geocoding API.
    
    Note, that in the case of multiple google geocode reuslts, this function returns details of the FIRST result.
    
    @param address: String address as accurate as possible. For Example "18 Grafton Street, Dublin, Ireland"
    @param api_key: String API key if present from google. 
                    If supplied, requests will use your allowance from the Google API. If not, you
                    will be limited to the free usage of 2500 requests per day.
    @param return_full_response: Boolean to indicate if you'd like to return the full response from google. This
                    is useful if you'd like additional location details for storage or parsing later.
    """
    # Set up your Geocoding url
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(address)
    if api_key is not None:
        geocode_url = geocode_url + "&key={}".format(api_key)
        
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    # Results will be in JSON format - convert to dict using requests functionality
    results = results.json()
    
    # if there's no results or an error, return empty results.
    if len(results['results']) == 0:
        output = {
            "formatted_address" : None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None
        }
    else:    
        answer = results['results'][0]
        output = {
            "formatted_address" : answer.get('formatted_address'),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
            "accuracy": answer.get('geometry').get('location_type'),
            "google_place_id": answer.get("place_id"),
            "type": ",".join(answer.get('types')),
            "postcode": ",".join([x['long_name'] for x in answer.get('address_components') 
                                  if 'postal_code' in x.get('types')])
        }
        
    # Append some other details:    
    output['input_string'] = address
    output['number_of_results'] = len(results['results'])
    output['status'] = results.get('status')
    if return_full_response is True:
        output['response'] = results
    
    return output




# -------------------------------------------- 


def address_2_lonlat(x):
    print (x)
    time.sleep(1)  # let's see if sleep 1 per epoch is OK for limitation 
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(x)
        print(location.latitude, location.longitude)
        return [location.latitude, location.longitude]
    except Exception as e:
        print (e)
        print ('fail to convert address to lon & lat ') 
        return [None,None]



def address_2_lonlat_hack(x):
    """
    in case frequent request would make script get block
    here is a mini hack : make script sleep until the API is able to response 
    then do the run again 
    """
    print (x)
    time.sleep(1)  # let's see if sleep 1 per epoch is OK for limitation 
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(x)
        print(location.latitude, location.longitude)
        return [location.latitude, location.longitude]
    except Exception as e:
        print (e)
        if str(e) == '[Errno 61] Connection refused':
            print ('meet API request limit, try again...')
            print ('sleep 1 min  ...')
            time.sleep(60)
            address_2_lonlat_hack(x)
        else:
            print ('fail to convert address to lon & lat ') 
        return [None,None]




    
    
    
def address_2_lonlat_hack_dev(x):
    """
    in case frequent request would make script get block
    here is a mini hack : make script sleep until the API is able to response 
    then do the run again 
    """
    print (x)
    time.sleep(1)  # let's see if sleep 1 per epoch is OK for limitation 
    # --------- API  1) GOOGLE MAP API 
    results= get_google_results(x)
    print ('google API results :' , results)
    if [results['latitude'], results['longitude']] != [None,None]:
        return [results['latitude'], results['longitude']] 
     # --------- API  2) GEOPY API 
    else:
        try:
            geolocator = Nominatim()
            location = geolocator.geocode(x, timeout=3)
            print(location.latitude, location.longitude)
            return [location.latitude, location.longitude]
        except Exception as e:
            print (e)
            if str(e) == '[Errno 61] Connection refused':
                print ('meet API request limit, try again...')
                print ('sleep 1 min  ...')
                time.sleep(60)
                address_2_lonlat_hack_dev(x)
            else:
                print ('fail to convert address to lon & lat ') 
            return [None,None]

    


# -------------------------------------------- 




