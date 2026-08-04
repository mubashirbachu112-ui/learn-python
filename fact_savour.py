import requests
import datetime
import json

#fet a fact
response = requests.get("https://catfact.ninja/fact")
fact_data = response.json()
fact = fact_data["fact"]

#build a record with timestamp
record = {
    "fact": fact,
    "saved_at": str(datetime.datetime.now())
}

#save it to file
with open("cat_facts.json", "w") as file:
    json.dump(record,file)
print(f"saved:{fact}")