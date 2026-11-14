class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_map = {}
        for num in nums:
            dict_map[num] = dict_map.get(num, 0) + 1 #get current count of that number, if not in map count will be 0
        
        arr = []
        for key, val in dict_map.items(): #key is the num, val is count
            arr.append([val,key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res