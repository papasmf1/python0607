# web2.py 
# 패키지명.모듈명
import urllib.request
from bs4 import BeautifulSoup

#웹서버에 실행을 요청해서 문자열로 받기
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

#<table> 한줄<tr>  <td>첫번째</td> <td>두번째 컬럼</td>
# <td class="title">
#    <a href="/webtoon/detail.nhn?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format(len(cartoons)) )

f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for tag in cartoons:
    title = tag.find("a").text
    print(title)
    link = tag.find("a")["href"]
    print(link)
    f.write(title + "\n")

f.close()

