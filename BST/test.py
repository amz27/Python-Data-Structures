import sys
import random
from kheap import minHeap


def test_pop_min(num_testcases, kmin=2, kmax=16, minsize=0,
                 maxsize=10 ** 2, minval=-sys.maxint, maxval=sys.maxint):
    for _ in xrange(num_testcases):
        # get some random numbers
        size = random.randint(minsize, maxsize)
        arr = [random.randint(minval, maxval) for _ in xrange(size)]
        k = random.randint(kmin, kmax)

        # get a k-heap
        h = minHeap(k)

        # fill heap
        for el in arr:
            h.add_num(el)

        arr.sort()

        # test heap extraction using de facto heapsort
        for el in arr:
            if h.pop_min() != el:
                print '{}-heap failed on array of size {}'.format(k, size)
                break


if __name__ == '__main__':
    try:
        test_pop_min(*map(int, sys.argv[1:]))
    except TypeError as e:
        print e
        print('Usage: ~$ python {} num_testcases kmin kmax minsize maxsize'
              ' minval maxval'.format(sys.argv[0]))
    except Exception:
        print 'Something went wrong :('
        raise

