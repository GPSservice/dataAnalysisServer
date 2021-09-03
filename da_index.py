import json
import module.Kmeans as kf
import warnings
warnings.filterwarnings(action='ignore')

def indexFunction(reqData):
    order = reqData["orderSetting"]
    data = reqData["data"]

    if not checkInput(order, data):
        returnValue = {
            "statusCode": 400,
            "body": {"errorMessage": "requestError: orderSetting Error!!"}
        }
    else:
        returnValue = {
            "statusCode": 200,
            "body": kf.mainFunction(reqData)
        }
    
    return returnValue


def checkInput(order, data):
    sw = True
    for i in range(len(data)):
        if(order.keys() != data[i]["detailInfo"].keys()):
            sw = False
            break
    return sw