import requests
import sys
url = "https://raw.githubusercontent.com/zihansu5/CMPUT404lab1/master/lab1.py"
reponse = requests.get(url)
print("requests version:", requests.__version__)
print("python version:", sys.version)
print("contents:")
print(reponse.text)
