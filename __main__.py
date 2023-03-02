import sys
from scrape.request import request_imdb, request_metacritic, request_rottentomatoes
from scrape.extract import extract_imdb, extract_metacritic, extract_rottentomatoes


def main():
    if len(sys.argv) < 3:
        print("error: must provide 2 args:\n\tmedia type (\"movie\" or \"tv\")\n\ttitle")
        return
    media_type = sys.argv[1]
    title = sys.argv[2]
    if media_type != "movie" and media_type != "tv":
        print("error: media type (arg 1) must be \"movie\" or \"tv\"")
        return
    
    html = request_imdb(media_type, title)
    imdb = extract_imdb(html)

    html = request_metacritic(media_type, title)
    metacritic = extract_metacritic(html)

    html = request_rottentomatoes(media_type, title)
    rottentomatoes = extract_rottentomatoes(html)


if __name__ == "__main__":
    main()
