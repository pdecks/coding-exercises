def hex_convert(hex_in):
    """Given a hexadecimal number as a string, return equiv. decimal integer

    >>> hex_convert('6')
    6

    >>> hex_convert('1A')
    26

    >>> hex_convert('FFFF')
    65535
    """
    # determine max power of 16
    n = len(hex_in) - 1

    int_sum = 0
    place = 0
    while n >= 0:
        int_sum += (16 ** n) * int(hex_in[place], 16)
        n -= 1
        place += 1

    return int_sum