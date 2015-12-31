"""Hackerrank sorting challenge"""
# # Enter your code here. Read input from STDIN. Print output to STDOUT

# def lex_check(word):
#     """Return the next lexicographically largest word, if it exists"""
#     # find min and max letter
#     min_c = min(word)
#     start = word.index(min_c)
#     max_c = max(word[start:])
#     end = word.index(max_c)
#     if end > start: #swap
#         word_list = list(word)
#         word_list[end - 1], word_list[end] = word_list[end], word_list[end - 1]
#         return "".join(word_list)
#     return "no answer"

# # create list of all input words
# num_words = input()
# words = []
# for i in range(num_words):
#     words.append(raw_input().strip())
#     # print words[i]

# # check each word
# for word in words:
#     print lex_check(word)

# Enter your code here. Read input from STDIN. Print output to STDOUT
def lex_check(word):

    """Return the next lexicographically largest word, if it exists"""
    # find min and max letter
    min_index = word.index(min(word))
    global_min = min_index
    #start = word.index(min_c)
    if len(word) > 2 and min_index == len(word) - 1:
        min_index = word.index(min(word[:-1]))
        #start = word.index(min_c)
        next_min = word.index(min(word[min_index + 1:-1])) # index of next min
    max_index = word.index(max(word[min_index:]))
    #end = word.index(max_c)
    if max_index > min_index: #swap
        word_list = list(word)
        if global_min == min_index:
            word_list[max_index - 1], word_list[max_index] = word_list[max_index], word_list[max_index - 1]
            
        else:
            temp = word_list[min_index]
            word_list[min_index] = word_list[next_min]
            word_list[next_min] = temp
            if max_index < next_min:
                temp = word_list[global_min]
                word_list[global_min] = word_list[max_index]
                word_list[max_index] = temp
        return "".join(word_list)
    return "no answer"


if __name__ == "__main__":
    test = 'dkhc'
    lex_check(test)
# # create list of all input words
# num_words = input()
# words = []
# for i in range(num_words):
#     words.append(raw_input().strip())
#     # print words[i]

# # check each word
# for word in words:
#     print lex_check(word)