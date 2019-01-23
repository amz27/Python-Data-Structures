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
        tmp = self.heap_array[0]
        self.heap_array[0] = self.heap_array[-1]
        self.heap_array.pop()
        self.heapify_down(0)
        return tmp

    def heapify_up(self, index):
        parent = int(math.floor((index - 1)/k))
        if index < 1:
                return
        elif self.heap_array[index] < self.heap_array[parent]:
                    tmp = self.heap_array[parent]
                    self.heap_array[parent] = self.heap_array[index]
                    self.heap_array[index] = tmp
                    self.heapify_up(parent)

    def heapify_down(self, index):
        if k * index + k - (k - 1) > len(self.heap_array):
            return 0
        else:
            minchild = k * index + 1
            for j in range(2, k+1):
                if k * index + j <= len(self.heap_array):
                    if self.heap_array[minchild] < self.heap_array[k * index + j]:
                        minchild = minchild
                    else:
                        minchild = k * index + j

                    if self.heap_array[minchild] < self.heap_array[index]:
                        tmp = self.heap_array[index]
                        self.heap_array[index] = self.heap_array[minchild]
                        self.heap_array[minchild] = tmp
                        self.heapify_down(minchild)



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

if __name__ == '__main__':
    [k, c] = [int(x) for x in raw_input().split()]
    h = minHeap(k)
    for i in range(c):
        command = raw_input().split()
        if command[0] == "add":
            h.add_num(int(command[1]))
        elif command[0] == "remove":
            print h.pop_min()
        elif command[0] == "print":
            print h