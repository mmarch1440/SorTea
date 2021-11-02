import jsonloader as jl

def loadFromDataFile(dataFolder):
    return jl.loadFromJson(dataFolder + "teacompanies.json")