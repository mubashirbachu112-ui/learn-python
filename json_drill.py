import requests
response = requests.get("https://api.github.com/users/mubashirbachu112-ui")
data = response.json()
print (f"username : {data['login']}")
print (f"public_repos : {data['public_repos']}")
print (f"followers : {data['followers']}")

joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
print (f"setup:{joke['setup']}")
print(f"punchline:{joke['punchline']}")

import json

data = {
    "user" : "mubashir",
    "repos": [
        {"name" : "learn-python", "stars" : 3},
        {"name" : "uigen", "stars": 7}
    ]
}

print(data["user"])
print(data["repos"][0]["name"])
print(data["repos"][1]["stars"])