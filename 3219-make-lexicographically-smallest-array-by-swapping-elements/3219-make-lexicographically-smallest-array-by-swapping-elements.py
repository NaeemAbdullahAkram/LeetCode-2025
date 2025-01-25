class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

# Here, we are creating empty queues and seperating groups of sorted numbers that exceed difference limit
# we are giving keys to each number with nums_to_group based on groups ie {1:0,3:0,5:0,8:1,9:1}
#Note: unhash the print statements to debug the code for better understanding
        group = []
        num_to_group = {}

        for num in sorted(nums):
            if not group or abs(num - group[-1][-1]) > limit:
                group.append(deque())
                #print(group)
            group[-1].append(num)
            num_to_group[num] = len(group) - 1
            #print(group,num_to_group)

# Here, we are taking each value in unsorted list, getting the key of the value and then appending the item to res from the queue that the key belongs to
        res = []
        for val in nums:
            key_of_n = num_to_group[val]
            res.append(group[key_of_n].popleft())
            #print("\n",group)
        return res