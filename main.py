import config
import tea
import window
#import tealoader

def Initialise():
    conf = config.LoadConfig()
    tea_provider = LoadTea(conf.DataFolder)
    window.LoadWindow(tea_provider)

def LoadTea(dataFolder):
    tea_provider = tea.TeaCompanyProviderFactory()
    tea_provider.Provide("T2")
    tea_provider.Provide("Good & Proper Tea")
    tea_provider.Provide("Curious Tea")
    tea_provider.Provide("Tea pigs")
    return tea_provider
    #tea_provider.loadFromData(tealoader.loadFromDataFile(dataFolder))
    #print(tea_provider.companies)


if __name__ == "__main__":
    Initialise()