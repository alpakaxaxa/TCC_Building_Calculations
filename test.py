from classes import BuildingInformationData, BuildingInformationData
import json

d = BuildingInformationData("./data.json")
d.addRecord(77, 'appartment')
print(d.buildingInformation())