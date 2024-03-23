#Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string


from flask import Flask, jsonify,request

from newspaper import Article
import json


def manual_testing(news):
  #Reading the fake data file in pandas
  data_fake = pd.read_csv('Fake.csv')
  data_fake.head()

  #Reading the true data file in pandas
  data_true = pd.read_csv('True.csv')
  data_true.head()

  #Assigning classes to the data
  data_fake["class"] = 0
  data_true["class"] = 1

  #Tells you the shape of the data in the csv files -> (rows, columns)
  data_fake.shape, data_true.shape

  #Manual testing of the datasets
  data_fake_manual_testing = data_fake.tail(10)
  for i in range(23480,23470,-1):
    data_fake.drop([i], axis = 0, inplace = True)

  data_true_manual_testing = data_true.tail(10)
  for i in range(21416,21406,-1):
    data_true.drop([i], axis = 0, inplace = True)

  #Assigning classes to the dataset
  data_fake_manual_testing['class'] = 0
  data_true_manual_testing['class'] = 1

  #Merging the datasets
  data_merge = pd.concat([data_fake, data_true], axis = 0)
  data_merge.head(10)

  #Dropping title, subject, and date columns
  data = data_merge.drop(['title','subject','date'], axis = 1)
  data.head(10)

  #Function to clean text...remove punctuation, put it all in lower case, etc
  def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

  #Applying the cleaning function to the text column and assigning X and Y
  data['text'] = data['text'].apply(wordopt)

  x = data['text']
  y = data['class']

  #Defining training and testing data, 75/25 split
  x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25)

  #Convert data into matrix
  from sklearn.feature_extraction.text import TfidfVectorizer

  vectorization = TfidfVectorizer()
  xv_train = vectorization.fit_transform(x_train)
  xv_test = vectorization.transform(x_test)

  #Creating first model
  from sklearn.linear_model import LogisticRegression

  LR = LogisticRegression()
  LR.fit(xv_train, y_train)

  #Model accuracy and classification report
  pred_lr = LR.predict(xv_test)
  LR.score(xv_test, y_test)
  print(classification_report(y_test, pred_lr))


  

  #Creating a second model
  from sklearn.tree import DecisionTreeClassifier

  DT = DecisionTreeClassifier()
  DT.fit(xv_train, y_train)

  #Checking model accuracy
  pred_dt = DT.predict(xv_test)
  DT.score(xv_test, y_test)
  print(classification_report(y_test, pred_dt))

  #Functions for Checking fake news
  def output_label(n):
    if n == 0:
      return "Fake News"
    elif n == 1:
      return "Not Fake News"

  testing_news = {"text":[news]}
  new_def_test = pd.DataFrame(testing_news)
  new_def_test["text"] = new_def_test["text"].apply(wordopt)
  new_x_test = new_def_test["text"]
  new_xv_test = vectorization.transform(new_x_test)
  pred_LR = LR.predict(new_xv_test)
  pred_DT = DT.predict(new_xv_test)
  print("\n\nLR Prediction: {} \nDT Prediction: {}".format(output_label(pred_LR[0]),output_label(pred_DT[0])))

  return str("LR Prediction: {}".format(output_label(pred_LR[0])))

def isNewsCredible(testing):
  if("LR Prediction: Fake News" == testing):
    return False
  return True
#Inputting a string to check if news is fake
print("Input News:")
news = str("This is 80 percent certain")
#credibleornot = isNewsCredible(manual_testing(news))
#print(credibleornot)


#data = credibleornot 

#Sending Data with Flask
app = Flask(__name__)

@app.route('/receive_url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data['url']
    
    article = Article(url)
    article.download()
    article.parse()

    with open('data.json', 'w', encoding='utf-8') as f:
      json.dump(article.text, f, ensure_ascii=False, indent=4)

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
      
      dataPyVar = isNewsCredible(manual_testing(news))
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
