# x=int(input("nhap vao so x :"))
# y=int(input("nhap vao so y :"))
# print("x=",x)
# print("y=",y)
# print("tong la ",x+y)


# pheptinh=str(input("nhap vao phep tinh"))
# print("x=",x)
# print("y=",y)


def eval(x,y,pheptinh):
    result =0
    if pheptinh == "+":
        result=x+y
    elif pheptinh =="-":
        result=x-y
    elif pheptinh =="*":
        result=x*y
    elif pheptinh == "/": 
        result=x/y

    return result

# a=int(input("a="))
# b=int(input("b="))
# op=input("op=")
# r= eval(a,b,op)
# print(r)


# def sayHi(n):# n la tham so cua ham 
#     print("hi")
#     print("hi",n)
#     print("bye bye")
# sayHi("quan")
# sayHi("minh")


# def add(x, y):
#     r = x+y
#     # return r

# s=add(5,6)
# print(s)
