# # quick sort (first item partition)
# def partition(myList, start, end):
#     pivot = myList[start]
#     left = start+1
#     # Start outside the area to be partitioned
#     right = end
#     done = False
#     while not done:
#         while left <= right and myList[left] <= pivot:
#             left = left + 1
#         while myList[right] >= pivot and right >=left:
#             right = right -1
#         if right < left:
#             done= True
#         else:
#             # swap places
#             temp=myList[left]
#             myList[left]=myList[right]
#             myList[right]=temp
#     # swap start with myList[right]
#     temp=myList[start]
#     myList[start]=myList[right]
#     myList[right]=temp
#     return right

# # quick sort (last item partition, left and right meet in middle)
# def partition(myList, start, end):
#     pivot = myList[end]
#     left = start
#     # Start outside the area to be partitioned
#     right = end - 1
#     done = False
#     while not done:
#         while left <= right and myList[left] <= pivot:
#             left = left + 1
#         while myList[right] >= pivot and right >=left:
#             right = right -1
#         if right < left:
#             done= True
#         else:
#             # swap places
#             temp=myList[left]
#             myList[left]=myList[right]
#             myList[right]=temp
#     # swap end with myList[left]
#     temp=myList[end]
#     myList[end]=myList[left]
#     myList[left]=temp
#     return left

# quick sort (last item partition, wall left)
def partition(myList, start, end):

    pivot = myList[end]
    left = start
    # Start outside the area to be partitioned
    right = left
    done = False
    while not done:
        if right != end and myList[right] < pivot:
            if left != right:
                # swap places
                temp=myList[left]
                myList[left]=myList[right]
                myList[right]=temp
            left += 1
            right += 1
        elif right != end:
            right += 1
        else:
            done= True

    # swap end with myList[left]
    temp=myList[end]
    myList[end]=myList[left]
    myList[left]=temp
    print " ".join([str(x) for x in myList])
    return left


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList



def main():
    myList = [7,2,5,1,29,6,4,19,11]
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)

main()