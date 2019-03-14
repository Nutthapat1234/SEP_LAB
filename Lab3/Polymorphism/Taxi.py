from Lab3.Polymorphism.incomplete_code import Transportation


class Taxi ( Transportation):
    def __init__(self,start, end, distance):
        Transportation.__init__(self, start, end, distance)
        self.d = distance

    def find_cost( self ):
        return 40*self.d