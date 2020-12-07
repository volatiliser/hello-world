# f(0)=1 f(1)=1 f(2)=1+1=2 f(3)=1+2=3 f(4)=2+3=5 f(5)=3+5=8 f(6)=5+8=13 f(7)=8+13=21 f(8)=13+21=34
# f(n)=f(n-2)+f(n-1)

def fibo(n):
    if n == 0 or n == 1:
        return 1;
    else:
        prev1 = 1
        prev2 = 1
        result = 0;
        for i in range(n - 1):
            result = prev1 + prev2
            prev2 = prev1
            prev1 = result 

        return result

def fibo2(n):
    ary = [1, 1]
    for i in range(2, n + 1):
        ary.insert(i, ary[i - 2] + ary[i - 1])
    return ary[n]

def fibo_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo_recursive(n - 2) + fibo_recursive(n - 1)


print(fibo_recursive(0))
print(fibo_recursive(1))
print(fibo_recursive(2))
print(fibo_recursive(6))