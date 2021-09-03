from flask import Flask, render_template, jsonify
import json
import da_index as DA
from module.DBconnect import PyDB

application = Flask(__name__)

###################### Main ######################
@application.route('/')
def home():
    return render_template("button.html")


###################### getJSON ######################
def dataClensing(getResult):
    data = []
    for gr in getResult:
        data.append({
            "location": {
                "latitude": gr["latitude"],
                "longitude": gr["longitude"]
            },
            "detailInfo": {
                "age": gr["age"],
                "gender": gr["gender"],
                "job": gr["job"],
                "salary": gr["salary"]
            }
        })
    return data

@application.route('/getJson')
def getJson():
    pydb = PyDB()
    selectQuery = "select * from location;"
    selectResult = pydb.select_query(selectQuery)
    inputJson = {
        "orderSetting": {
            "age": [
                "count"
            ],
            "gender": [
                "count"
            ],
            "job": [
                "count"
            ],
            "salary": [
                "sort",
                "rsort",
                "average"
            ]
        },
        "data": dataClensing(selectResult)
    }

    result = DA.indexFunction(inputJson)
    ### JSON파일로 저장 ###
    with open("./resultJSON.json", "w") as j:
        json.dump(result, j)
    
    return jsonify(result["statusCode"])


###################### JSON read ######################
@application.route('/jsonread')
def jsonRead():
    with open("./resultJSON.json", "r") as j:
        return json.dumps(json.load(j))


if __name__ == "__main__":
    application.run(debug=True)