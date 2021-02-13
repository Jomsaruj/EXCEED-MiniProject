from flask import Flask, request
from flask_pymongo import PyMongo
import time

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo = PyMongo(app)

myCollection = mongo.db.g16

@app.route('')

@app.route('/create', methods=['POST'])
def insert_one():
    data = request.json
    myInsert = {
            "car_number": data["car_number"],
            ""
            "time_in": data["time_in"],
            "time_out": data["time_out"]
            }
    myCollection.insert_one(myInsert)
    return {'result': 'Created successfully'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50005', debug=True)
    
