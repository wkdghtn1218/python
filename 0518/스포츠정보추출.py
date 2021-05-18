import urllib.request
from bs4 import BeautifulSoup as bs

def main():
    for i in range(1,30):
        print("4월 "+ str(i) + "일 최신 뉴스")
        if i>=1 and i<=9:       
            url = "http://news.sbs.co.kr/news/newsSection.do?sectionType=09&pageDate=2021040"+ str(i)
        else:
            url = "http://news.sbs.co.kr/news/newsSection.do?sectionType=09&pageDate=202104"+ str(i)
        soup = bs(urllib.request.urlopen(url), "html.parser")
        ul = soup.find("div", class_ = "w_news_list type_issue")
        for i in ul.find_all("strong"):
            print(i.get_text())

if __name__ == "__main__":
    main()
    