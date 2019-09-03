from domain.Humidity import Humidity
from domain.Temperature import Temperature
from domain.Time import Time

class Controller:

    def __init__(self):
        self.temperatureList = []
        self.humidityList = []
        self.readInputs()


    def readInputs(self):
        f = open("input.in", "r")
        temps = f.readline().split(", ")
        for t in temps:
            self.temperatureList.append(int(t))

        humids = f.readline().split(", ")
        for h in humids:
            self.humidityList.append(int(h))

    def computeTime(self):
        result = []
        for i in range(0, len(self.temperatureList)):
            temperature = Temperature(self.temperatureList[i])
            humidity = Humidity(self.humidityList[i])
            time = Time(temperature, humidity)
            defuz = time.defuzzification()
            result.append(int(defuz))
            print("Humidity: " + str(self.humidityList[i]) + " Temperature: " + str(self.temperatureList[i]) + " Time: " + str(defuz))

        return result