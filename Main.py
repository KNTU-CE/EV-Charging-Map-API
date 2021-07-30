import requests
import datetime      

def api_call(coordinates):
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

# The actual coordinates are reveresed from what we give to the function.

print(str(find_duration(api_call(['13.388860,52.517037' , '13.397634,52.529407']))))