# class1.py 
#클래스(새로운 커스텀 형식을 정의)
class Person:
    #생성자 메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본 생성)
p1 = Person()
p2 = Person() 
p1.name = "전우치"
p1.print()
p2.print()

