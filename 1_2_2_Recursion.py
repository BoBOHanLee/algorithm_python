import numpy

# n! algorithm

def n_fumc(num):
    if num != 0:
        ans = num*n_fumc(num-1)
        return ans
    else:
        return 1

print('ans1 = %d'%(n_fumc(5)))

#Fibonacci Polynomial
#  Fn = {0 if n==0 ; 1 if n==1 ; Fn-1+Fn-2 if n==2,3,4,5.......}

def Fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return Fibonacci(num-1)+Fibonacci(num-2)

print('ans2 = %d'%(Fibonacci(4)))
