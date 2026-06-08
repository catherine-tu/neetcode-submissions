class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach: minheap of k largest elts
        heap = []
        heapq.heapify(heap)

        for num in nums:
            # need at least k elts
            if len(heap) < k: 
                heapq.heappush(heap, num)
            # if heap is greater than smallest
            elif heap[0] < num:
                heapq.heapreplace(heap, num)
        
        return heap[0]






        # maintain a min heap of the k biggest number
        # return the root

        # heap = []
        # heapq.heapify(heap)

        # for num in nums:
        #     # keep adding elements as long as heap isnt size k
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     # if heap is size k, but we found a larger number, push and replace
        #     elif heap[0] < num:
        #         heapq.heappushpop(heap, num)

        # return heap[0]
        