from scrape.extract import extract_imdb, extract_metacritic, extract_rottentomatoes
from scrape.source import Source
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
    source = extract_imdb(html)
    expected = Source("imdb", 95, 1900000)
    assert source.score == expected.score
    assert source.count == expected.count
    assert compareReviewsList(source.reviews, expected.reviews)

def test_extract_metacritic():
    html = open("tests/test_extract/metacritic", "rb").read()
    source = extract_metacritic(html)
    expected = Source("metacritic", 96, 266)
    assert source.score == expected.score
    assert source.count == expected.count
    assert compareReviewsList(source.reviews, expected.reviews)

def test_extract_rottentomatoes():
    html = open("tests/test_extract/rottentomatoes", "rb").read()
    source = extract_rottentomatoes("movie", html)
    expected = Source("rotten tomatoes", 96, 250000)
    assert source.score == expected.score
    assert source.count == expected.count
    assert compareReviewsList(source.reviews, expected.reviews)
