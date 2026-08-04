import requests
import datetime
import json

#loading existing saved files
try:
    with open("facts.json", "r") as file:
        facts = json.load(file)
except FileNotFoundError:
    facts = []

#requesting cat fact
try:
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        new_fact = {
            "fact" : response.json()["fact"],
            "saved_at" : str(datetime.datetime.now())
        }
        facts.append(new_fact)
    else:
        print(f"API error : {response.status_code}")
except requests.exceptions.RequestException:
    print("could not connect.")

#save the whole list
with open("facts.json", "w") as file:
    json.dump(facts, file)

    #reporting total 

print(f"you now have : {len(facts)} facts saved")