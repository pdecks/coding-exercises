"""You want to build a word cloud, an infographic where the size of a word 
corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its
word cloud data in a dictionary, where the keys are words and the values are the
number of times the words occured.

Assume the input will only contain words and standard punctuation.

Are you sure your code handles hyphenated words and standard punctuation?
"""

import string

def word_clouderize(text):
    s = text
    exclude = set('!"#$%&\()*+,./:;<=>?@[\\]^_`{|}~')
    s = ''.join(ch for ch in s if ch not in exclude)
    words = s.split()

    word_cloud = {}
    for word in words:
        lword = word.lower()
        word_cloud[lword] = word_cloud.get(lword, 0) + 1

    return word_cloud


sample1 = 'After beating the eggs, Dana read the next step:'
sample2 = 'Add milk and eggs, then add flour and sugar.'

dict1 = word_clouderize(sample1)
dict2 = word_clouderize(sample2)