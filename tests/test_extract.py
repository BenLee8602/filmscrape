from scrape.extract import extract_imdb, extract_metacritic, extract_rottentomatoes
from scrape.movie import Movie
from scrape.review import Review

def compareReviewsList(r1: list[Review], r2: list[Review]) -> bool:
    if len(r1) != len(r2):
        return False
    for i in range(len(r1)):
        if r1[i].score != r2[i].score or r1[i].text != r2[i].text:
            return False
    return True

def test_extract_imdb():
    html = open("tests/test_extract/imdb", "rb").read()
    movie = extract_imdb(html)
    expected = Movie(95, 1900000)
    assert movie.score == expected.score
    assert movie.count == expected.count
    assert compareReviewsList(movie.reviews, expected.reviews)

def test_extract_metacritic():
    html = open("tests/test_extract/metacritic", "rb").read()
    movie = extract_metacritic(html)
    expected = Movie(96, 266)
    assert movie.score == expected.score
    assert movie.count == expected.count
    assert compareReviewsList(movie.reviews, expected.reviews)

def test_extract_rottentomatoes():
    html = open("tests/test_extract/rottentomatoes", "rb").read()
    movie = extract_rottentomatoes("movie", html)
    expected = Movie(96, 250000)
    assert movie.score == expected.score
    assert movie.count == expected.count
    assert compareReviewsList(movie.reviews, expected.reviews)
