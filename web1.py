# web1.py 
#from 패키지명 import 모듈명
from bs4 import BeautifulSoup

#물리적으로 저장된 html파일 읽기(Read Text) 유니코드(utf-8)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체(HTML태그)
soup = BeautifulSoup(page, "html.parser")

#print( soup.prettify() )

#모든 <p>태그를 검색
#print( soup.find_all("p") )

#첫번째 <p>태그 
#print( soup.find("p") )

#필터링(조건을 주고 걸러내기): <p class="outer-text">컨텐츠</p>
#태그의 스타일을 적용하는 class속성
#print( soup.find_all("p", class_="outer-text") )

#태그 내부의 문자열 데이터 
for tag in soup.find_all("p"):
    #태그를 없애고 컨텐츠만 가져오기 
    print(tag.text.replace("\n", "").strip())



