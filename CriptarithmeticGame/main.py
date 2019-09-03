from Controller.Controller import Controller
from Domain.Problem import Problem
from UI.Console import Console


def readFromFile(path):
    '''
    read from file function
    :param path: file path
    :return:
    '''
    try:

        arr = []

        with open(path) as f:
            for line in f:
                line.strip("\n")
                arr.append(line.split())


    except IOError:
        raise Exception("File is missing")

    oprds = []
    oprds.append(arr[0][0])
    cnt = 0
    for i in range(1,len(arr) - 1):
        if (len(arr[i]) == 1):
            oprds.append(arr[i][0])
        cnt+=1

    oprds.append(arr[cnt][0])

    op = arr[0][1]
    res = arr[cnt+1][0]
    if op == '+':
        return Problem(oprds, res, op)
    else:
        first = oprds[0]
        oprds[0] = res
        res = first
        return Problem(oprds, res, op)

if __name__=='__main__':
    path = "input.txt"


    pr = readFromFile(path)
    ctrl = Controller(pr)
    console = Console(ctrl, pr)
    console.run()

    # print(ctrl.DFS(pr.getRoot()))
    # print(ctrl.GBFS(pr.getRoot()))


