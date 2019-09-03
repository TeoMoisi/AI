from copy import deepcopy

from Domain.State import State


class Problem:

    def __init__(self, oprds, result, op):
        self._op = op
        self._oprds = oprds
        self._result = result
        self._keys = result
        for i in range(0, len(oprds)):
            self._keys = list(set().union(oprds[i], self._keys))
        self._initialConf = dict.fromkeys(self._keys, 0)
        self._state = State(self._keys, list(self._initialConf.values()), self._oprds, self._result)

    # def get_first(self):
    #     return self._first
    #
    # def get_second(self):
    #     return self._second

    def getOprds(self):
        return self._oprds

    def expand(self):
        expList = []
        pos = self._state.findFirstZero()

        for newValue in range(0,16):
            candidate = self._state.copyState()
            candidate[pos] = newValue
            newState = State(self._keys, candidate, self._oprds, self._result)
            expList.append(newState)

        return expList

    def getRoot(self):
        return self._state

    def setState(self, state):
        self._state = state

    def getHexa(self, opr):
        hexa = ''
        for char in opr:
            hexa = hexa + hex(self._state.getValue(char)).split('x')[1]
        return '0x' + hexa

    def getOprdsSum(self):
        sum = 0
        for opr in self._oprds:
            hexa = self.getHexa(opr)
            sum += int(hexa, 16)
        return sum

    def getOprdsDiff(self):
        sum = int(self.getHexa(self._oprds[0]), 16)
        for opr in self._oprds[1:]:
            hexa = self.getHexa(opr)
            sum -= int(hexa, 16)
        return sum

    def areUnique(self):
        seen = set()

        values = []
        for char in self._keys:
            values.append(self._state.getValue(char))

        return not any(i in seen or seen.add(i) for i in values)


    def noZeros(self):
        count = 0
        for nbr in self._oprds:
            if self._state.getValue(nbr[0]) == 0:
                count += 1
        if count == 0:
            return True
        return False



    def getResult(self):
        res = ''
        for char in self._result:
            res = res + hex(self._state.getValue(char)).split('x')[1]
        return int('0x'+res, 16)


    def isCorrect(self):
        if self.getOprdsSum() == self.getResult() and self.noZeros() == True and self.areUnique() == True:
            return True
        return False

    # def isCorrect(self):
    #     if self._op == '+':
    #         if self.getOprdsSum() == self.getResult() and self.noZeros() == True and self.areUnique() == True:
    #             return True
    #         return False
    #     else:
    #         if self.getOprdsDiff() == self.getResult() and self.noZeros() == True and self.areUnique() == True:
    #             return True
    #         return False