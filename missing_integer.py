def solution(nums):
    arr = list(set(nums))
    print(arr)
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
    return len(arr) + 1

# print(solution([-1, -3]))
# print(solution([2]))
# print(solution([1, 2, 3]))


#input integer n > 0 , get maxium 平方根 integer K
def solution2(n):
    if n == 1:
        return 1
    for i in range(n):
        if i * i > n:
            return (i - 1)


print(solution2(12))

