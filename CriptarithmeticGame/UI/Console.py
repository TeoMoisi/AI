import time


class Console:
    def __init__(self, c, pr):
        self.__pr = pr
        self.__controller = c


    def printOptions(self):
        print("Options: \n"
              "0. Exit\n"
              "1. Run using dfs\n"
              "2. Run using gbfs\n")

    def uiDFS(self):
        startTime = time.clock()

        result = self.__controller.DFS(self.__pr.getRoot())

        if result is None:
            print("Cannot reach configuration!")
        else:
            print(result)

        print("Time: {0} \n".format(time.clock() - startTime))

    def uiGBFS(self):
        startTime = time.clock()

        result = self.__controller.GBFS(self.__pr.getRoot())

        if result is None:
            print("Cannot reach configuration!")
        else:
            print(result)

        print("Time: {0} \n".format(time.clock() - startTime))


    def run(self):
        options = {"1": self.uiDFS, "2": self.uiGBFS}

        while True:
            try:
                self.printOptions()
                cmd = input()

                if cmd == "0":
                    break

                if cmd not in options.keys():
                    raise ValueError("Inexistent command")

                options[cmd]()
                time.sleep(3)
            except Exception as ex:
                print(ex)