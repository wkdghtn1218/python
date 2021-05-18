import urllib.request
from bs4 import BeautifulSoup as bs

def main():
    url = "https://news.sbs.co.kr/news/newsMain.do"
    soup = bs(urllib.request.urlopen(url), "html.parser")
    ul = soup.find("ul", class_ = "type_text")
    for i in ul.find_all("a"):
        print(i.get_text())

if __name__ == "__main__":
    main()