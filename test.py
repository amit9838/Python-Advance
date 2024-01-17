# if not isinstance(local_time, str):
#     print(f"Local time in {timezone_name}: {local_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
# else:
#     print(local_time)

# https://timezonefinder.michelfe.it/api_guide
import json
sunrise = 1704974944
sunset = 1705013287
latitude = "25.18"
longitude = "75.83"
latitude = "25.77"
longitude = "-80.19"
mode = "1"
# url = f"http://timezonefinder.michelfe.it/api/3_{longitude}_{latitude}"
from datetime import datetime

# 5:30 : 19800

import time
from datetime import datetime, timedelta

def get_timezone_offset():
    try:
        # Get the current time in UTC
        utc_now = datetime.utcnow()

        # Get the local time
        local_now = datetime.now()

        # Calculate the time difference between local time and UTC
        offset =  utc_now - local_now 

        # Convert the offset to seconds
        offset_seconds = int(offset.total_seconds())

        return offset_seconds
    except Exception as e:
        return f"Error: {str(e)}"


import requests
def get_epoch_offset(lat,lon):
    url = f"https://api.geotimezone.com/public/timezone?latitude={lat}&longitude={lon}"

    res = requests.get(url)
    if res.status_code != 200:
        return 0
    
    res = json.loads(res.text)
    if res.get("offset") is None:
        return 0
    
    offset_arr = res.get("offset")[3:].split(":")
    offset_arr = [int(x) for x in offset_arr]
    epoch_hr = abs(offset_arr[0])*3600
    epoch_s = 0
    
    print(offset_arr)
    if len(offset_arr) > 1:
        epoch_s = offset_arr[1]*60
        
    epoch_offset = epoch_hr+epoch_s

    if offset_arr[0] < 0:
        epoch_offset *= -1
    
    return epoch_offset

# res = get_epoch_offset(latitude,longitude)

# # print(res)

# # Example usage
# timezone_offset = get_timezone_offset()


# utc_time = sunrise - timezone_offset + res

# date_ = (datetime.fromtimestamp(utc_time).strftime("%I:%M %p"))
# print(date_)

print(get_timezone_offset())


