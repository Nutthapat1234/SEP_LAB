from Polymorphism.incomplete_code import Transportation

class Train(Transportation):
    def __init__(self, start, end, distance, station):
        Transportation.__init__(self, start, end, distance)
        self.a = station
    def find_cost(self):
        return self.a*5