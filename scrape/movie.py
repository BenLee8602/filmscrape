from .review import Review


class Movie:
    rating: int
    rating_count: int
    reviews: list[Review]
    
    def __init__(self, rating: int=-1, rating_count: int=0, reviews: list[Review]=[]):
        self.rating = rating
        self.rating_count = rating_count
        self.reviews = reviews
