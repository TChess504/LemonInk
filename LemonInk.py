#For scraping, stores data in data.json, sends the result back to main.js in a variable called data

#Import libraries
import pandas as pd
import numpy as np

import numpy as np
import json 
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


from flask import Flask, jsonify,request

from newspaper import Article
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd




#Goes to url
url = "https://www.dailymail.co.uk/news/article-13785465/The-real-reason-Prince-Harry-golden-ticket-diplomatic-visa-U-S-getting-green-card-financial-dagger-heart-Royal-Family.html"
print("hi")

#scrapes data
html = urlopen(url)
bsObj = BeautifulSoup(html, 'lxml')
print(bsObj.find("p").get_text())


divText = bsObj.find("body")
divText = divText.contents

for child in divText.children:
    if(child)
    print(child)

#puts data in JSON
print(divText)
with open('data.json', 'w', encoding='utf-8') as f:
  json.dump(str(divText), f, ensure_ascii=False, indent=4)


#Sending Data with Flask
app = Flask(__name__)


#testing material
@app.route('/receive_url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data['url']
    print(url)
    
    
    # Process the URL or perform any other actions with it
    # For example, print it
    print(f'Received URL: {url}')

    # You can send a response back if needed
    return jsonify({'message': 'URL received successfully'})


@app.route('/data', methods=['GET'])
def get_data():
    try:
      with open('data.json', 'r', encoding='utf-8') as f:
        news = f.read()
      
      dataPyVar = False
      if dataPyVar == False:
          data = jsonify({"message": "False"})
      else:
        data = jsonify({"message": "True"})
      data.headers.add('Access-Control-Allow-Origin', '*')
      return data
    except Exception as e:
        return jsonify({"error": str(e)}) 

if __name__ == '__main__':
    app.run(debug=True)


