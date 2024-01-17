import requests
url = "https://argus-keda-example.diamond.ac.uk"

for i in range(1000):
    with requests.get(url) as r:
        print(f"response: {r}, iteration: {i+1}")
