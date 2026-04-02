class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsset=set()
        i=0
        for r in range(len(nums)):
            if r-i>k:
                if nums[i] in numsset:
                    numsset.remove(nums[i])
                i+=1
            if nums[r] in numsset:
                return True
            numsset.add(nums[r])
        return False

