import re
from selenium import webdriver


def request(url: str) -> str:
    driver = webdriver.Chrome()
    driver.get(url)
    res = driver.page_source
    driver.quit()
    return res

def request_imdb(title: str) -> str:
    url = f"https://www.imdb.com/find/?q={title}"
    res = request(url)
    idx = res.find("href=\"/title/tt") + len("href=\"/title/tt")
    id = res[idx:].split('/', 1)[0]
    url = f"https://www.imdb.com/title/tt{id}"
    return request(url)

def request_metacritic(media_type: str, title: str) -> str:
    title = re.sub(r'[^a-z0-9-]+', '', title.lower().replace(' ', '-'))
    url = f"https://www.metacritic.com/{media_type}/{title}"
    return request(url)

def request_rottentomatoes(media_type: str, title: str) -> str:
    media_type = "m" if media_type == "movie" else "tv"
    title = re.sub(r'[^a-z0-9_]+', '', title.lower().replace(' ', '_'))
    url = f"https://www.rottentomatoes.com/{media_type}/{title}"
    return request(url)
