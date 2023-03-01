import sys
from selenium import webdriver
from scrape.extract import extract_imdb, extract_metacritic, extract_rottentomatoes

def main():
    if len(sys.argv) < 2:
        print("no title given")
        return
    title = sys.argv[1]
    print(title)
    # do stuff

if __name__ == "__main__":
    main()
