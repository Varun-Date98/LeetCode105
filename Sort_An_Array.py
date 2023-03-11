import heapq
from typing import List


'''
912. Sort an Array | Medium
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible.
---------------------------------------------------------------------------------

'''


class MergeSort:
    def __init__(self, nums: List[int]) -> None:
        self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums: List[int], left: int, right: int) -> None:
        if left < right:
            mid = left + (right - left) // 2
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)

    def merge(self, nums: List[int], left: int, mid: int, right:int):
        k = left
        i, j = 0, 0
        A = [num for num in nums[left:mid + 1]]
        B = [num for num in nums[mid + 1:right + 1]]

        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                nums[k] = A[i]
                i += 1
            else:
                nums[k] = B[j]
                j += 1
            
            k += 1
        
        while i < len(A):
            nums[k] = A[i]
            i += 1
            k += 1
        
        while j < len(B):
            nums[k] = B[j]
            j += 1
            k += 1


class QuickSort:
    def __init__(self, nums: List[int]) -> None:
        self.quickSort(nums, 0, len(nums) - 1)
    
    def quickSort(self, nums: List[int], left: int, right: int) -> None:
        if left < right:
            Idx = self.partition(nums, left, right)
            self.quickSort(nums, left, Idx)
            self.quickSort(nums, Idx + 1, right)
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        i, j = left, right
        pivot = nums[left]

        while i < j:
            while i < right and nums[i] <= pivot:
                i += 1
            
            while j > left and nums[j] > pivot:
                j -= 1
            
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[left], nums[j] = nums[j], nums[left]
        return j


class HeapSort:
    def __init__(self, nums: List[int]) -> None:
        self.heapSort(nums)
    
    def heapSort(self, nums: List[int]) -> None:
        heap = []
        right = len(nums) - 1

        for num in nums:
            heapq.heappush(heap, num)
        
        while heap:
            num = heapq.heappop(heap)
            nums[right] = num
            right -= 1
