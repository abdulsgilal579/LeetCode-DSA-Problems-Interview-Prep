class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sets = {}
        for number in nums:
            if number in sets:
                sets[number] += 1
            else:
                sets[number] = 1
        asc = {
            k: v
            for k, v in sorted(sets.items(), key=lambda item: item[1], reverse=True)
        }
        return list(asc.keys())[:k]
