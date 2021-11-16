"""
파이썬 모듈 안에는 함수와 클래스를 선언할 수 있다
block comment
"""
# line comment

def add(n1,n2):
    #pass
    return n1 + n2

#add(10,20)
print(type(add))
print(add(10,20))

add2 = lambda n1,n2 : n1+n2
print(type(add2))
print(add2(10,10))

#클래스 생성
class User:
    #생성자 선언
    def __init__(self, name):
        self.name = name

    # toString()
    def __str__(self):
        return self.name

#객체생성
user = User("Python")
print(user)


#ctrl + shift + f10 : 실행