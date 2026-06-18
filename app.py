from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

api = os.getenv("API_KEY")
app = Flask(__name__)

categories = ["technology", "business", "sports", "entertainment", "health"]


@app.route("/", methods = ["GET"])

def index():
    category = request.args.get("category", "technology")
    search = request.args.get("search", "")
    if search:
        url = "https://api.currentsapi.services/v1/search"
        params = {
            "apiKey": api,
            "keywords": search,
            "language": "en"
        }
    else:
        url = "https://api.currentsapi.services/v1/latest-news"
        params = {
            "apiKey": api,
            "category": category,
            "language": "en"
        }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    articles = data["news"]
    for article in articles:
        try:
            dt = datetime.strptime(article['published'], '%Y-%m-%d %H:%M:%S %z')
            article['published'] = dt.strftime('%b %d, %Y')
        except:
            pass
    print("Number of articles:", len(data["news"]))
    return render_template("index.html", articles=articles, categories=categories, selected_category=category,search=search)

if __name__ == '__main__':
    app.run(debug=True)





