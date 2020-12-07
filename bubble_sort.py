def bubble(list):
    for i in range(len(list)):
        for j in range (i + 1, len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def bubble2(list):
    for i in range(len(list)):
        for j in range (len(list)-1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


print(bubble2([4,9,3]))
print(bubble2([22,39,55,20,27,11]))
print(bubble2([55,44,33,22,11]))