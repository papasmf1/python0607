# class2.py 
#클래스(새로운 커스텀 형식을 정의)
class Person:
    #클래스에 소속된 멤버변수(데이터 공유)
    num_person = 0 
    #생성자 메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본 생성)
p1 = Person()
p2 = Person() 
p3 = Person() 
print("인스턴스 갯수:{0}".format(Person.num_person) )

#새로운 변수 추가
Person.title = "new title"

print( p1.title )
print( p2.title )
print( Person.title )

