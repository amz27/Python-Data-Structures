import sys


def cities(months, switchingCost, profitInCity1, profitInCity2):
    #
    # Please write code here
    #
    profit = 0
    h, w = months, 2
    M = [[0 for x in range(w)] for y in range(h)]
    tb_a = [[0 for d in range(w)] for e in range(h)]
    cityList = [0 for i in range(months)]
    M[0][0] = profitInCity1[0]
    M[0][1] = profitInCity2[0] - switchingCost
    if months == 0:
        return 0
    if months == 1:
        if M[0][0] > M[0][1]:
            profit = M[0][0]
            tb_a[0][0] = 1
            cityList[0] = tb_a[0][0]
        else:
            profit = M[0][1]
            tb_a[0][0] = 2
            cityList[0] = tb_a[0][0]

    else:
        for i in range(1,months):
            if M[i-1][0] + profitInCity1[i] > M[i-1][1] - switchingCost + profitInCity1[i]:
                M[i][0] = M[i-1][0] + profitInCity1[i]
                tb_a[i-1][0] = 2
            else:
                M[i][0] = M[i - 1][1] - switchingCost + profitInCity1[i]
                tb_a[i -1][0] = 2
            if M[i-1][1] + profitInCity2[i]> M[i-1][0] - switchingCost + profitInCity2[i]:
                M[i][1] = M[i-1][1] + profitInCity2[i]
                tb_a[i-1][1] = 1
            else:
                M[i][1] = M[i-1][0] - switchingCost + profitInCity2[i]
                tb_a[i-1][1] = 2

            if M[months-1][0] > M[months-1][1]:
                profit = M[months-1][0]
                cityList[months - 1] = 1
            else:
                profit = M[months-1][1]
                cityList[months - 1] = 2

            for j in range(1, months):
                if M[months - 1][0] > M[months - 1][1]:
                    cityList[j - 1] = tb_a[j - 1][1]
                else:
                    cityList[j - 1] = tb_a[j - 1][0]

    return profit, cityList


# Read input
header = [1, 5]
city1 = [8]
city1 = [int(x) for x in city1]
city2 = [15]
city2 = [int(x) for x in city2]

profit, cityList = cities(header[0], header[1], city1, city2)
listString = ' '.join(str(x) for x in cityList)

print profit  # max profit
print listString  # cities
