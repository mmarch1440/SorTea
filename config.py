import jsonloader as jl

def LoadConfig():
    config = jl.loadFromJson("config.json")
    return Config(**config)

class Config:
    def __init__(self, dataFolder):
        self.DataFolder = dataFolder
