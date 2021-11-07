class TeaCompanyProviderFactory:
    def __init__(self):
        self.companies = {}
        
    #def loadFromData(self, companies):
    #    self.companies = companies

    def Provide(self, name):
        if name not in self.companies:
            self.companies[name] = TeaCompany(name)
        return self.companies[name]

class TeaCompany:
    def __init__(self, name):
        self.name = name
        self.teas = []
    
    def addTea(self, tea):
        if tea.name not in [t.name for t in self.teas]:
            self.teas.append(tea)

class Tea:
    def __init__(self, name, score):
        self.name = name
        self.score = score