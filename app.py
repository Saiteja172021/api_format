from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Update if using a remote DB
db = client["official_crime"]  # Replace with your database name
collection = db["test101"]  # Replace with your collection name

@app.route('/', methods=['GET'])  # Default route to check if API is running
def home():
    return jsonify({"message": "API is running!"})

@app.route('/get_data', methods=['GET'])  # Your API route
def get_data():
    data = list(collection.find({}, {"_id": 0}))  # Fetch data from MongoDB
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
