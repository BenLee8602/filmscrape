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
    
    all_sources = (
        extract_imdb(request_imdb(title)),
        extract_metacritic(request_metacritic(media_type, title)),
        extract_rottentomatoes(media_type, request_rottentomatoes(media_type, title))
    )
    
    total_count = sum(source.count for source in all_sources)
    average_score = sum(source.get_weighted(total_count) for source in all_sources)
    print(average_score)


if __name__ == "__main__":
    main()
