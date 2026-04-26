import requests    

res = requests.get("http://127.0.0.1:8000/")
data = res.json()

parsed = data['message']
for item in parsed:
    if 'pass' in item:
        print(item)
    