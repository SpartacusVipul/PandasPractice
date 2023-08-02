class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, curr_list, index_set):
            if start == len(nums):
                res_list.append(curr_list[:])  
                return
            
            for i in range(0, len(nums)):
                if i not in index_set:
                    curr_list.append(nums[i])
                    index_set.add(i)
                    backtrack(start + 1, curr_list, index_set)
                    curr_list.pop()
                    index_set.remove(i)

        res_list = []
        backtrack(0, [], set())
        return res_list
