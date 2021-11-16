#packing
my_list1 = [20,30,40]
print(my_list1)
#unpacking
n1,n2,n3 = my_list1
print(n1,n2,n3)

my_list2 = list()

my_list1.append(10)
print(my_list1)
my_list1.extend([50,60,70])
print(my_list1)
my_list1.insert(0,10)
print(my_list1)
print(my_list1[0:3])

#set - 중복 허용 않함, 순서 유지 않됨
my_set = set(my_list1)
print(type(my_set))
print(my_set)

my_tuple = (100,200,300)
my_tuple2 = tuple()
print(type(my_tuple))
print(my_tuple)
# my_tuple[0] = 10
# print(my_tuple) # 에러 튜블 read only, 리스트보다 튜블이 속도가 빠르다

num1 = (3)
num2 = (3,)
print(type(num1), type(num2))

#tuple usage
def swap(a, b) :
    #튜플 형태로 리턴하는 것도 가능함
    return (b,a)

n1,n2 = swap(10, 20)
print(n1, n2)


