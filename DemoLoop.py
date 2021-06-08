# DemoLoop.py 
value = 5 
#디버깅할 때 중단점(Break Point)
#블럭을 주석 처리: ctrl + / 
while value > 0:
    print(value)
    value -= 1 


lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))


#구구단 출력
for x in [2,3,4,5,6]:
    print("----{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))


#continue, break 구문
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("continue구문----")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

print("continue구문----")
for i in lst:
    if i % 2 == 1:
        continue
    print("Item:{0}".format(i))

print("삼각형출력-----")
for i in lst:
    print("*" * i)


#수열함수: range()
print( list(range(10)) )
print( list(range(1,11)) )
print( list(range(2000, 2022)) )
print( list(range(1,32,2)) )

#리스트 컴프리헨션
lst = [1,2,3,4,5,6,7,8,9,10]
#한줄로 코딩
result = [i**2 for i in lst if i > 5]
print(result)
test = ("apple", "orange", "kiwi")
print( [len(i) for i in test] )

#반복문을 사용할 때 필터링하는 함수
lst = [10, 25, 30]
#함수(함수명) ===> first class function(함수도 객체다~~)
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("----필터링하는 경우---")
#필터링하는 함수 정의(여러개의 단어를 합치는 경우:함수명은 카멜 표기법사용)
#네이밍룰(이름명명 기법)
def getBiggerThan20(i):
    return i > 20 

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

