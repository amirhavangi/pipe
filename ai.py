from world import World


def HowToReturnPath(array2d, s, e, w, h):
    array2d[s] = [1, 1, 1, 1]
    array2d[e] = [1, 1, 1, 1]
    world = World(array2d, s, e, w, h)
    print world
    return depthFirstSearch(world)


def depthFirstSearch(world):
    act1 = world.rotate_block(2, 1, 180)
    act2 = world.rotate_block(0, 1, 270)
    act3 = world.rotate_block(1, 1, 90)
    return [act1, act2, act3]


def breadthFirstSearch(world):
    return [] 


def iterativeDeepeningSearch(world):
    return []


def uniformCostSearch(world):
    return []


def manhattanHeuristicFunction(world):
    return 0


def heuristicFunction(world):
    return 0


def aStarSearch(world):
    return []
