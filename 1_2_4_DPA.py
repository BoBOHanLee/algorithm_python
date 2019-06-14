#Dynamic Programming Algorithm
#以此重寫費伯納序列

output = [None]*200 #暫存區
def fibonacci_dpa(num):
    result = output[num]
    if result==None :
        if num==0:
            result = 0
        elif num==1:
            result =1
        else:
            result = fibonacci_dpa(num-1)+fibonacci_dpa(num-2)
        output[num] = result
    else:
        pass #代表已經有值無需處理

    return result


print('ans1 = %d'%fibonacci_dpa(5))

