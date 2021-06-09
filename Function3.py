# Function3.py
#기본값이 있는 경우
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자 방식
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

#가변인자(인자의 갯수가 가변적인 상황)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )


#정의되지 않은 인자처리(사전식으로 받기)
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str 

#호출
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234") )
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234", 
    name="mike", age="30") )


#람다함수 
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )

print( (lambda x:x*x)(3) )

#메모리에 있는 변수, 함수 보여달라~
print( globals() )

#아무것도 하지 않는 키워드
class Demo:
    pass 


#제너레이터 형태의 함수 정의
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

#함수 호출
for char in reverse("gold"):
    print(char)

#좀 더 단순한 데모 
def abc():
    s = "abc"
    for char in s:
        #값을 생성하고 추출하고 없으면 반환 
        yield char 

#호출
for char in abc():
    print(char)

