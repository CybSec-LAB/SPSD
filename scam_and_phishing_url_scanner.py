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
#from tkinter import *
import requests
import urllib
import json

"""ws = Tk()
ws.title('SCAM SCANNER')
ws.geometry('400x300')

f = ('Times', 14)

left_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
    )

Label(
    left_frame,
    text="Link",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Link_tf = Entry(
    left_frame,
    font=f
    ) """



# simple_detector
url = input("Enter a url: ")
encoded_url = urllib.parse.quote(url, safe='')
api_url = "https://ipqualityscore.com/api/json/url/flO6UAmrHHJk513EmBItfxyrWkM9p2Kz/"
#strictness = input("choose 0-1:  ")
#additional_params = {'strictness': strictness}
response = requests.get(api_url + encoded_url + """additional_params""")

"""scan_btn = Button(
    left_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=encoded_url
    )"""


# viewing response
data = requests.get(api_url + encoded_url)
print(json.dumps(data.json(), indent=4))


# The user interface
"""Link_tf.grid(row=0, column=1, pady=10, padx=20)
scan_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.pack()

ws.mainloop()"""