class Fibber(object):
    """Compute fibonacci(n) in O(n) time and O(n) space."""
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise ValueError('n must be 0 or a positive integer')

        elif n in [0, 1]:
            return n

        # check in n in memo
        if self.memo.get(n, 0) != 0:
            print "Getting memo at", n
            return self.memo[n]

        else:
            print "Calculating memo at", n
            result = self.fib(n - 1) + self.fib(n - 2)
            self.memo[n] = result

            return result


def fib_bot_up(n):
    """Compute fibonacci(n) in O(n) time and O(1) space."""
    if n < 0:
        raise ValueError('n must be 0 or a positive integer')
    
    elif n in [0, 1]:
        return n
    
    prev_prev = 1
    prev = 0

    for _ in xrange(n):
        print "n:", _
        current = prev_prev + prev
        print "current:", current
        prev_prev = prev
        prev = current

    return current

if __name__ == "__main__":

    print fib_bot_up(3)
    print Fibber().fib(3)