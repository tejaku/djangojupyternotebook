def add(*a):
    s=0
    for i in a:
        s+=i
    return s

def sub(a,b):
    c=0
    if a>b:
        c=a-b
    else:
        c=b-a
    return c
        
def multiply(*a):
    s=1
    for i in a:
        s*=i
    return s

def division(a,b):
    return a/b