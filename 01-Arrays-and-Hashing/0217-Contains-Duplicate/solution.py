class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # # sln 1 - worst (inbuilt hasing)
        # time - O(n); space - O(n)
        # return len(nums) != len(set(nums))

        # ===================================
        # sln 2 - average
        # approach - Hash Set (Optimal Time)
        # time - O(n); space - O(n)
        # seen = set()
        # for element in nums:
        #     if element in seen:
        #         return True
        #     seen.add(element)
        # return False

        # ===================================
        # sln 3 - best
        # approach - two pointer - adjacent element
        # Sorting (Optimal Space)
        # time - O(n log n); space - O(1)
        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False