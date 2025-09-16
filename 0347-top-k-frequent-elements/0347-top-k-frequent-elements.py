class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1

        sortList = sorted(hashMap.items(), key=lambda x:x[1], reverse=True)
        
        return [key for key, v in sortList[:k]]