import re
from bs4 import BeautifulSoup
from .source import Source
from .review import Review

HTML_PARSER = "html5lib"

def suffix_to_number(num: str) -> int:
    conv = {
        'K': 10 ** 3,
        'M': 10 ** 6,
        'B': 10 ** 9
    }
    num = num.strip()
    if num[-1] not in conv:
        return int(num)
    return int(float(num[:-1]) * conv[num[-1]])


def extract_imdb(html: str) -> Source:
    soup = BeautifulSoup(html, HTML_PARSER)
    rating_divs = soup.find(attrs={
        "data-testid": "hero-rating-bar__aggregate-rating__score"
    }).parent.find_all("div")

    score = int(float(rating_divs[0].find("span").get_text()) * 10)
    count = suffix_to_number(rating_divs[2].get_text())

    return Source("imdb", score, count)


def extract_metacritic(html: str) -> Source:
    soup = BeautifulSoup(html, HTML_PARSER)
    rating_div = soup.find(class_="user_score_summary")

    score = int((float(rating_div.find(class_="metascore_w").get_text())) * 10)
    count = int(rating_div.find(class_="based_on").get_text().split(' ')[2])

    return Source("metacritic", score, count)


def extract_rottentomatoes(media_type: str, html: str) -> Source:
    soup = BeautifulSoup(html, HTML_PARSER)

    if media_type == "tv":
        score = soup.find("span", attrs={"data-qa": "audience-score"})
        score = int(score.get_text().strip()[:-1])
        return Source("rotten tomatoes", score, 0)

    score_board = soup.find("score-board")
    count = score_board.find(attrs={"data-qa": "audience-rating-count"})

    score = int(score_board["audiencescore"])
    count = int(re.sub("[^0-9]", "", count.get_text()))

    return Source("rotten tomatoes", score, count)
