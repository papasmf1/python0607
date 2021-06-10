# 메모리구조.py
#부모 클래스 
class SuperClass:
    def __init__(self):
        self.x = 10 
    def printX(self):
        print(self.x)

#자식클래스 
# class SubClass(SuperClass):
#     #덮어쓰기(재정의)
#     def __init__(self):
#         #생성자를 재정의하는 경우 필수적으로 부모 생성자 호출
#         SuperClass.__init__(self)
#         self.y = 20
#     def printY(self):
#         print(self.y)

s = SubClass()
s.a = 30 
# ctrl + / 
# print("SuperClass:", SuperClass.__dict__)
# print("SubClass:", SubClass.__dict__)
# print("s:", s.__dict__)
s.printX()
s.printY()
 
