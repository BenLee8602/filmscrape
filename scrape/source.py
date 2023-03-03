from .review import Review

class Source:
    def __init__(self, name: str, score: int=-1, count: int=0, reviews: list[Review]=[]):
        self.name: str = name
        self.score: int = score
        self.count: int = count
        self.reviews: list[Review] = reviews
    
    def get_weighted(self, total_count: int) -> float:
        return self.score * self.count / total_count
