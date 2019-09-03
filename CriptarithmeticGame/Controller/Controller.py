from queue import PriorityQueue


class Controller:

    def __init__(self, problem):
        self._problem = problem

    def DFS(self, root):
        visited = []
        stack = [root]
        while stack:
            currentState = stack.pop()
            visited.append(currentState)
            self._problem.setState(currentState)
            if self._problem.isCorrect():

                return self.createSolution(currentState)

            for newState in self._problem.expand():
                if newState not in visited:
                    #stack.append(newState)
                    stack = [newState] + stack

    def GBFS(self, root):
        visited = []
        queue = PriorityQueue()
        queue.put(root)
        while not queue.empty():
            currentState = queue.get()
            visited.append(currentState)
            self._problem.setState(currentState)
            if self._problem.isCorrect():

                return self.createSolution(currentState)

            for newState in self._problem.expand():
                if newState not in visited:
                    queue.put(newState)

    def createSolution(self, state):
        solution = {}
        for i in range(len(state.getValues())):
            solution[state.getLetters()[i]] = hex(state.getValues()[i])
        return solution