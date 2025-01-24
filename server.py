from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/TEST", methods=["GET"])
def get():
    f = open('leaderboard.json')
    data = json.load(f)
    return data

@app.route("/TEST", methods=["POST"])
def post():
    print(json.loads(request.json)["data"])
    f = open('leaderboard.json')
    data = json.load(f)
    data["scores"].append(json.loads(request.json)["data"][0])
    data["names"].append(json.loads(request.json)["data"][1])
    with open("leaderboard.json", "w") as outfile:
        json.dump(data, outfile)
    return data["scores"] 

app.run() 
