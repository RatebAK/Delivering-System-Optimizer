class Truck:
    loads = []
    currentPath = []
    shortestPath = []

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def addLoad(self, *arg):
        for load in arg:
            self.loads.append(load)

    def addPathPoint(self, *arg):
        for point in arg:
            self.loads.append(point)
