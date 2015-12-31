## O(n**2) Solution
# def get_products_of_all_ints_except_at_index(lst):
#     product_list = []
#     for i in range(len(lst)):
#         current_product = 1
#         if i == 0:
#             sliced_array = lst[1:]
#         elif i == len(lst) - 1:
#             sliced_array = lst[:-1]
#         else:
#             sliced_array = lst[:i] + lst[i+1:]
#         for val in sliced_array:
#             current_product *= val
#         product_list.append(current_product)
        
#     return product_list

## O(n) Solution
def get_products_of_all_ints_except_at_index(lst):
    mult_before_index = [1] * len(lst) 
    mult_after_index = [1]
    final_product = [1] * len(lst) 
    
    for j in range(-1, -(len(lst) + 1), -1):
        if j == -1:
            continue
        else:
            mult_after_index.insert(0, lst[j + 1]*mult_after_index[j + 1])

    for i in range(len(lst)):
        if i != 0:
            mult_before_index[i] = mult_before_index[i - 1] * lst[i - 1]

        final_product[i] = mult_before_index[i] * mult_after_index[i]

    print "Before index:", mult_before_index
    print "After index:", mult_after_index
    print "Final product:", final_product

    return final_product

my_list = [1, 7, 3, 4]
get_products_of_all_ints_except_at_index(my_list)