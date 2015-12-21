def dec2bin(dec_num):
    """Given a decimal integer, return its binary equivalent as a string.

    >>> dec2bin(6)
    '110'
    
    >>> dec2bin(12)
    '1100'

    >>> dec2bin(97)
    '1100001'

    """
    # find the largest power of 2 divisible into number
    n = 0
    while 2**(n+1) <= dec_num:
        n += 1
    
    # generate the string
    dec_str = ''
    next_num = dec_num
    while n >= 0:
        curr_char = next_num / 2**n
        dec_str += str(curr_char)
        # only update next_num if next_num would remain > 0
        if next_num - 2**n >= 0:
            next_num -= 2**n
        n -= 1
    return dec_str

