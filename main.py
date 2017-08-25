from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def returnAllChildAnchors(href_list):
    # 等等我們要回傳的子節點list
    result_list = []
    for single_href in href_list:
        try:
            html = urlopen(single_href)
            bsObj = BeautifulSoup(html, "html.parser")
            for anchor in bsObj.findAll("a"):
                if anchor.has_attr('href') and anchor['href'].startswith('/wiki/') and not anchor['href'].startswith('/wiki/Wikipedia'):
                    #print(anchor['href'])
                    result_list.append('https://zh.wikipedia.org' + anchor['href'])
                    if anchor.has_attr('title'):
                        print('title = ', anchor['title'])
        except:
            print('open ', single_href, ' error')
    return result_list

ssl._create_default_https_context = ssl._create_unverified_context
startUrl = ['https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%BF%B0%C2%B7%E5%88%97%E4%BE%AC']
stopUrl = 'https://zh.wikipedia.org/wiki/%E8%BF%88%E5%85%8B%E5%B0%94%C2%B7%E4%B9%94%E4%B8%B9'
times = 0

while True:
    print("times", times)
    startUrl = returnAllChildAnchors(startUrl)
    print(times, startUrl)
    times = times + 1
    if stopUrl in startUrl:
        print("find in ", times, " times")
        break



