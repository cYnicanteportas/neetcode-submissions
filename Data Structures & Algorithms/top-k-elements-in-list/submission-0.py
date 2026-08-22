
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency : dict[int, int] = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        top_k = heapq.nlargest(k, frequency.keys(), key=frequency.get)

        return top_k