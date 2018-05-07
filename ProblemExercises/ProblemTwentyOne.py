"""

"""

import requests
from bs4 import BeautifulSoup


def getURLRequest():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text 
    return r_html

def writeToFile(path):
    r_html = getURLRequest()
    soup = BeautifulSoup(r_html,"html.parser")
    headings = soup.findAll("h2", {"class": "story-heading"})
    with open(path,'w') as open_file:
        for heading in headings:
            if heading.findAll("a"):
                open_file.write(heading.a.text.replace("\n", " ").strip() + '\n')
            else:
                open_file.write(str(heading.text).replace("\n", " ").strip() + '\n')

def main(filePath):
    writeToFile(filePath)

if __name__ == '__main__':
    path = 'C:/Users/Home/Desktop/grid.txt'
    main(path)
    print("Success File Closed")