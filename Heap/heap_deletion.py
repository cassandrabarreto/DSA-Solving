""" 
    Implement the extract_min method for the existing class. 
    The method should return and remove the smallest value in the heap,
    maintaining min heap order and height balance.
    Start by watching the approach video. 
    You'll also want to follow along with the walkthrough video. 
    You won't know how to implement this if it is your first time dealing with heaps.
"""

class MinHeap:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)
  
    def swap(self, index_1, index_2):
        self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
  
    def sift_up(self, index):
        current_index = index
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.list[current_index] < self.list[parent_index]:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break
    
    def insert(self, val):
        self.list.append(val)
        self.sift_up(self.size() - 1)
      
    def extract_min(self):
        pass