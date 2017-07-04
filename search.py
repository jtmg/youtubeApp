import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
class Search():
    def __init__(self,query):
        self.query = query
        request = urllib.parse.quote(query)
        url = "https://www.youtube.com/results?search_query=" + request
        response = urllib.request.urlopen(url)
        html = response.read()
        self.soup = BeautifulSoup(html,"html.parser")
        self.resp = dict()

    def getResults(self):
        try:
            for vid in self.soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                if "&list=" in vid["href"]:
                    aux = vid["href"].split("&")
                    vid["href"] = aux
                    
                if "?v=" in vid["href"]:
                    self.resp.update({vid['title']:'https://www.youtube.com' + vid['href']})
        except:
            raise
        return self.resp
