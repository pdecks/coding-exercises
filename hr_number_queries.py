def answer_queries(array_N, array_Q):
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

# The above times out for most test cases. From the discussions on HackerRank:
# There is linear O(N+Q) solution. Use frequency table instead of the original
# array and O(logN) lookups with turn into O(1) array indexing.