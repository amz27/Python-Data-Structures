import sys 


def pizzaSearch(alist):
    locations = pizzasearch(alist, 0, len(alist) - 1)
    return locations


def pizzasearch(alist, min, max):
    array = []
    if min + 1 == max:
        array.append(min)
        array.append(max)
        return array
    else:
        mid = (min + max) / 2
        avg_left = (alist[mid] - alist[min]) / (mid - min)
        avg_right = (alist[max] - alist[mid]) / (max - mid)
        if avg_left < avg_right:
            return pizzasearch(alist, min, mid)
        else:
            return pizzasearch(alist, mid, max)


n = 5
alist = [1, 20, 23, 24, 40]
pair = pizzaSearch(alist)

ls = ""
for j in pair:
    ls = ls + str(j) + " "

print ls
