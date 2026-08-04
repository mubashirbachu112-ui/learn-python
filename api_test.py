import requests
try:
    response = requests.get("https://catfact.ninja/weee")
    if response.status_code == 200:
        data = response.json()
        print(f"Cat fact: {data['fact']}")
    else:
        print(f"API error.status code:{response.status_code}")
except requests.exceptions.RequestException:
    print("could not connect to internet")