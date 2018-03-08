import requests
from bs4 import BeautifulSoup

# if __name__== '__main__':
#     re_obj = requests.get('https://movie.douban.com/')
#     bs_obj = BeautifulSoup(re_obj.text.encode('utf-8'),'html.parser')
#
#     print(bs_obj)

def getContent():
    with open(r'F:\python\test\html.txt','rb') as f:
        return f.read()
if __name__== '__main__':
    soup = BeautifulSoup(getContent(), 'lxml')
    # print(soup.title.name)
    # print(soup.p.attrs['class'])
    # print(soup.find_all('p'))
    # print(soup.find_all('a'))
    # print(soup.find_all('href'))
    # print(soup.select('p'))
    # print(soup.select('.appintro-title'))
    # print(soup.select('p.appintro-title'))

    list = list(soup.find_all('a'))
    for mylist in list:
        # print(mylist)
        # print(mylist.get_text())
        # print(mylist.get['href'])
         print(mylist['href'])