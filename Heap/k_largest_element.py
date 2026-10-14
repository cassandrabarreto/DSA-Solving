""" 
    Write a function, kth_largest, that takes in a list of numbers and a value, k. 
    The function should return the k-th largest element of the list.

    kth_largest([9,2,6,6,1,5,8,7], 3) # -> 7

"""

# Method # 1

def kth_largest(numbers, k):
    sorted_nums = sorted(numbers)
    return sorted_nums[-k]


# Method # 2 
class MinHeap:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def swap(self, index1, index2):
        self.list[index1] , self.list[index2] = self.list[index2] , self.list[index1]

    def sift_up(self, index):
        current_index = index
        while current_index > 0:
            parent_index = (current_index - 1 ) // 2
            if self.list[current_index] < self.list[parent_index]:
                self.swap(parent_index, current_index)
                current_index = parent_index
            else:
                break

    def insert(self, val):
        self.list.append(val)
        self.sift_up(self.size() -1)

    def sift_down(self, index):
        current_index = index

        while current_index < self.size() -1:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2

            left_child_val = float('inf') if left_child_index >= self.size() else self.list[left_child_index]
            right_child_val = float('inf') if right_child_index >= self.size() else self.list[right_child_index]

            smaller_child_val = left_child_val if left_child_val < right_child_val else right_child_val
            smaller_child_index = left_child_index if left_child_val < right_child_val else right_child_index

            if self.list[current_index] > smaller_child_val:
                self.swap(current_index, smaller_child_index)
                current_index = smaller_child_index
            else:
                break

    def extract_min(self):
        if self.is_empty():
            return None

        if self.size() == 1:
            return self.list.pop()

        min_val = self.list[0]
        self.list[0] = self.list.pop()
        self.sift_down(0)
        return min_val

def kth_largest(numbers, k):
    heap = MinHeap()

    for num in numbers:
        heap.insert(num)
        if heap.size() > k:
            heap.extract_min()
    return heap.extract_min()

# Method #3

import heapq

def kth_largest(numbers, k):
    my_heap = []
    for num in numbers:
        heapq.heappush(my_heap, num)
        if len(my_heap) > k:
            heapq.heapop(my_heap)
    return heapq.heappop(my_heap)

