import json
import uuid
import os

# Collection of BuildingInformation objects saved in local json file
class BuildingInformationData:
    def __init__(self, filePath):
        self.filePath = filePath
    # Check if file has content. Additional checks to be implemented
    def initFile(self):
        if os.stat(self.filePath).st_size == 0:
            with open(self.filePath, 'w') as file:
                jsonTemplate = {'data': {}}
                json.dump(jsonTemplate, file)
    # Return raw file data
    def fileData(self):
        fileContent = self.initFile()
        with open(self.filePath, 'r') as file:
            fileContent = json.load(file)
        return fileContent
    # Check record validity 
    def isValidRecord(self, buildingCubicMeters, buildingType):
        # implement check
        return True
    # Add building information user entry to the json file
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
    # Update existing record
    def updateRecord(self, uID, newBuildingUsage, newBuildingType, newBuildingCubicMeters, 
    newBuildingConstructionType, newBuildingStandard, newBuildingTerrain):
        if self.isValidRecord(newBuildingCubicMeters, newBuildingType): #add additional parameters
            fileContent = self.fileData()
            with open(self.filePath, 'w') as file:
                fileContent['data'][uID] = {'buildingUsage': newBuildingUsage, 'buildingType': newBuildingType, 
                'buildingCubicMeters': newBuildingCubicMeters, 'buildingConstructionType': newBuildingConstructionType, 
                'buildingStandard': newBuildingStandard, 'buildingTerrain': newBuildingTerrain}
                json.dump(fileContent, file)
            return uID
    # Find a building information record
    def buildingInformationRecord(self, uID):
        buildingInformationEntries = self.buildingInformation()
        buildingInformationRecord = None
        for buildingInformation in buildingInformationEntries:
            if buildingInformation.uID == uID:
                buildingInformationRecord = buildingInformation
                break
        return buildingInformationRecord
    # Return multiple building information records saved in json file
    def buildingInformationRecords(self, uIDList):
        buildingInformationRecords = []
        for uID in uIDList:
            buildingInformationRecords.append(self.buildingInformationRecord(uID))
        return buildingInformationRecords
    # Return all building information records saved in json file
    def buildingInformation(self):
        buildingInformationEntries = []
        fileContent = self.fileData()
        for k, v in fileContent['data'].items():
            b = BuildingInformation(k, v['buildingUsage'], v['buildingType'], v['buildingCubicMeters'], v['buildingConstructionType'], 
            v['buildingStandard'], v['buildingTerrain'])
            buildingInformationEntries.append(b)
        return buildingInformationEntries

# Class to manage and calculate price of buildings
class BuildingInformation:
    # Multipliers to calculate building prices (values are made up and don't make sense yet)
    USAGE = [1.3,1.1,0.9,0.7]
    TYPE = [1.3,0.8,1.1]
    PRICE_CUBIC_METERS = 70
    CONSTRUCTION_TYPE = [1,0.9,1.1]
    STANDARD = [0.8,1,1.2]
    TERRAIN = [1,1.3]
    
    def __init__(self, uID, buildingUsage, buildingType, buildingCubicMeters, 
    buildingConstructionType, buildingStandard, buildingTerrain):
        self.uID = uID
        self.buildingUsage = buildingUsage
        self.buildingType = buildingType
        self.buildingCubicMeters = buildingCubicMeters
        self.buildingConstructionType = buildingConstructionType
        self.buildingStandard = buildingStandard
        self.buildingTerrain = buildingTerrain
    # Calculation process is realistic but multipliers are made up
    def valueCalculate(self):
        cubic_meter_price = self.PRICE_CUBIC_METERS*self.buildingCubicMeters
        usage_mult = self.USAGE[self.buildingUsage-1]
        type_mult = self.TYPE[self.buildingType-1]
        construction_type_mult = self.CONSTRUCTION_TYPE[self.buildingConstructionType-1]
        standard_mult = self.STANDARD[self.buildingStandard-1]
        terrain_mult = self.TERRAIN[self.buildingTerrain-1]
        return cubic_meter_price*usage_mult*type_mult*construction_type_mult*standard_mult*terrain_mult
    # The name methods are convenience functions to transform integer values into corresponding template names
    def nameBuildingUsage(self):
        namesBuildingUsage = ["Family house", "Multi family house (3-4 Units)", "Multi generation house", "Multi family house (6-12 units)"]
        return namesBuildingUsage[self.buildingUsage-1]
    
    def nameBuildingType(self):
        namesBuildingType = ["New building", "Conversion", "Extension"]
        return namesBuildingType[self.buildingType-1]
    
    def nameBuildingConstructionType(self):
        namesBuildingConstructionType = ["Solid construction", "Timber construction", "Steel construction"]
        return namesBuildingConstructionType[self.buildingConstructionType-1]
    
    def nameBuildingStandard(self):
        namesBuildingStandard = ["Low", "Medium", "High"]
        return namesBuildingStandard[self.buildingStandard-1]

    def nameBuildingTerrain(self):
        namesBuildingTerrain = ["Flat", "Hillside"]
        return namesBuildingTerrain[self.buildingTerrain-1]
    # Return dictionary to display class in template
    def templateBuildingInformation(self):
        return {"uID": self.uID, "buildingUsage": self.nameBuildingUsage(),
        "buildingType": self.nameBuildingType(), "buildingCubicMeters": self.buildingCubicMeters, 
        "buildingConstructionType": self.nameBuildingConstructionType(), "buildingStandard": self.nameBuildingStandard(), 
        "buildingTerrain": self.nameBuildingTerrain(), "buildingValue": "CHF {:,.2f}".format(self.valueCalculate())}


    def __str__(self):
        return 'BuildingInformation(uID: '+str(self.uID)+', buildingType: '+ self.buildingType + ')'
    
