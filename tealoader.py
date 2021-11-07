import pickle

def loadFromDataFile(dataFolder):
    with open(f"{dataFolder}/data.pkl", 'rb') as file:
        return pickle.load(file)
    
def saveToDataFile(tea_provider, dataFolder):
    with open(f"{dataFolder}/data.pkl", 'wb') as file:
        pickle.dump(tea_provider, file)