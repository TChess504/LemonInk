from newspaper import Article
import json
from flask import Flask, jsonify, request

my_variable = "https://omaha.com/life-entertainment/local/wellness/investigating-rabies-a-dead-kitten-in-omaha-triggers-sweeping-multi-agency-response/article_ec363bfa-7361-11ee-ba8f-eb06400ec53c.html"
article = Article(my_variable)
article.download()
article.parse()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(article.text, f, ensure_ascii=False, indent=4)

with open('data.json', 'r', encoding='utf-8') as f:
    contents = f.read()

print(contents)