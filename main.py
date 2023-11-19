"""


"""

import json
import requests

def get_data(type_of_data):
    """
    This function is used to retrive data from the config.json file.

    Here we use the python json library to get the required data from the config.json file that is in the same directory as 
    this file is located in. 
    """

    with open('config.json', 'r') as file:
        data = json.load(file)
    return data[type_of_data]
    
def assemble_curl():
    """
    This function assembles the data for the request that is to be send to the server specified
    in the config.json file.
    
    """
    url = get_data('url')

    headers = {
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache', 
        'Accept': '*/*',
        'Authorization': get_data('auth'),
        'Sec-Fetch-Site': 'same-site',
        'Host': get_data('host'),
        'Accept-Language': 'en-GB,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Sec-Fetch-Mode': 'cors',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': get_data('origin'),
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
        'Referer': get_data('referer'),
        'Content-Length': '123',
        'Sec-Fetch-Dest': 'empty',
        'X-MWAPPS-CLIENTVERSION': '1.13.7-1614,enduserweb',
        'X-MWAPPS-CLIENT': 'enduserweb',
        'X-MWAPPS-APPID': get_data('app-id'),
    }

    data = {
        "partitionDate": 20231119,
        "userId": get_data('user-id'),
        "classId": get_data('class-id')
    }

    return url, headers, json.dumps(data)

def launch_request():
    """
    
    
    """
    url, headers, json_data = assemble_curl()

    response = requests.post(url, headers=headers, data=json_data)

    if response.status_code == 200:
        response_data = response.json()

        desired_data = response_data.get('key')  

        print("Desired Data:", desired_data)
    else:
        print("Request failed with status code:", response.status_code)
        print("Response Content:", response.text)
