from flask import Flask, jsonify, Response
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB URL
db = client["official_crime"]  # Replace with your database name
collection = db["test101"]  # Replace with your collection name

@app.route('/download_json', methods=['GET'])
def download_json():
    data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB _id field
    json_data = json.dumps(data, indent=4)  # Convert to JSON string

    response = Response(json_data, content_type="application/json")
    response.headers["Content-Disposition"] = "attachment; filename=data.json"  # Force download
    return response

if __name__ == '__main__':
    app.run(debug=True)
