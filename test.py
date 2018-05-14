
class State:
    def __init__(self ,x ,y):
        self. x =x
        self. y =y
    def isgoal(self):
        return self.y==1
    def tostring(self):
        return str((self.x ,self.y))
    def getlegalactions(self):
        result =[]
        if self. x >0:
            result.append("Empty5")
        if self. y >0:
            result.append("Empty2")
        if self. x<=3 and self.y >0:
            result.append("2to5")
        if self. x>=2 and self.y==0:
            result.append("5to2")
        if self. x==1 and self.y <2:
            result.append("5to2part")
        return result
def step(state ,action):
    if action=="Empty5":
        return State(0 ,state.y)
    if action=="Empty2":
        return State(state.x ,0)
    if action=="2to5":
        return State(state. x +state.y ,0)
    if action=="5to2":
        return State(state. x -2 ,2)
    if action=="5to2part":
        return State(0 ,state. y +state.x)

    return state


# print(initialstate.getlegalactions())
# print(initialstate.isgoal())
# state=step(initialstate,"Empty5")
# print(state.x,state.y)
# print(state.tostring())

def BFS(state):
    #    pdb.set_trace()
    todo =[(state ,[])]
    finished =False
    while not finished:
        cur,path =todo[0]
        del todo[0]
        legalactions =cur.getlegalactions()
        for action in legalactions:
            newstate =step(cur ,action)
            todo.append((newstate ,path +[action]))

            if newstate.isgoal():
                finished =True
                return path +[action]
initialstate =State(5 ,0)
path =BFS(initialstate)
print(path)

path = []   # the solution
states = []   # the seen states
def DFS(state):
    states.append(state.tostring())
    if state.isgoal():
        return True
    for action in state.getlegalactions():
        newstate = step(state, action)
        if newstate.tostring() not in states:
            pass
        else:
            continue
        path.append(action)
        if DFS(newstate):
            return True
        else:
            path.remove(action)
    return False


initialstate=State(5,0)
DFS(initialstate)
print(path)
