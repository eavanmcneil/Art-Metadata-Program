import requests
import json


base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
data =[]

# Loop through numbers from 1 to 491122
for ItemID in range(1, 1000):
    url = f"{base_url}{ItemID}"

    try:
        # Send GET request to fetch data from the URL
        response = requests.get(url)
        
        # If the request was successful (status code 200)
        if response.status_code == 200:
            rec = response.json()  # Parse the response as JSON
            # You can process the data here as needed
            print("Process:" + str(ItemID))
            data.append(rec)
        else:
            print(f"Failed to retrieve object {ItemID}. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"Error fetching object {ItemID}: {e}")

with open("ItemDatabase/ItemDatabase.json","w") as file:
    json.dump(data, file, indent=4)

print("Process: Done")
file.close()