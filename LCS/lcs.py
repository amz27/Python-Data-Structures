import sys

def lcs(a , b):
    c = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = max(c[i+1][j], c[i][j+1])

    commonString = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if c[x][y] == c[x-1][y]:
            x = x - 1
        elif c[x][y] == c[x][y-1]:
            y = y - 1
        else:
            assert a[x-1] == b[y-1]
            commonString = a[x-1] + commonString
            x = x - 1
            y = y - 1
    return (len(commonString), commonString)
    #



# Read input
stringA = "abcdef"
stringB = "xbayzdfe"

lcsSol = lcs(stringA, stringB)

print str(lcsSol[0])
print str(lcsSol[1])