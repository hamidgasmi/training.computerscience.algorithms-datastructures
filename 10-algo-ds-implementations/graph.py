

class Weighted_Edge:
    def __init__(self, source: int, sink: int, weight: int):
        self.source = source
        self.sink = sink
        self.weight = weight

class Positively_Weighted_Edge(Weighted_Edge):
    def __init__(self, source: int, sink: int, weight: int):
        assert(weight >= 0)