from flask import Flask, render_template, redirect, url_for, request, make_response
from datetime import datetime
import buildingInformation
app = Flask(__name__)

# Initial building information form is displayed here
@app.route('/')
def index():
    uID = request.args.get('uID')
    buildingInformationData = buildingInformation.BuildingInformationData('data.json')
    record = buildingInformationData.buildingInformationRecord(uID)
    return render_template('index.html', record=record)

# Shows the last 3 records added by the user
@app.route('/view')
def view():
    cookieRecordUIDs = cookieGetRecordUIDs(request.cookies)
    buildingInformationData = buildingInformation.BuildingInformationData('data.json')
    records = buildingInformationData.buildingInformationRecords(cookieRecordUIDs)
    templateRecords = [] 
    for record in records:
        templateRecords.append(record.templateBuildingInformation())
    return render_template('view.html', records=templateRecords)

# Route for adding new records
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

# Route for updating existing records
@app.route('/updateRecord', methods=["POST"])
def updateRecord():
    if request.method == "POST":
        buildingInformationData = buildingInformation.BuildingInformationData('data.json')
        uID = buildingInformationData.updateRecord(request.form['uID'], int(request.form['buildingUsage']), int(request.form['buildingType']), 
        int(request.form['buildingCubicMeters']), int(request.form['buildingConstructionType']), 
        int(request.form['buildingStandard']), int(request.form['buildingTerrain']))
        return make_response(redirect(url_for('view')))

# Set a cookie in order to associate records with its respective user/author
def cookieSet(response, cookiesDictionary, uID):
    timeStamp = str(datetime.now())
    cookies = []
    for key in cookiesDictionary:
        cookies.append(key)
        if len(cookies) == 3:
            # Sort the array in order to delete the oldest entry (as default sorting is ascending and oldest timestamp has the lowest value)
            cookies.sort()
            response.set_cookie(cookies[0], '', expires=0)
            break
    response.set_cookie(timeStamp, uID)
    return response

# Fetch records based on user cookies
def cookieGetRecordUIDs(cookiesDictionary):
    cookieRecordUIDs = []
    cookies = []
    for key in cookiesDictionary:
        cookies.append(key)
    cookies.sort(reverse=True)
    for cookie in cookies:
        cookieRecordUIDs.append(cookiesDictionary[cookie])
    return cookieRecordUIDs

if __name__ == '__main__':
    app.run(debug=True)

    
