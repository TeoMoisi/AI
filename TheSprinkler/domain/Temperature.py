from domain.FuzzyBaseClass import FuzzyBaseClass

class Temperature(FuzzyBaseClass):

    def __init__(self, value):
        FuzzyBaseClass.__init__(self)
        self.temps = {}
        self.verycold = 0
        self.cold = 0
        self.normal = 0
        self.warm = 0
        self.hot = 0
        self.fuzzification(value)


    def fuzzification(self, val):
        self.verycold = self.trapezoidMethod(val, -30, -30, -20, 5)
        self.cold = self.triangleMethod(val, -5, 0, 10)
        self.normal = self.trapezoidMethod(val, 5, 10, 15, 20)
        self.warm = self.triangleMethod(val, 15, 20, 25)
        self.hot = self.trapezoidMethod(val, 25, 30, 35, 35)


