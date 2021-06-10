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


