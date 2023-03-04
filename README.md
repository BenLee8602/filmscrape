# filmscrape
Web scraper for film reviews and ratings

### Install
clone repo and install dependencies
```
git clone https://github.com/BenLee8602/filmscrape.git
cd filmscrape
pip install -r requirements.txt
```

### Usage
run the main script, with 2 args:
- type: media type to search for, must be `movie` or `tv`
- title: title of the movie or tv show
you can pipe the output to a file, in this case "results.json"
```
python . movie "fight club" > results.json
```

### Output
the script outputs json containing the following info:
- score: rating of the movie/show out of 100
- count: number of ratings the score is based on

results.json after running the above commands:
```json
{
    "score": 88,
    "count": 2452123,
    "sources": [
        {
            "name": "imdb",
            "score": 88,
            "count": 2200000,
            "reviews": []
        },
        {
            "name": "metacritic",
            "score": 89,
            "count": 2123,
            "reviews": []
        },
        {
            "name": "rotten tomatoes",
            "score": 96,
            "count": 250000,
            "reviews": []
        }
    ]
}

```
