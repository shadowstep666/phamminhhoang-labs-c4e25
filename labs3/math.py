from random import randint


socau =True
mang = 3 
while True:
    if mang > 0 :
        x = randint(0,100)
        y = randint(0,100)
        tong = x+y
        z = randint(0,200)
        print(x,"+",y,"=",z)
        n=str(input("nhap vao (y/n)"))
        if socau % 2 == 0 :
            z=tong
            if tong == z :
                if n == "y"   :
                    print(x,"+",y,"=",z)
                    n=str(input("nhap vao (y/n)"))
                elif n == "n" :
                    mang=mang-1
                    print(x,"+",y,"=",z)
                    n=str(input("nhap vao (y/n)"))
            else:
                if n == "n"  :
                    print(x,"+",y,"=",z)
                    n=str(input("nhap vao (y/n)"))
                elif n == "y" :
                    mang=mang-1
                    print(x,"+",y,"=",z)  
                    n=str(input("nhap vao (y/n)"))   
        else :     
            if n == "y"   :
                    print(x,"+",y,"=",z)
                    n=str(input("nhap vao (y/n)"))
                elif n == "n" :
                    mang=mang-1
                    print(x,"+",y,"=",z)
                    n=str(input("nhap vao (y/n)"))
            else:
                if n == "n"  :
                    print(x,"+",y,"=",z)
                    n=str(input("nhap vao (y/n)"))
                elif n == "y" :
                    mang=mang-1
                    print(x,"+",y,"=",z)  
                    n=str(input("nhap vao (y/n)")) 
    else :
        print("lose")
        break



