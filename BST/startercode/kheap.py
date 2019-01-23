import math

class minHeap(object):
    def __init__(self, k):
        self.heap_array = []
        self.k = k

    def add_num(self, x):
        self.heap_array.append(x)
        n = len(self.heap_array)
        self.heapify_up(n - 1)



    def pop_min(self):
        min = self.heap_array[0]
        n = len(self.heap_array)
        self.heap_array[0] = self.heap_array[-1]
        self.heap_array.pop()
        self.heapify_down(1)


    def heapify_up(self, index):
        parent = int(math.floor((index - 1)/k))
        if index < 1:
                return
        elif self.heap_array[index] < self.heap_array[parent]:
                tmp = self.heap_array[parent]
                self.heap_array[parent] = self.heap_array[index]
                self.heap_array[index] = tmp
        else:
                return

    def jthChild(self, index, j):
        return k * index + j

    def minChild(self, index):
        bestChild = self.jthChild(index, 1)
        j = 2
        pos = self.jthChild(index, j)
        while (j < k) and (pos < len(self.heap_array)):
            if self.heap_array[pos] < len(self.heap_array):
                bestChild = pos
            pos = self.jthChild(index, ++j)
        return bestChild

    def heapify_down(self, index):
        parent = int(math.floor((index - 1) / k))
        for j in range(0, k-1):
            if k * index + j <= len(self.heap_array) and self.heap_array[k * index + j] < self.heap_array[index]:
                smallest = k * index + j-1
            else:
                smallest = index
            if smallest < self.heap_array[parent]:
                tmp = self.heap_array[parent]
                self.heap_array[parent] = self.heap_array[smallest]
                self.heap_array[index] = tmp
            else:
                return

    # This will print the heap in the requested format
    def __str__(self):
        # Do not sort the heap array
        s = ""
        for i in self.heap_array:
            s += str(i) + " "
        return s.strip()

# Given Starter Code for IO. You need not modify code beneath this line

[k, c] = [2, 13]
h = minHeap(k)
command = ['add', 3700]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['print']
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 656]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 8375]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 2344]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['remove']
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 8365]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 6391]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 6349]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['remove']
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 7413]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['add', 641]
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h

command = ['print']
if command[0] == "add":
        h.add_num(int(command[1]))
elif command[0] == "remove":
        print h.pop_min()
elif command[0] == "print":
        print h