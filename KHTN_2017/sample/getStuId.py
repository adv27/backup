from lxml import etree
import urllib
from bs4 import BeautifulSoup
from urllib import request
import lxml.html as LH
import io

def saveToFile(data, file_name):
    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(data)

def getID(soup):
    ids = list()
    tds = soup.find_all('td')
    for td in tds:
        if td.has_attr('width'):
            if td.attrs['width'] == '10%':
                ids.append(td.get_text())
    saveToFile(','.join(ids),"listId.txt")

def getData():
    url = 'http://hsgs.edu.vn/images/stories/gbthpt2017.html'
    page = urllib.request.urlopen(url,timeout=20)
    content = page.read()
    soup = BeautifulSoup(content,'lxml')
    print('Loaded')
    getID(soup)
        

def main():
    getData()
    

if __name__ ==  "__main__":
    main()
