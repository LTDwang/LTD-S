def unabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError ('wrong')
    else:
         if x <=0:
            return x
         else:
            return -x ##定义一个反绝对值的函数


     