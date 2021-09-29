def unabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError ('wrong')
    else:
         if x <=0:
            return x
         else:
            return -x ##定义一个反绝对值的函数

def power(x, n):
    s = x
    while n > 1:
        n = n-1
        s = s * x
    return s



     