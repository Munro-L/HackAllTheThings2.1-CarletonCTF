import requests
import json

session = requests.get("http://scoreboard.h4tt.ca:3002/api/get-endpoints")
print(session.content)
data = json.loads(session.content)

json.dumps(data, indent=4)
