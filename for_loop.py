# 給數字判斷是否是質數，是的話回true
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(prime(36))


# 第一個參數 任意長度一個字串【】，第二個參數是一個>0的整數
# hi 4 = hihihihi
def repeat(string, num):
    result = ''
    for i in range(num):
        result = result + string
    return result

print(repeat('you', 3))


# 給一個目標數，列出小於目標數的list
def solution(nums,target):
    ary = []
    for num in nums:
        if target > num:
            ary.append(num)
    return ary

nums = [2, 7, 11, 13, 19]
print(solution(nums,10))

nums = [99, 7, 1, 2]
print(solution(nums,3))

nums = [-4, 54, 30, 2]
print(solution(nums,100))


# 求1+N的總和
def solution(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + i
    return sum

print(solution(10))


# 求2的N平方等於多少
def solution2(n):
    total = 1
    for i in range(n):
        total = total * 2
    return total

print(solution2(0))
print(solution2(3))


# 求平均值
input1 = [95, 100, 75, 80]
input2 = [1,2,3,4,5]
#expect output: 87.5

def average(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    ans = sum / len(nums)
    return ans

print(average(input1))


# 求成績區間
def grade(num):
    if num > 80:
        return 'A'
    elif num >= 60 and num < 80:
        return 'B'
    else:
        return 'C'

# print(grade(87)) # A
# print(grade(65)) # B
# print(grade(4))  # C


# 交換位置
#input: [a, b], output: [b, a]
def swap(ary):
    result = [ary[1], ary[0]]
    return result
# return [ary[1], ary[0]]

def swap2(ary):
    result1 = ary[0]
    result2 = ary[1]
    ary[0] = result2
    ary[1] = result1
    return ary

def swap3(ary):
    result1 = ary[0]
    ary[0] = ary[1]
    ary[1] = result1
    return ary

print(swap3([4,5]))


# 求最大值
#input = [2,1,4,5,8], output: 8
def largest(ary):
    temp = 0
    for i in ary:
        if i >= temp:
            temp = i
    return temp

# print(largest([2,1,4,5,8]))