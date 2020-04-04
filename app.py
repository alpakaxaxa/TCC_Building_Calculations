from flask import Flask, render_template, redirect, url_for, request, make_response
from datetime import datetime
import json
import buildingInformation
from buildingInformation import BuildingInformation
app = Flask(__name__)

@app.route('/')
def index():
    uID = request.args.get('uID')
    buildingInformationData = buildingInformation.BuildingInformationData('data.json')
    record = buildingInformationData.buildingInformationRecord(uID)
    return render_template('index.html', record=record)

@app.route('/view')
def view():
    cookieRecordUIDs = cookieGetRecordUIDs(request.cookies)
    buildingInformationData = buildingInformation.BuildingInformationData('data.json')
    records = buildingInformationData.buildingInformationRecords(cookieRecordUIDs)
    templateRecords = []
    for record in records:
        templateRecords.append(record.templateBuildingInformation())
    return render_template('view.html', records=templateRecords)

@app.route('/addRecord', methods=["POST"])
def addRecord():
    if request.method == "POST":
        buildingInformationData = buildingInformation.BuildingInformationData('data.json')
        uID = buildingInformationData.addRecord(int(request.form['buildingUsage']), int(request.form['buildingType']), 
        int(request.form['buildingCubicMeters']), int(request.form['buildingConstructionType']), 
        int(request.form['buildingStandard']), int(request.form['buildingTerrain']))
        response = make_response(redirect(url_for('view')))
        response = cookieSet(response, request.cookies, uID)
        return response

@app.route('/updateRecord', methods=["POST"])
def updateRecord():
    if request.method == "POST":
        buildingInformationData = buildingInformation.BuildingInformationData('data.json')
        uID = buildingInformationData.updateRecord(request.form['uID'], int(request.form['buildingUsage']), int(request.form['buildingType']), 
        int(request.form['buildingCubicMeters']), int(request.form['buildingConstructionType']), 
        int(request.form['buildingStandard']), int(request.form['buildingTerrain']))
        return make_response(redirect(url_for('view')))

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
    cookies.sort(reverse=True)
    print(cookies)
    for cookie in cookies:
        cookieRecordUIDs.append(cookiesDictionary[cookie])
    print(cookieRecordUIDs)
    return cookieRecordUIDs

if __name__ == '__main__':
    app.run(debug=True)

    
