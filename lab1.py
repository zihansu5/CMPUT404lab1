import requests
link = "http://google.com/"
reponse = requests.get(link)
print(reponse.content)
