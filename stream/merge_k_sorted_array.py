""" 
Python3 program to merge k sorted arrays of size n each 
https://www.geeksforgeeks.org/merge-k-sorted-arrays/
"""
import sys 
from typing import List, Optional 
Matrix = List[List[int]] 


class MinHeapNode: 
	def __init__(self, el, i, j): 
		self.element = el # the element to be sorted 
		self.i = i		 # index of array from which element is taken 
		self.j = j		 # index of next element to be picked from array 


class MinHeap: 
	def __init__(self, ar: List[MinHeapNode], size: int): 
		self.heap_size = size 
		self.heap_arr = ar 
		i = (self.heap_size - 1) // 2
		while i >= 0: 
			self.min_heapify(i) 
			i -= 1

	""" 
	A recursive method to heapify a subtree 
	with the root at given index. This method 
	assumes that the subtree are already heapified 
	"""
	def min_heapify(self, i): 
		l = left(i) 
		r = right(i) 
		smallest = i 
		if l < self.heap_size and self.heap_arr[l].element < self.heap_arr[i].element: 
			smallest = l 
		if r < self.heap_size and self.heap_arr[r].element < self.heap_arr[smallest].element: 
			smallest = r 
		if smallest != i: 
			swap(self.heap_arr, i, smallest) 
			self.min_heapify(smallest) 

	def get_min(self) -> Optional: 
		if self.heap_size <= 0: 
			print('Heap underflow') 
			return None
		return self.heap_arr[0] 

	# Replace root with new root 
	def replace_min(self, root): 
		self.heap_arr[0] = root 
		self.min_heapify(0) 


def left(i): 
	return 2 * i + 1


def right(i): 
	return 2 * i + 2


def swap(arr: List[MinHeapNode], i, j): 
	temp = arr[i] 
	arr[i] = arr[j] 
	arr[j] = temp 


def merge_k_sorted_arrays(arr: Matrix, k: int): 
	h_arr = [] 
	result_size = 0
	for i in range(len(arr)): 
		node = MinHeapNode(arr[i][0], i, 1) 
		h_arr.append(node) 
		result_size += len(arr[i]) 

	min_heap = MinHeap(h_arr, k) 
	result = [0]*result_size 
	for i in range(result_size): 
		root = min_heap.get_min() 
		result[i] = root.element 
		if root.j < len(arr[root.i]): 
			root.element = arr[root.i][root.j] 
			root.j += 1
		else: 
			root.element = sys.maxsize 
		min_heap.replace_min(root) 
	for x in result: 
		print(x, end=' ') 
	print() 


if __name__ == '__main__': 
	arr = [ 
		[2, 6, 12, 34], 
		[1, 9, 20, 1000], 
		[23, 34, 90, 2000] 
	] 
	print('Merged Array is:') 
	merge_k_sorted_arrays(arr, len(arr)) 

# The code is contributed by Rajat Srivastava 
