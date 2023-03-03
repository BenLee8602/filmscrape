from .review import Review


class Movie:
    score: int
    count: int
    reviews: list[Review]
    
    def __init__(self, score: int=-1, count: int=0, reviews: list[Review]=[]):
        self.score = score
        self.count = count
        self.reviews = reviews
    
    def get_weighted(self, total_count: int) -> int:
        return self.score * self.count // total_count
