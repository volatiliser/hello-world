ary = [1,2,3,[4,5,[6,7,8]]]
def print_list(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_list(each_item, level + 1)
        else:
            for each_tab in range(level):
                print('\t', end='')
            print(each_item)

# print_list(ary, 0)


# format函數中的參數，會依序填到前面字串中的大括號位置。format函數是直接以「.」串列在字串的後方，中間沒有任何空格。
for i in range(5):
    print("Hello, line {}.".format(i))

for i in range(1, 3):
    for j in range(1, 3):
        print("{}*{}={}".format(i, j, i*j))