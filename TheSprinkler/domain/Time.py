
class Time:

    def __init__(self, temp, humid):
        self.short = max(min(humid.wet, temp.verycold), min(humid.wet, temp.cold), min(humid.wet, temp.normal), min(humid.wet, temp.warm),  min(humid.normal, temp.verycold))
        self.medium = max(min(humid.wet, temp.hot), min(humid.normal, temp.cold), min(humid.normal, temp.warm), min(humid.normal, temp.normal), min(humid.dry, temp.verycold))
        self.long = max(min(humid.dry, temp.cold), min(humid.normal, temp.hot), min(humid.dry, temp.normal), min(humid.dry, temp.warm), min(humid.dry, temp.hot))


    def defuzzification(self):
        print("time with short: " + str(self.short) + " medium: " + str(self.medium) + " long: " + str(self.long))
        defuz = 0
        if self.short + self.medium + self.long > 0:
            defuz = (0 * self.short + 50 * self.medium + 100 * self.long)/ (self.short + self.medium + self.long)
        f = open("output.in", "a+")
        f.write("\n Defuzzificate: " + str(defuz))
        return defuz

