import re
import requests
from bs4 import BeautifulSoup
import ssl
import Summerizer_Model
ssl._create_default_https_context = ssl._create_unverified_context


def indianews():
    url="https://www.ndtv.com/india?pfrom=home-mainnavgation"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"lxml")
    news_box=soup.find("div", class_="new_storylising" )
    allnews=news_box.find_all("h2", class_="nstory_header")
    def fetch_news(allnews):
        a=0
        for news in allnews:
            newstext=news.find("a").contents[0]
            print("NEWS HEADLINE---{x}--->>>".format(x=str(a+1)),re.sub(r"^\s+","",newstext))
            print()
            for link in newstext:
                newslink=news.find("a")["href"]
                res=requests.get(newslink)
                soup=BeautifulSoup(res.text,"lxml")
                news=soup.find("div",id="ins_storybody")
                try:
                    places=news.find("b",class_="place_cont")
                    print(places.text)
                except AttributeError:
                    pass
                all_content=news.find_all("p",class_="")
                wholeContents=""
                for content in all_content:
                    wholeContents+=content.text
                #print(wholeContents)
                print(Summerizer_Model.summerizer(wholeContents))
                print()
                break
            a+=1
            
    fetch_news(allnews)
    print("<<<<------------------>>>>NEXT PAGE<<<<-------------->>>>")
    print()
    print()
    
    for i in  range(1,15):
        url2="https://www.ndtv.com/india/page-{}".format(i)
        res=requests.get(url2)
        soup=BeautifulSoup(res.text,"lxml")
        news_box=soup.find("div", class_="new_storylising" )
        allnews=news_box.find_all("h2", class_="nstory_header")
        fetch_news(allnews)
        print("<<<<---------------->>>>NEXT PAGE<<<<---------------->>>>")
        print()
        print()            
indianews()
