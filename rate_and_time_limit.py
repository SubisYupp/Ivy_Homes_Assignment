# so to determine the rate limit and the time required to reset the rate limit , I have written a python script that sends requests to the API and checks the response status code. If the response status code is 429, it means the rate limit is reached. The script then waits for 5 seconds and sends a test request to check if the rate limit is reset. If the test request is successful, it calculates the time taken to reset the rate limit. The script continues to send requests until the rate limit is reached.

import requests
import time


url = "http://35.200.185.69:8000/v2/autocomplete?query=a"
count = 0  # this stores the number of requests
rate_limit_start_time = None  # it tracks the time when rate limit is reached so that we can calculate the reset time

while True:
    response = requests.get(url)
    count += 1
    
    if response.status_code == 200:
        print(f"Request {count}: Success")
    elif response.status_code == 429:
        print(f"Request {count}: Rate limit reached! API returned 429 Too Many Requests.")
        rate_limit_start_time = time.time()  #this captures the time when rate limit is reached
        
        while True:
            time.sleep(5)  # this restarts the request after 5 seconds
            test_response = requests.get(url)  # this sends a test request to check if rate limit is reset
            
            if test_response.status_code != 429:  # this checks if API allows to request again
                reset_time = time.time() - rate_limit_start_time
                print(f"Rate limit reset after {reset_time:.2f} seconds.")
                break 
    else:
        print(f"Request {count}: Unexpected error {response.status_code}")
    
    time.sleep(0.2)
