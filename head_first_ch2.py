ary = [1,2,3,[4,5,[6,7,8]]]
def print_list(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_list(each_item, level + 1)
        else:
            for each_tab in range(level):
                print('\t', end='')
            print(each_item)

print_list(ary, 0)