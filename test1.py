from flask import Flask, request
from flask_pymongo import PyMongo
import time

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo = PyMongo(app)

myCollection = mongo.db.g16

@app.route('')

@app.route('/store', methods=['GET'])
def find():
    flit = {"time_out": None}
    query = myCollection.find(flit)
    output = [{0:0},{1:0},{2:0},{3,0}]
    for ele in query:
        output[ele["slot_number"]] = 1
    return { "result": output }

@app.route('/addcar', methods=['POST'])
def insert_one():
    data = request.json
    myInsert = {
            "type": "car",
            "slot_number" : data["No"],
            "time_in": time.time(),
            "time_out": None
            }
    myCollection.insert_one(myInsert)
    return {'result': 'Created successfully'}

@app.route('/addcar', methods=[''])
def insert_one():
    data = request.json
    myInsert = {
            "type": "car",
            "slot_number" : data["No"],
            "time_in": time.time(),
            "time_out": None
            }
    myCollection.insert_one(myInsert)
    return {'result': 'Created successfully'}
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50005', debug=True)
    