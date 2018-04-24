# python 3 


"""

intro 

# working with geopy 
# https://github.com/geopy/geopy/issues/262


from geopy.geocoders import Nominatim
from urllib.request import Request

def get_geolocator():
    geolocator = Nominatim()

    requester = geolocator.urlopen

    def requester_hack(req, **kwargs):
        req = Request(url=req, headers=geolocator.headers)
        return requester(req, **kwargs)

    geolocator.urlopen = requester_hack

    return geolocator

>>>lat, lon = (50.7938380221, 4.34659512392835)
>>>#location = get_geolocator().reverse("50.7938380221, 4.34659512392835")
>>>location = get_geolocator().reverse("{},{}".format(lat,lon))
>>>address = location.address
>>>print (address)
>>> 143, Rue du Repos - Ruststraat, Uccle - Ukkel, Brussel-Hoofdstad - Bruxelles-Capitale, Région de Bruxelles-Capitale - Brussels Hoofdstedelijk Gewest, 1180, België / Belgique / Belgien


"""

def rev_geocoder_fixed(lat,lon):
    time.sleep(1)
    try:
        g = geocoder.google([lat,lon], method = 'reverse')
        address = g.json['address']
        #print (address)
        address = address.replace("'", "''")
    except:
        location = get_geolocator().reverse("{},{}".format(lat,lon))
        address = location.address
        #address=''
    return address


def run_r_geocoder(row):
    if row['multiple_cells_p'] == 1:
        addr = row['name']
    else:
        addr = rev_geocoder_fixed(row['lat'],row['lon'])
    print(addr)
    return addr




if __name__ == '__main__':
    df['address'] = df.apply(run_r_geocoder, axis=1)





