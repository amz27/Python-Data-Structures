import sys





def pizzasearch(alist):
    locations = pizzasearch(alist, 0, len(alist) - 1)
    return locations


def pizzasearch(alist, min, max):
    n = (max - min) + 1
    if n > 2:
        mid = n/2
        i = mid
        if alist[mid] <= alist[1] + (i-1)(40/(n-1)):
            return pizzasearch(alist, min, mid)
        else:
            return pizzasearch(alist, mid, max)
    else:
        return alist[min,min+1]


[n] = [int(x) for x in sys.stdin.readline().split()]
alist = [float(x) for x in sys.stdin.readline().split()]
pair = pizzasearch(alist)

ls = ""
for j in pair:
    ls = ls + str(j) + " "

print ls
