# In this file, you will develop a Min Heap to use in a priority queue.
# A priority queue is a fundamental data structure for many of the algorithms we will cover in this class,
# so it is important to get the fundamentals right.

# In a normal queue, you insert items, and they are removed in first-in, first-out order (FIFO).
# In a priority queue, you insert an arbitrary object AND a priority value for that item.
# When an item is requested, the item with the lowest priority value is returned (and removed).
# Read more: https://en.wikipedia.org/wiki/Priority_queue

# Fundamental to the Priority Queue is the "Heap" data structure.
# Heaps (especially min-heaps) allow for fast retrieval of the smallest-priority element,
# and efficient re-ordering after inserts/removals.
# Once you have a heap, implementing a Priority Queue is straightforward.

# A min-heap can be thought of as a binary tree where each node has priority <= its children.
# This means the smallest-priority element will always be at index 0.

# The tree is stored in a list. For a node at index i:
# left child index = 2*i + 1
# right child index = 2*i + 2
# parent index = (i - 1) // 2

# When you add an item, append it to the end of the list, then "bubble up"
# by swapping it with its parent while it has a smaller priority than the parent.

# When you pop the minimum item, you remove and return the item at index 0.
# Then move the last element to index 0 and "bubble down" by swapping with the smaller child
# until the heap property is restored.

# Read more: https://en.wikipedia.org/wiki/Heap_(data_structure)

# You can also watch this video, but note it starts indexing at 1 (different math).
# You may implement a 1-indexed heap if you want (leave index 0 unused), or use 0-indexing.
# Either approach works:
# https://www.youtube.com/watch?v=0wPlzMU-k00

# For this assignment, the items added to the priority queue can be any object.
# You will only compute/compare priorities (ints).
# For peek() and pop(), return (item, priority) as a tuple.

class MinHeap:
    def __init__(self):
        # We'll store elements as tuples: (priority, item)
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.data:
            return self.data[0]
        else:
            return "None"

    def add(self, priority, item):
        self.data.append((priority, item)) #add new element to end of list
        idx = len(self.data) - 1 #0-based so index is one less than list length
        self._bubble_up(idx) #move up to proper priority

    def pop_min(self):
        if self.data: #check list not empty
            last_element = self.data[0] #save old root
            if len(self.data) == 1: #if list is 1 long no need to bubble
                self.data.pop()
                return last_element
            else:
                self.data[0], self.data[-1] = self.data[-1], self.data[0] #swap first and last elements
                self.data.pop() #pop old root
                self._bubble_down(0) #move new minimum element down to proper priority
                return last_element
        else:
            return "None"

    def _bubble_up(self, idx):
        parent = (idx - 1) // 2 #identify parent
        parent_priority = self.data[parent][0] #get parent priority
        idx_priority = self.data[idx][0] #get new element's priority
        while idx != 0 and parent_priority > idx_priority: #stop when parent is greater priority or when new element has become the new root
            self.data[idx], self.data[parent] = self.data[parent], self.data[idx] #swap new element and parent
            idx = parent #new element now has index of old parent
            parent = (idx - 1) // 2 #identify new parent
            parent_priority = self.data[parent][0] #get new parent's priority
            idx_priority = self.data[idx][0] #get new element's new priority

    def _bubble_down(self, idx):
        left_child = 2 * idx + 1 #identify potential left child
        right_child = 2 * idx + 2 #identify protential right child
        if left_child >= len(self.data): #stop if no left child
            pass
        else:
            if right_child >= len(self.data): #if no right child, left child is the lowest priority child
                small = left_child
            elif self.data[left_child][0] > self.data[right_child][0]: #if both children exist, check if right child has lower priority
                small = right_child
            else:
                small = left_child #if both exist, and right does not have lowest priority, left is lowest priority
            small_priority = self.data[small][0] #get priority of lowest priority child
            idx_priority = self.data[idx][0] #get priority of element to be bubbled down
            while small_priority < idx_priority and left_child < len(self.data): #stop when all children are lower priority than parent or when there are no children
                self.data[idx], self.data[small] = self.data[small], self.data[idx] #swap parent and lowest priority child
                idx = small #element being bubbled down now has index of smallest child
                left_child = 2 * idx + 1 #find new potential left child
                right_child = 2 * idx + 2 #find new potential right child
                if right_child >= len(self.data): #if no right child, left child is the lowest priority
                    small = left_child
                elif self.data[left_child][0] > self.data[right_child][0]: #if both children exist, check if right child has lower priority
                    small = right_child
                else:
                    small = left_child #if both exist, and right does not have lowest priority, left is lowest priority
                small_priority = self.data[small][0] #get priority of lowest priority child
                idx_priority = self.data[idx][0] #get priority of element to be bubbled down

# Once you have a min heap, the priority queue is pretty straightforward. 
# Make sure you understand what it is doing

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def is_empty(self):
        return self.heap.is_empty()

    def add(self, priority, item):
        self.heap.add(priority, item)

    def pop(self):
        return self.heap.pop_min()

    def peek(self):
        return self.heap.peek()

    def __len__(self):
        return len(self.heap)
