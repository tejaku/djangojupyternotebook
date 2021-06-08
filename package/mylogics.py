class MyMath:
    def isEven(num):
        if num%2==0:
            return True
        return False
        
    def isodd(num):
        if num%2==0:
            return False
        return True
    
    def isprime(num):
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    
class calsi:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
        