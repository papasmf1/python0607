#클래스 외부에 전역 변수 
str = "Not Class Member"
class GString:
    def __init__(self):
        #인스턴스에서 사용할 멤버 변수 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그 발생~~
        print(self.str)

#인스턴스 생성 
g = GString()
g.set("First Message")
g.print()
