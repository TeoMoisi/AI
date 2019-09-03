from copy import deepcopy


class State:

    def __init__(self, letters, values, oprds, res):
        '''

        :param letters: all the letter whose values have ot be found
        :param values: list of values for every letter
        :param oprds: list of the operands
        :param res: result of the operation
        '''
        self.__letters = letters
        self.__values = values
        self.__oprds = oprds
        self.__result = res

    def __eq__(self, other):
        for i in range(0, len(self.__values)):
            if self.__values[i] != other.getValues()[i]:
                return False
        return True

    def __lt__(self, other):
        return self.heuristics() < other.heuristics()

    def heuristics(self):
        sum = 0
        maxOp = max(self.__oprds, key=len)
        minOp = min(self.__oprds, key=len)
        maxLen = max(len(maxOp), len(self.__result))
        minLen = min(len(minOp), len(self.__result))


        for i in range(maxLen, 0):
            nbr_sum = 0
            for nbr in self.__oprds:
                nbr_sum += self.getValue(nbr[i])
                if i < minLen:
                    sum += abs(nbr_sum - self.getValue(self.__result[i]))

                elif i < len(nbr):
                    sum += abs(self.getValue(nbr[i]) - self.getValue(self.__result[i]))
                else:
                    sum += self.__result[i]
        return sum

    def getValue(self, char):
        for i in range(len(self.__letters)):
            if self.__letters[i] == char:
                return self.__values[i]
        return -1

    def setValues(self, values):
        self.__values = values

    def getValues(self):
        return self.__values

    def getLetters(self):
        return self.__letters


    def findFirstZero(self):
        for i in range(len(self.__letters)):
            if self.__values[i] == 0:
                return i
        return -1

    def copyState(self):

        copy_letters = [val for val in self.__letters]
        copy_values = [val for val in self.__values]
        copy_oprds = [val for val in self.__oprds]
        copy_result = [val for val in self.__result]

        copy = State(copy_letters, copy_values, copy_oprds, copy_result)
        return copy.getValues()
