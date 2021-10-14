import requests
import datetime 
import json    

def route_call(coordinates):
    URL = 'http://router.project-osrm.org/route/v1/driving/'  
    for i in range(len(coordinates)):
        URL += coordinates[i]
        if(i != len(coordinates) - 1):
            URL += ';'
    r = requests.get(URL)
    return r.json()

def find_duration(data):
    seconds = data['routes'][0]['legs'][0]['duration']
    duration = datetime.timedelta(seconds=seconds)
    return duration


def api_nodes_call():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area["ISO3166-1"="CHE"][admin_level=2];
    (node["amenity"="charging_station"](area);
    );
    out center;
    """
    response = requests.get(overpass_url, 
                            params={'data': overpass_query})
    f = open('./stations.json' , 'a')
    f.write(str(response.json()))
    f.close()
    

api_nodes_call()

# The actual coordinates are reveresed from what we give to the function.

# print(str(find_duration(api_call(['13.388860,52.517037' , '13.397634,52.529407']))))

