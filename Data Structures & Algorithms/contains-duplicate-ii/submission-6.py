class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        container = set()
        l=0
        for r in range(len(nums)):
            while r-l>k:
                if nums[l] in container:
                    container.remove(nums[l])
                l+=1
            if nums[r] in container:
                return True
            container.add(nums[r])
        return False
        