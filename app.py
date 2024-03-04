# Import necessary libraries
from flask import Flask, jsonify, request
from pymongo import MongoClient
import requests
import json

# Create Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://db:27017/')
db = client['nytimes']

# Define API endpoint for most popular articles
@app.route('/mostpopular', methods=['GET'])
def most_popular():
    # Get API key
    api_key = 'enter your key
    '

    # Make API request
    url = f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)

    # Store data in MongoDB
    db.articles.insert_many(data['results'])

    # Return JSON data
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
