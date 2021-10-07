def unabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError ('wrong')
    else:
         if x <=0:
            return x
         else:
            return -x ##定义一个反绝对值的函数

def power(x, n =2):
    s = x
    while n > 1:
        n = n-1
        s = s * x
    return s

def imfor(name, age):
     print ("name:", name)
     print ("age:", age)

def get(f, g, h):
    b =(f, g, h)
    a =b[0]
    print (a)

def jiecheng(i):
    if i ==1:
        return 1
    return i * jiecheng(i-1)
    

     