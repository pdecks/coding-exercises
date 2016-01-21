def answer_queries(array_N, array_Q):
    """ Sample Input / Output

    >>> 3
    >>> -1 2 -3
    >>> 3
    >>> 1 -2 3
    5
    7
    6

    """
    length = len(array_N)
    curr_array = array_N[:]
    # abs_sum_N = abs(sum(array_N))
    # for q in array_Q:
    #     print abs_sum_N + length * abs(q)
    for q in array_Q:
        for i, n in enumerate(curr_array):
            curr_array[i] = curr_array[i] + q
        print sum([abs(x) for x in curr_array])
        
    
# input parsing
len_N = int(raw_input())
lst_N =  [int(x) for x in raw_input().strip().split()]
len_Q = int(raw_input())
lst_Q =  [int(x) for x in raw_input().strip().split()]

answer_queries(lst_N, lst_Q)

# The above times out for most test cases, as it is O(nxq).
# From the discussions on HackerRank:
# There is linear O(N+Q) solution. Use frequency table instead of the original
# array and O(logN) lookups with turn into O(1) array indexing.

# It's more of a math question than coding. My solution has complexity 
# O(logN + N + QlogN). Got timeout for the last testcase firstly. The trick is 
# to use printf instead cout. After that the execution time significantly 
# improved. My solution was to sort the array only once at the beginning 
# (because whatever the query will be the order of array remains same), and use 
# prefix sum to store the so-far sum of array and so-far sum of queries, and for
# every query use binary search to find the element that is the closest to the 
# opposite of prefix sum of queries, that means you can use the (sum of the left
# side of that element) + (prefix sum of queries) * (number of left-side
# elements) to get the sum of that part and the same way for the right side.