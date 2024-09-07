#Import libraries
import pandas as pd
import numpy as np

import numpy as np
import json 
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string


from flask import Flask, jsonify,request

from newspaper import Article
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd





url = "https://www.dailymail.co.uk/news/article-13785465/The-real-reason-Prince-Harry-golden-ticket-diplomatic-visa-U-S-getting-green-card-financial-dagger-heart-Royal-Family.html"
print("hi")

html = urlopen(url)
bsObj = BeautifulSoup(html, 'lxml')
print(bsObj.find("p").get_text())


divText = bsObj.find("body")
divText = divText.contents

for child in divText.children:
    if(child)
    print(child)


print(divText)
with open('data.json', 'w', encoding='utf-8') as f:
  json.dump(str(divText), f, ensure_ascii=False, indent=4)


#Sending Data with Flask
app = Flask(__name__)

@app.route('/receive_url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data['url']
    print(url)
    #article = Article(url)
    #article.download()
    #article.parse()
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'lxml')
    print(bsObj.find("h1").get_text())
    print("hi")
    article = bsObj.find("article")
    divText = article.find("div", id="storytext")
    [a.extract() for a in divText.findAll("aside")]
    [d.extract() for d in divText.findAll("div")]
    print(divText.get_text())
    with open('data.json', 'w', encoding='utf-8') as f:
      json.dump(divText.get_text(), f, ensure_ascii=False, indent=4)

    with open('data.json', 'r', encoding='utf-8') as f:
      contents = f.read()

    
    
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


