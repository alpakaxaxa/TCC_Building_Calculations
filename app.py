from flask import Flask, render_template, redirect, url_for, request, make_response
from datetime import datetime
import json
import buildingInformation
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    cookieRecordUIDs = cookieGetRecordUIDs(request.cookies)
    buildingInformationData = buildingInformation.BuildingInformationData('data.json')
    records = buildingInformationData.buildingInformationRecords(cookieRecordUIDs)
    return render_template('view.html', records=records)

@app.route('/addRecord', methods=["POST"])
def addRecord():
    if request.method == "POST":
        buildingUsage = int(request.form['buildingUsage'])
        buildingType = int(request.form['buildingType'])
        buildingCubicMeters = int(request.form['buildingCubicMeters'])
        buildingConstructionType = int(request.form['buildingConstructionType'])
        buildingStandard = int(request.form['buildingStandard'])
        buildingTerrain = int(request.form['buildingTerrain'])
        buildingInformationData = buildingInformation.BuildingInformationData('data.json')
        uID = buildingInformationData.addRecord(buildingUsage, buildingType, buildingCubicMeters, buildingConstructionType, 
        buildingStandard, buildingTerrain)
        response = make_response(redirect(url_for('view')))
        response = cookieSet(response, request.cookies, uID)
        return response

def calculateValue(buildingCubicMeters, buildingType):
    multiplicator = 0
    if type == "house":
        multiplicator = 1.5
    elif type == "extension":
        multiplicator = 1
    elif type == "appartment":
        multiplicator = 0.8
    return buildingCubicMeters*1000*multiplicator

def cookieSet(response, cookiesDictionary, uID):
    timeStamp = str(datetime.now())
    cookies = []
    for key in cookiesDictionary:
        cookies.append(key)
        if len(cookies) == 3:
            cookies.sort()
            response.set_cookie(cookies[0], '', expires=0)
            break
    response.set_cookie(timeStamp, uID)
    return response

def cookieGetRecordUIDs(cookiesDictionary):
    cookieRecordUIDs = []
    cookies = []
    for key in cookiesDictionary:
        cookies.append(key)
    cookies.sort()
    for cookie in cookies:
        cookieRecordUIDs.append(cookiesDictionary[cookie])
    return cookieRecordUIDs


if __name__ == '__main__':
    app.run(debug=True)