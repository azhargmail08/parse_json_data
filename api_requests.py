import requests

url = "https://data.gov.my/data-catalogue/births"

response = requests.get(url)

if response.status_code == 200:
    print("Success!")
    data = response.json()
else:
    print("Failed! Status code: ", response.status_code) 

print(data.keys())
print(data[0].keys())