# Course: CS261 - Data Structures
# Assignment: 5
# Student: Minkyong Lee
# Description: MinHeap Implementation


# Import pre-written DynamicArray and LinkedList classes
from a5_include import DynamicArray


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property.
        Runtime complexity of its implementation must be O(logN)
        """

        self.heap.append(node)
        cur_index = self.heap.length() - 1
        parent_index = int((cur_index - 1) / 2)

        # the added node percolates up the tree until it reaches the root or parent node's value is less
        while cur_index > 0 and self.heap.get_at_index(parent_index) > self.heap.get_at_index(cur_index):
            self.heap.swap(parent_index, cur_index)
            cur_index = parent_index
            parent_index = int((cur_index - 1) / 2)

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap.
        If heap is empty, the method raises an Exception.
        Runtime complexity must be O(1).
        """
        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap.
        If the heap is empty, the method raises an Exception.
        Runtime complexity of this implementation must be O(logN).
        """
        if self.heap.length() == 0:
            raise MinHeapException

        min_value = self.heap.get_at_index(0)
        self.heap.swap(0, self.heap.length() - 1)  # replace the min node with the last filled node
        self.heap.pop()  # remove the min node
        self.percolate_down(0)   # call percolate_down helper method
        return min_value

    def percolate_down(self, cur_index):
        """
        Helper method to percolate node down the tree until the subtree is a valid heap
        Runtime complexity is O(logN)
        """
        while cur_index >= 0:
            swap_index = -1
            right_index = 2 * cur_index + 2
            left_index = 2 * cur_index + 1

            # Case where right child is less than the current node
            if right_index < self.heap.length() and self.heap.get_at_index(right_index) < self.heap.get_at_index(cur_index):
                # check if the left child is less than or equal to the right child. parent node will swap with left child
                if self.heap.get_at_index(left_index) <= self.heap.get_at_index(right_index):
                    swap_index = left_index
                else:
                    swap_index = right_index
            # Case where left child is less than the current node
            elif left_index < self.heap.length() and self.heap.get_at_index(left_index) < self.heap.get_at_index(cur_index):
                swap_index = left_index

            # swap the current node and the smaller child node (swap_index > 0 means that a swap is needed)
            if swap_index >= 0:
                self.heap.swap(cur_index, swap_index)

            cur_index = swap_index

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a dynamic array with objects in any order and builds a proper MinHeap from them.
        Current content of the MinHeap is lost.
        Runtime complexity must be O(N).
        """
        self.heap = DynamicArray()
        counter1 = 0

        # copy elements in da to the MinHeap array (O(N))
        for i in range(da.length()):
            self.heap.append(da.get_at_index(i))

        last_index = self.heap.length() - 1
        first_nonleaf = int((last_index - 1) / 2)

        # Start with the first non-leaf node in the tree and continue swapping nodes until
        # the tree is a valid heap (O(N))
        for pos in range(first_nonleaf, -1, -1):
            self.percolate_down(pos)

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
