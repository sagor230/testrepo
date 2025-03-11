name = "sagor"
age = 25
a = [1,2,3]
print(type(name),age,type(a))

#name = input("enter your name : ")
print(name)
'''
mark = int(input("enter marks : "))
if mark > 90 : 
    print("Grade A")
elif mark > 80:
    print("grade B")
else :
    print("lower grade")
'''
''''for i in range(1,6):
    if i==3:
        continue
    print("num",i)

for i in range(1,6):
    if i ==3 : 
        break
    print(i)
'''

def hello(a,b):
    #print("hello")
    return a + b

print(hello(4,5))

sqare_lam = lambda x:x*x
print(sqare_lam(5))

add = lambda a,b:a+b
print(add(5,5))
