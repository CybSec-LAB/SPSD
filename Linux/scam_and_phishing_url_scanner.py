
# Required Imports
import json
import urllib
import requests




# simple_detector
url = input("Enter a url: ")
encoded_url = urllib.parse.quote(url, safe='')
api_url = "https://ipqualityscore.com/api/json/url/flO6UAmrHHJk513EmBItfxyrWkM9p2Kz/"
#strictness = input("choose 0-1:  ")

#additional_params = {'strictness': strictness}

response = requests.get(api_url + encoded_url + """additional_params""")


# viewing response
data = requests.get(api_url + encoded_url)
print(json.dumps(data.json(), indent=4))



# MESSAGE
print(" Hope you got your intel")
print("IuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuI\n"
      "I       MALICIOUS URL SCANNER            I\n"
      "I              V-1.0.0                   I\n"       
      "IuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuI")

input("  \n     \nPress Any Key to Quit")
