import sys, json
from scrape.request import request_imdb, request_metacritic, request_rottentomatoes
from scrape.extract import extract_imdb, extract_metacritic, extract_rottentomatoes


def get_all_sources(media_type: str, title: str) -> str:
    sources = (
        extract_imdb(request_imdb(title)),
        extract_metacritic(request_metacritic(media_type, title)),
        extract_rottentomatoes(media_type, request_rottentomatoes(media_type, title))
    )
    
    total_count = sum(s.count for s in sources)
    average_score = int(sum(s.get_weighted(total_count) for s in sources))

    return json.dumps({
        "score": average_score,
        "count": total_count,
        "sources": list(map(vars, sources))
    }, indent=4)


def main():
    if len(sys.argv) < 3:
        print("error: must provide 2 args:\n\tmedia type (\"movie\" or \"tv\")\n\ttitle")
        return
    media_type = sys.argv[1]
    title = sys.argv[2]
    if media_type != "movie" and media_type != "tv":
        print("error: media type (arg 1) must be \"movie\" or \"tv\"")
        return
    print(get_all_sources(media_type, title))


if __name__ == "__main__":
    main()
