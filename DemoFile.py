# DemoFile.py 

URL = "http://www.naver.com/?page=" + str(1) 
print(URL)


import sys 
print("welcome to", "python", sep="~", end="!", file=sys.stderr)

#출력을 파일로 방향을 전환
f = open("c:\\work\\demo.txt", "wt")
print("file write", file=f)
f.close()
print( f.closed )

#파일에 쓰기, 읽기 
f = open("c:\\work\\demo2.txt", "wt")
f.write("한글\n")
f.write("abcd\n1234\n")
f.close() 

f = open("c:\\work\\demo2.txt", "rt")
print("----read()----")
print( f.read() )
print( f.tell() )
#처음으로 돌아가(리셋)
f.seek(0)
print("----readlines()----")
result = f.readlines()
print( result )
#한줄씩 읽기 
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )



