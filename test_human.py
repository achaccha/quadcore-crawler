from crawler.rss import RSSCrawler
from crawler.github import GithubCrawler
from crawler.wiki import WikipediaCrawler
from crawler.config import RSSConfig as conf

import json, sys

def test_rss():
    # RSS test
    # TODO prevent from unappropriate input
    newspaper = input("[+] Newspaper name: ")
    rss_result = RSSCrawler(newspaper)
    print(json.dumps(rss_result, indent=4))

def test_github():
    # Github test
    # TODO prevent from fake username
    username = input("[+] GitHub Username: ")
    github_result = GithubCrawler(username)
    print(json.dumps(github_result, indent=4))

def test_wiki():
    # Wikipedia test
    wiki_result = WikipediaCrawler()
    print(json.dumps(wiki_result, indent = 4))

def main():
    print("[+] Type 1 for RSS, 2 for Github, 3 for Wiki. Other to exit.")
    choose = input("[?] Choose > ")
    if choose == "1": test_rss()
    elif choose == "2": test_github()
    elif choose == "3": test_wiki()
    else: sys.exit(0)

if __name__ == "__main__":
    while True: 
        main()
        print("\n\n\n")