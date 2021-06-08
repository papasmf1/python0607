# Function1.py 
#함수를 정의
def times(a,b):
    return a*b

#함수를 호출
print( times(3,4) )

#함수를 정의
def setValue(newValue):
    x = newValue
    print(x)

#호출
result = setValue(5)
print(result)

#값을 리턴 
def swap(x,y):
    return y,x

#호출
print( swap(3,4) )

#불변형식과 가변형식
a = 1.2
print( id(a) )
a = 2.3 
print( id(a) )

#가변형식
lst = [1,2,3]
print("가변형식:", id(lst) )
lst.append(4)
print("가변형식:", id(lst) )

#디버깅 연습(문자의 교집합)
def intersect(prelist, postlist):
    #내부에서 교집합 문자를 저장할 리스트(지역변수) 
    retList = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에도 있고 그리고 x가 retList에 없으면 
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

#호출(디버깅할 때 중단점)
print( intersect("HAM","SPAM") )


