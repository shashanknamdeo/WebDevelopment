def sum1(a, b):
    return a+b

def operation(opertor, a, b):
    return opertor(a,b)

print(operation(opertor=sum1, a=1, b=5))

s = operation

print("s : ", s(opertor=sum1, a=1, b=5))


print(operation)