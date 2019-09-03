from domain.FuzzyBaseClass import FuzzyBaseClass

class Humidity(FuzzyBaseClass):

    def __init__(self, value):
        FuzzyBaseClass.__init__(self)
        self.dry = 0
        self.normal = 0
        self.wet = 0
        self.fuzzification(value)


    def fuzzification(self, val):
        self.dry = self.triangleMethod(val, 0, 0, 50)
        self.normal = self.triangleMethod(val, 0, 50, 100)
        self.wet = self.triangleMethod(val, 50, 100, 100)


