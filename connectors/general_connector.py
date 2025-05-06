
# Write a Python Script that pulls paginated data from the public API: and 

# Fetches all posts 
# Saves them to CSV
# Retries on failure (max 3 times) 
# Logs errors to a file 

import requests 
import time 
import csv
import logging 

BASE_URL = "https://jsonplaceholder.typicode.com/posts"
HEADERS = {}
SLEEP_TIME = 1 
MAX_RETRIES = 3 

logging.basicConfig(filename='connector_errors.log', level = logging.WARNING)

def fetch_all_data():
  data = []
  page = 1 
  while True:
    url = f"{BASE_URL}?_page={page}" 
    for attempt in range(MAX_RETRIES + 1):
      try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 429:
          logging.warning("Rate limit hit. Sleeping before retry") 
          time.sleep(10)
          continue 
        response.raise_for_status()
        break  #break out of retry loop
      except requests.RequestException as e: 
        logging.warning(f"Attempt {attempt}: Error on Page {page}")
        if attempt == MAX_RETRIES:
          raise 
        time.sleep(2 ** attempt)

    page_data = response.json()
    if not page_data:
      break
    data.extend(page_data)
    page += 1
    time.sleep(SLEEP_TIME)
  return data 

def write_to_csv(data, file_path): 
  if not data: 
    return 
  with open(file_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames = data[0].keys())
    writer.writeheader()
    writer.writerows()


# Run 
all_data = fetch_all_data()
write_to_csv(all_data, "posts.csv")Help 
  

