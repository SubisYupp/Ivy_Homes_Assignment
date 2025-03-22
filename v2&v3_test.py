import time
import requests

"""so our base logic for the code is to get the names form the API but the main problem in that the number of combinations 
is greater than the rate limit so we need to wait for the rate limit to reset so what we do is since we have determined 
the rate limit reset time before we can rerequest again after the rate limit is reset and till that time the operations 
are paused and we use two variables for it current_request_count and total_requests , current_request_count is used to 
keep track of the number of requests made before hitting the rate limit and total_requests is used to keep track of the 
total number of requests made till now and we also have a set DistinctNames to store the unique names and a list 
AllNames to store all the names including duplicates"""

version = "v2" #change it to v2 or v3  
rate_limits = {"v1": 100, "v2": 50, "v3": 80} 
reset_times = {"v1": 16, "v2": 39, "v3": 27}  

rate_limit = rate_limits[version] 
reset_time = reset_times[version] 

# this includes all possible base characters that give results when requested as single or paired with any other character
characters = "abcdefghijklmnopqrstuvwxyz0123456789#&+"

url = f"http://35.200.185.69:8000/{version}/autocomplete?query={{}}"

DistinctNames = set()  # this stores  unique names as some are repeated
AllNames = []  # this stores all including duplicates

total_requests = 0  # this tracks total requests
current_request_count = 0  # this tracks requests before hitting rate limit

for char in characters:
    queries = [char] + [char + other for other in characters]  # this generates queries: 'a', 'aa', 'ab', 'ac', ...
    
    for query in queries:
        if current_request_count >= rate_limit:  # check rate limit
            print(f"Rate limit reached for {version}. Pausing for {reset_time} seconds...")
            total_requests += current_request_count  # add to total requests
            current_request_count = 0  # reset current count
            time.sleep(reset_time)  # wait for rate limit to reset
        
        try:
            response = requests.get(url.format(query))
            current_request_count += 1  # increment current request count
            
            if response.status_code == 200:
                data = response.json()
                if 'results' in data and data['results']:  # ensure 'results' is not empty
                    DistinctNames.update(data['results'])
                    AllNames.extend(data['results'])
                print(f"Query '{query}' returned: {data['results'] if 'results' in data else 'No results'}")
            else:
                print(f"Error {response.status_code} for query '{query}'")
        except Exception as e:
            print("Request failed", e)
            time.sleep(1)  # small delay before retrying

# add remaining requests to total count
total_requests += current_request_count

print(f"Total requests made: {total_requests}")
print(f"Total unique names collected: {len(DistinctNames)}")
print(f"Total names collected (including duplicates): {len(AllNames)}")
