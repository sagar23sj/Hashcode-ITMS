import requests
import json
from pprint import pprint


#res=requests.get('https://traffic.api.here.com/traffic/6.1/flow.json?bbox=51.5082%2C-0.1285%3B51.5062%2C-0.1265&app_id=KK3hHiZmChGu21AcuEVn&app_code=tjqvZvXK0z_PiRTCSgSiXg')
res=requests.get('https://traffic.api.here.com/traffic/6.1/flow.json?bbox=51.516463%2C-0.130435%3B51.516419%2C-0.130349&app_id=KK3hHiZmChGu21AcuEVn&app_code=tjqvZvXK0z_PiRTCSgSiXg')
#img=requests.get('https://image.maps.api.here.com/mia/1.6/mapview?app_id={YOUR_APP_ID}&app_code={YOUR_APP_CODE}&bbox=13.235732,14.761452,70.239879,78.123132')
print(res)

def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jsonobj = res.json()
pprint(jsonobj)

# recursivejson.py

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results



#cur_tmc_de = jsonobj['RWS'][0]['RW'][0]['FIS'][0]['FI'][0]['TMC']['DE']
#cur_flow = jsonobj['RWS'][0]['RW'][0]['FIS'][0]['FI'][0]['CF']

#print(cur_tmc_de, cur_flow)
