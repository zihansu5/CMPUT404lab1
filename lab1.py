import requests
url = "https://raw.githubusercontent.com/zihansu5/CMPUT404lab1/master/lab1.py"
reponse = requests.get(url)
print(reponse.text)
