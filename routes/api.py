# import all the modules
from flask import Blueprint, jsonify
import json
from copy import deepcopy
import concurrent.futures

#import the data
from data import data

#import the function to get the data from url
from utils.fetchAll import fetchAll

# Register blueprint
api = Blueprint('rankyApi', __name__)

@api.route("/fetch", methods=["GET", "POST"])
def ranky():
    #Copy the data so the main data doesn't change
    jsonData = deepcopy(data)

    # Get the data from the online judges and replace the urls with that data
    executor = concurrent.futures.ProcessPoolExecutor()
    for i in range(jsonData.__len__()):
        #Create process and store the result
        fetcher = executor.submit(fetchAll, jsonData[i][3],jsonData[i][4],jsonData[i][5])
        result = fetcher.result()

        #Store the result into list
        jsonData[i][3] = result["toph"]
        jsonData[i][4] = result["dimik"]
        jsonData[i][5] = result["uri"]

        # Total score
        jsonData[i][0] = int(jsonData[i][3])+int(jsonData[i][4])+int(jsonData[i][5])

    # Sorting the data according to total score
    jsonData = sorted(jsonData, reverse=True)

    # Returning the data
    return jsonify(jsonData)
