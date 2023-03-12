def element_at(my_list, ix):
    if ix < 0 or ix > (len(my_list) - 1):
        return (None)
    return (my_list[ix])

my_list = [1, 2, 3, 4, 5]
ix = 4
print("Element at index {:d} is {}".format(ix, element_at(my_list, ix)))
