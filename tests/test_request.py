from scrape.request import request_imdb, request_metacritic, request_rottentomatoes

def test_request_imdb():
    res = request_imdb("breaking bad")
    not_found_message = "<title>404 Error - IMDb</title>"
    assert not_found_message not in res

def test_request_metacritic():
    res = request_metacritic("tv", "avatar the last airbender")
    not_found_message = "<title>404 Page Not Found - Metacritic - Metacritic</title>"
    assert not_found_message not in res

def test_request_rottentomatoes():
    res = request_rottentomatoes("movie", "fight club")
    not_found_message = "<h1>404 - Not Found</h1>"
    assert not_found_message not in res
