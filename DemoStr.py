# DemoStr.py 
#문자열 만들기
names = ["전우치","홍길동","이순신"]
for name in names:
    print("안녕하세요 {0}님 더운 여름입니다.".format(name))
    print("="*40)


#어떤 메서드가 있는지?
#print( dir(str) )

#데이터 전처리 
u = "<<<  spam and ham  >>>"
print(u)
#사용하지 않는 글자를 제거 
result = u.strip("<> ")
print(result)
result = result.replace("spam", "spam and egg")
print(result)
lst = result.split()
print(lst)
print("---다시 하나의 문자열로 합치기---")
print( ":)".join(lst) )
print( "MBC2580".isalnum() )
print( "2580".isnumeric() )


#정규 표현식(특정한 패턴을 찾기)
import re 
#정확하게 일치하는 경우 
print( re.match("[0-9]*th", "35th") )
#처음부터 끝까지 검색해서 포함하고 있으면 가져오기 
print( re.search("[0-9]*th", "35th") )

#정확하게 일치하는 경우 
print( bool(re.match("[0-9]*th", "35th")) )
#처음부터 끝까지 검색해서 포함하고 있으면 가져오기 
print( bool(re.search("[0-9]*th", "35th")) )

#우편번호 찾기 \d => digit [0-9]{5}
print( bool(re.match("\d{5}", "우리동네는 51200")) )
#search함수는 처음부터 끝까지 지독하게 검색 
print( bool(re.search("\d{5}", "우리동네는 51200")) )

#년도 찾기
print( bool(re.match("\d{4}", "올해는 2021년")) )
#search함수는 처음부터 끝까지 지독하게 검색 
print( bool(re.search("\d{4}", "올해는 2021년")) )
