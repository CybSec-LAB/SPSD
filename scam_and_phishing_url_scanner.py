"""
_________________________________
|            AUTHOR:            |
| By Solomon Nasara | Bughunter |
|   & Pentester at CYBSEC LAB   |
|-------------------------------|     """

# see README.md for requirements, specifications and usage !

""" A scanner for detecting malicious website i.e (scam websites, phishing links and malwares). 
Built by integrating the {IPQUALITYSCORE_api}, for ease of access and better availability. """


# required_imports
from tkinter import *
import requests
import urllib
import json

# simple_detection_code

url = input("Enter a url: ")
encoded_url = urllib.parse.quote(url, safe='')
api_url = "https://ipqualityscore.com/api/json/url/flO6UAmrHHJk513EmBItfxyrWkM9p2Kz/"
response = requests.get(api_url + encoded_url)


# viewing response
data = requests.get(api_url + encoded_url)
print(json.dumps(data.json(), indent=4))


# The user interface