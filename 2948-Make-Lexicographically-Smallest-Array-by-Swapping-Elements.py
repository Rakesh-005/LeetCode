class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        idx = list(range(n))

        idx.sort(key=lambda i : nums[i])

        group = [[idx[0]]]
        prev = nums[idx[0]]

        for i in range(1, n):
            I = idx[i]
            x = nums[I]
            if x - prev <= limit:
                group[-1].append(I)
            else:
                group.append([I])
            prev = x
        for seq in group:
            values = [nums[index] for index in seq]
            values.sort()
            seq.sort()
            for i in range(len(seq)):
                nums[seq[i]] = values[i]

        return nums        
