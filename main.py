import config
import window
#import tea
import tealoader

def Initialise():
    conf = config.LoadConfig()
    tea_provider = LoadTea(conf.DataFolder)
    window.LoadWindow(tea_provider)

def LoadTea(dataFolder):
    #tea_provider = tea.TeaCompanyProviderFactory()
    #company1 = tea_provider.Provide("T2")
    #company1.addTea(tea.Tea("Creme brulee", 7))
    #company1.addTea(tea.Tea("Melborne Breakfast", 9.5))
    #company2 = tea_provider.Provide("Good & Proper Tea")
    #company2.addTea(tea.Tea("Darjeeling 2nd flush", 9))
    #company2.addTea(tea.Tea("Iron Buddha", 8))
    #company3 = tea_provider.Provide("Curious Tea")
    #company3.addTea(tea.Tea("Gui Fei Oolong", 9))
    #company3.addTea(tea.Tea("Nu Er Huan Jasmine Girl Rings", 9.5))
    #tealoader.saveToDataFile(tea_provider, dataFolder)
    return tealoader.loadFromDataFile(dataFolder)
    #tea_provider.loadFromData(tealoader.loadFromDataFile(dataFolder))
    #print(tea_provider.companies)
    #return tea_provider

if __name__ == "__main__":
    Initialise()