from flask import Flask, render_template
import json
import da_index as DA
from module.DBconnect import PyDB

application = Flask(__name__)

@application.route('/')
def home():
    return render_template("button.html")


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
    return result

if __name__ == "__main__":
    application.run(debug=True)