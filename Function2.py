# Function2.py 
#전역변수와 지역변수
x = 1 
def func(a):
    return a+x 

#호출
print( func(1) )

def func2(a):
    #지역변수(LGB)
    x = 2 
    return a+x 

#호출
print( func2(1) )


#가변형식은 입출력이 자유롭다
#사실은 원본이 참조가 복사되서 넘어간다. 
def change(x):
    x[0] = "H"

def change(x):
    #내부에서 복사본을 생성
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)


#함수 호출( J(0) | A(1) | M(2) )
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)


#전역변수(불변형식)을 함수 내부에서 읽기+쓰기를 하는 경우
g = 1
def testScope(a):
    #바깥쪽에 있는 전역변수를 맵핑하기 
    #global g 
    g = 2  
    return a+g 

#함수 호출
testScope(1)

#전역변수출력
print("함수 호출후 g:", g)
