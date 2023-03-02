class Review:
    rating: int
    text: str

    def __init__(self, rating: int=-1, text: str=""):
        self.rating = rating
        self.text = text
