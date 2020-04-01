import json
import uuid
import os

class BuildingInformationData:
    def __init__(self, filePath):
        self.filePath = filePath
    def initFile(self):
        if os.stat(self.filePath).st_size == 0:
            with open(self.filePath, 'w') as file:
                jsonTemplate = {'data': {}}
                json.dump(jsonTemplate, file)
        
    def fileData(self):
        fileContent = self.initFile()
        with open(self.filePath, 'r') as file:
            fileContent = json.load(file)
        return fileContent

    def isValidRecord(self, buildingCubicMeters, buildingType):
        # implement check
        return True

    def addRecord(self, buildingUsage, buildingType, buildingCubicMeters, buildingConstructionType, buildingStandard, buildingTerrain):
        if self.isValidRecord(buildingCubicMeters, buildingType): #add additional parameters
            fileContent = self.fileData()
            uID = str(uuid.uuid1())
            with open(self.filePath, 'w') as file:
                fileContent['data'][uID] = {'buildingUsage': buildingUsage, 'buildingType': buildingType, 
                'buildingCubicMeters': buildingCubicMeters, 'buildingConstructionType':buildingConstructionType, 
                'buildingStandard':buildingStandard, 'buildingTerrain': buildingTerrain}
                json.dump(fileContent, file)
            return uID

    def buildingInformationRecord(self, uID):
        buildingInformationEntries = self.buildingInformation()
        buildingInformationRecord = None
        for buildingInformation in buildingInformationEntries:
            if buildingInformation.uID == uID:
                buildingInformationRecord = buildingInformation
                break
        return buildingInformationRecord

    def buildingInformationRecords(self, uIDList):
        buildingInformationRecords = []
        for uID in uIDList:
            buildingInformationRecords.append(self.buildingInformationRecord(uID))
        return buildingInformationRecords

    def buildingInformation(self):
        buildingInformationEntries = []
        fileContent = self.fileData()
        for k, v in fileContent['data'].items():
            b = BuildingInformation(k, v['buildingUsage'], v['buildingType'], v['buildingCubicMeters'], v['buildingConstructionType'], 
            v['buildingStandard'], v['buildingTerrain'])
            buildingInformationEntries.append(b)
        return buildingInformationEntries

    def value(self):
        return "1000"

class BuildingInformation:
    def __init__(self, uID, buildingUsage, buildingType, buildingCubicMeters, 
    buildingConstructionType, buildingStandard, buildingTerrain):
        self.uID = uID
        self.buildingUsage = buildingUsage
        self.buildingType = buildingType
        self.buildingCubicMeters = buildingCubicMeters
        self.buildingConstructionType = buildingConstructionType
        self.buildingStandard = buildingStandard
        self.buildingTerrain = buildingTerrain

    def calculateValue(self):
        return 
    
    def __str__(self):
        return 'BuildingInformation(uID: '+str(self.uID)+', buildingType: '+ self.buildingType + ')'
    
