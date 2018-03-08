import requests
from bs4 import BeautifulSoup

re = requests.get('https://book.douban.com/top250?start=25')
soup = BeautifulSoup(re.text,'lxml')

#书名
nameList = soup.find_all('div',class_ = 'pl2')
nameL = [name.find('a')['title'] for name in nameList]
#作者信息
authorList = soup.find_all('p',class_ = 'pl')
authorL = [author.get_text() for author in authorList]
#评分
starList = soup.find_all('span',class_ = 'rating_nums')
starL = [star.get_text() for star in starList]
#评价
plList = soup.find_all('span',class_ = 'pl')
plL = [pl.get_text() for pl in plList]
# plList = soup.select('div > table > div  span')
#简介
shortList = soup.find_all('span',class_ = 'inq')
shortL = [short.get_text() for short in shortList]
# for name in nameList:
#     print(name.find('a')['title'])
# for author in authorList:
#     print(author.get_text())
# for star in starList:
#     print(star.get_text())
# for pl in shortList:
#     print(pl.get_text())
    # print(pl)

# 文件名
filename = '豆瓣图书Top250.txt'
f = open(filename, 'w', encoding='utf-8')
# 保存文件操作
# 合并
for name,author,star,short in zip(nameL,authorL,starL,shortL):
    f.writelines("%s , %s , %s , %s" %(name,author,star,short)+'\n'+'=============='+'\n')


f.close()
print('保存成功')


